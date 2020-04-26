from decimal import Decimal
from flask import Flask, Blueprint, jsonify, request, session, g, redirect, url_for, abort, render_template, flash, \
    current_app
from flask_wtf import FlaskForm

from ..forms import ConfigurationForm
from ..forms import AddPostForm
from ..forms import AddPlayerForm
from ..forms import AddLocationForm
from ..forms import CreateSeasonForm

from ..backend import PlayfieldAPI

app = Flask(__name__)

admin = Blueprint('admin',
                  __name__,
                  static_url_path='/admin',
                  static_folder='../static',
                  template_folder='../templates')

playfield = PlayfieldAPI("host.docker.internal", "8080")


@admin.route('/admin')
@admin.route('/admin/runleague')
def show_admin():
    player_json = playfield.api_request("get", "player", "all_players", None)
    location_json = playfield.api_request("get", "location", "all_locations", None)

    # If error querying API flash message to user
    if player_json is not "Error" and player_json is not None:
        entries = playfield.parse_json(player_json)
    else:
        flash("Problem accessing Playfield API")
        entries = {}

    # If error querying API flash message to user
    if location_json is not "Error" and location_json is not None:
        locations = playfield.parse_json(location_json)
    else:
        flash("Problem accessing Playfield API")
        locations = {}

    return render_template('show_admin.html',
                           title="Admin - Run League",
                           highlightActive='runleague',
                           entries=entries,
                           locations=locations)


@admin.route('/admin/players', methods=['GET', 'POST'])
def show_admin_players():
    # Query API for all players
    player_json = playfield.api_request("get", "player", "all_players", None)

    # If error querying API flash message to user
    if player_json is not "Error" and player_json is not None:
        playerEntries = playfield.parse_json(player_json)
    else:
        flash("Problem accessing Playfield API")
        playerEntries = {}

    playerform = AddPlayerForm()

    # When a form is submitted, process it
    if request.method == 'POST':

        # Process new player form
        if playerform.validate_on_submit():

            # Pull submitted data from the form
            data = dict(name=request.form['name'],
                        nick=request.form['nick'],
                        email=request.form['email'],
                        phone=request.form['phone'],
                        location=request.form['location'],
                        ifpanumber=request.form['ifpanumber'],
                        pinside=request.form['pinside'],
                        notes=request.form['notes'],
                        status=request.form['status'],
                        active=request.form['active'])

            results = playfield.api_request("post", "player", "add_player", data)

            if results is not "Error":
                # Succeeded, so lets display a message
                flash("Added new player - %s" % request.form['name'])
            else:
                flash("Problem accessing Playfield API")

            return render_template('show_admin_players.html',
                                   title="Admin - Manage Players",
                                   highlightActive='players',
                                   entries=playerEntries,
                                   playerform=playerform)

        else:
            # Server side validation failed, lets not proceed, and instead display error
            for field, errors in playerform.errors.items():
                for error in errors:
                    flash(u"Error in the %s field - %s" % (getattr(playerform, field).label.text, error))

            return render_template('show_admin_players.html',
                                   title="Admin - Manage Players",
                                   highlightActive='players',
                                   entries=playerEntries,
                                   playerform=playerform)

    return render_template('show_admin_players.html',
                           title="Admin - Manage Players",
                           highlightActive='players',
                           entries=playerEntries,
                           playerform=playerform)


@admin.route('/admin/_admin_player_info')
# Get all the admin editable details about a player from the database and return as JSON
def admin_player_info():
    pid = request.args.get('pid', 0, type=str)

    # Query API for specific player by id
    player_json = playfield.api_request("get", "player", "player_by_id", pid)

    # If error querying API flash message to user
    if player_json is not "Error" and player_json is not None:
        entries = playfield.parse_json(player_json)
    else:
        # flash("Problem accessing Playfield API")
        entries = {}

    # TODO: Make API call to IFPA to refresh stored player info

    # Parse out results and compile into JSON
    for entry in entries:
        pid = entry['player_id']
        nick = entry['nick']
        name = entry['name']
        phone = entry['phone']
        email = entry['email']
        location = entry['location']
        ifpanumber = entry['ifpanumber']
        pinside = entry['pinside']
        notes = entry['notes']
        status = entry['status']
        active = entry['active']

    return jsonify(pid=pid,
                   nick=nick,
                   name=name,
                   phone=phone,
                   email=email,
                   location=location,
                   ifpanumber=ifpanumber,
                   pinside=pinside,
                   notes=notes,
                   status=status,
                   active=active)


@admin.route('/admin/locations', methods=['GET', 'POST'])
def show_admin_locations():
    # Query API for locations
    location_json = playfield.api_request("get", "location", "all_locations", None)

    # If error querying API flash message to user
    if location_json is not "Error" and location_json is not None:
        locations = playfield.parse_json(location_json)
    else:
        flash("Problem accessing Playfield API")
        locations = {}

    locationform = AddLocationForm()

    # When a form is submitted, process it
    if request.method == 'POST':

        # Process new location form
        if locationform.validate_on_submit():

            # locationname = request.form['name']
            # locationaddress = request.form['address']
            # locationprivate = request.form['addressprivate']
            # locationtype = request.form['loctype']
            # locationnotes = request.form['notes']
            # locationactive = request.form['active']

            # Pull submitted data from the form
            data = dict(name=request.form['name'],
                        address=request.form['address'],
                        address_private=request.form['addressprivate'],
                        notes=request.form['notes'],
                        loc_type=request.form['loctype'],
                        active=request.form['active'])

            results = playfield.api_request("post", "location", "add_location", data)

            if results is not "Error":
                # Succeeded, so lets display a message
                flash("New location added! - %s" % request.form['name'])
            else:
                flash("Problem accessing Playfield API")

            return render_template('show_admin_locations.html',
                                   title="Admin - Manage Locations",
                                   highlightActive='locations',
                                   locations=locations,
                                   locationform=locationform)

        else:
            # Server side validation failed, lets not proceed, and instead display error
            for field, errors in locationform.errors.items():
                for error in errors:
                    flash(u"Error in the %s field - %s" % (getattr(locationform, field).label.text, error))

            return render_template('show_admin_locations.html',
                                   title="Admin - Manage Locations",
                                   highlightActive='locations',
                                   locations=locations,
                                   locationform=locationform)

    return render_template('show_admin_locations.html',
                           title="Admin - Manage Locations",
                           highlightActive='locations',
                           locations=locations,
                           locationform=locationform)


@admin.route('/admin/_admin_location_info')
def admin_location_info():
    location_id = request.args.get('location_id', 0, type=str)

    location_json = playfield.api_request("get", "location", "location_by_id", location_id)

    # If error querying API flash message to user
    if location_json is not "Error" and location_json is not None:
        entries = playfield.parse_json(location_json)
    else:
        flash("Problem accessing Playfield API")
        entries = {}

    # Parse out results and compile into JSON
    for entry in entries:
        lid = entry['lid']
        name = entry['name']
        address = entry['address']
        notes = entry['notes']
        active = entry['active']

        return jsonify(lid=lid, name=name, address=address, notes=notes, active=active)


@admin.route('/admin/_games_for_location')
def games_for_location():
    location_id = request.args.get('location_id', 0, type=str)

    location_json = playfield.api_request("get", "location", "active_machines_for_location", location_id)

    # If error querying API flash message to user
    if location_json is not "Error" and location_json is not None:
        entries = playfield.parse_json(location_json)
    else:
        flash("Problem accessing Playfield API")
        entries = {}

    return jsonify(games=entries)


@admin.route('/admin/_update_location_status')
# Update the location status.  Inactive locations are not available for league play/view.
def update_location_status():
    location_id = request.args.get('location_id', 0, type=str)
    active = request.args.get('active', 0, type=int)
    if active == 1:
        activevalue = True
    elif active == 0:
        activevalue = False
    else:
        activevalue = False

    data = (location_id, str(activevalue),)
    retval = playfield.api_request("get", "location", "set_active", data)

    return jsonify(ret=0)


@admin.route('/admin/content', methods=['GET', 'POST'])
def show_admin_content():

    # Get all posts

    posts = ""
    postform = AddPostForm()

    # Get the current configuration

    leaguename = "League name here"
    welcometext = "Welcome text here"

    form = ConfigurationForm(leaguename=leaguename, welcometext=welcometext)

    form.leaguename.data = leaguename
    form.welcometext.data = welcometext

    # When a form is submitted, process it
    if request.method == 'POST':
        # Process new post form
        if postform.validate_on_submit():

            posttitle = request.form['title']
            postcontent = request.form['content']

            flash("New post '%s' created!" % (posttitle))

            return render_template('show_admin_content.html',
                                   title="Admin - Edit Content",
                                   highlightActive='content',
                                   posts=posts,
                                   postform=postform,
                                   form=form,
                                   leaguename=leaguename,
                                   welcometext=welcometext)

        else:
            for field, errors in postform.errors.items():
                for error in errors:
                    flash(u"Error in the %s field - %s" % (getattr(postform, field).label.text, error))

            return render_template('show_admin_content.html',
                                   title="Admin - Edit Content",
                                   highlightActive='content',
                                   posts=posts,
                                   postform=postform,
                                   form=form,
                                   leaguename=leaguename,
                                   welcometext=welcometext)

    return render_template('show_admin_content.html',
                           title="Admin - Edit Content",
                           highlightActive='content',
                           posts=posts,
                           postform=postform,
                           form=form,
                           leaguename=leaguename,
                           welcometext=welcometext)


@admin.route('/admin/config', methods=['GET', 'POST'])
def show_admin_config():

    sid = ""
    length = ""
    dropweeks = ""
    numrounds = ""
    numgames = ""
    scoring = ""
    seeding = ""
    order = ""
    drawing = ""
    dues = ""
    running = ""

    historicalSeasons = ""

    form = CreateSeasonForm(seeding=seeding, scoring=scoring, playorder=order, drawing=drawing)

    # Set values for form fields.  If season data already exists, but isn't started
    # the current data will be made available for edit.
    form.seasonLength.data = length
    form.dropWeeks.data = dropweeks
    form.numRounds.data = numrounds
    form.numGames.data = numgames
    if dues != "":
        form.dues.data = Decimal(dues)
    form.sid.data = sid

    # When the form is submitted, process it.
    if request.method == 'POST':
        # If all looks good update the database (if sid included) or insert new record
        if form.validate_on_submit():

            sid = request.form['sid']
            seasonLength = request.form['seasonLength']
            dropWeeks = request.form['dropWeeks']
            numRounds = request.form['numRounds']
            numGames = request.form['numGames']
            dues = request.form['dues']
            seeding = request.form['seeding']
            scoring = request.form['scoring']
            playorder = request.form['playorder']
            drawing = request.form['drawing']

            # If season exists (and is not started)
            if sid == "" and not running:

                flash("New season added!")
            # Update existing season record (if not started)
            elif sid > 0 and not running:

                flash("Season updated!")

            # If the season has started
            else:
                flash("A season that is currently running canot be modified!")

            return render_template('show_admin_config.html',
                                   title="Admin - Configure League",
                                   highlightActive='configure',
                                   form=form,
                                   cursid=sid,
                                   currunning=running,
                                   historicalseason=historicalSeasons)

        # If the form fails validation, provide reasonable output via flash
        else:

            for field, errors in form.errors.items():
                for error in errors:
                    flash(u"Error in the %s field - %s" % (getattr(form, field).label.text, error))

            return render_template('show_admin_config.html',
                                   title="Admin - Configure League",
                                   highlightActive='configure',
                                   form=form,
                                   cursid=sid,
                                   currunning=running,
                                   historicalseason=historicalSeasons)

    return render_template('show_admin_config.html',
                           title="Admin - Configure League",
                           highlightActive='configure',
                           form=form,
                           cursid=sid,
                           currunning=running,
                           historicalseason=historicalSeasons)


@admin.route('/admin/_update_season_hidden')
# Update the season activity.  Inactive seasons are not available for view.
def update_season_hidden():
    sid = request.args.get('sid', 0, type=int)
    active = request.args.get('active', 0, type=int)
    if active == 1:
        activevalue = True
    elif active == 0:
        activevalue = False
    else:
        activevalue = False

    return jsonify(ret=0)


@admin.route('/admin/data')
def show_admin_data():
    return render_template('show_admin_data.html', title="Admin - Export Data", highlightActive='export')
