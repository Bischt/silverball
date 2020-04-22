from decimal import Decimal
import psycopg2
import psycopg2.extras
import requests
from flask import Flask, Blueprint, jsonify, request, session, g, redirect, url_for, abort, render_template, flash, current_app
#from flask_openid import OpenID
from flask_wtf import FlaskForm

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from ..forms import ConfigurationForm
from ..forms import AddPostForm
from ..forms import AddPlayerForm
from ..forms import AddLocationForm
from ..forms import CreateSeasonForm

app=Flask(__name__)

admin = Blueprint('admin', 
                  __name__, 
                  static_url_path='/admin', 
                  static_folder='../static', 
                  template_folder='../templates')

# Connect to database
def connect_db():
    try:
        conn_string = "dbname=%s user=%s host=%s password=%s" % (current_app.config["DB_NAME"], 
                                                                 current_app.config["DB_USER"], 
                                                                 current_app.config["DB_HOST"], 
                                                                 current_app.config["DB_PASS"])
        return psycopg2.connect(conn_string)
        print("DB connection successful!")
    except:
        print("I am unable to connect to the database")
        exit(1)

@admin.route('/admin')
@admin.route('/admin/runleague')
def show_admin():
    conn = connect_db()
    dbcur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    dbcur.execute("select pid, nick, name, email, notes, status, active from player order by active")
    entries = dbcur.fetchall()
    dbcur.execute("select lid, name, address, active, notes from location order by active")
    locations = dbcur.fetchall()
    dbcur.close()
    conn.close()
    return render_template('show_admin.html', 
           title="Admin - Run League", 
           highlightActive='runleague', 
           entries=entries, 
           locations=locations)

@admin.route('/admin/players', methods=['GET', 'POST'])
def show_admin_players():
    conn = connect_db()
    dbcur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    dbcur.execute("select pid, nick, name, email, phone, location, ifpanumber, pinside, notes, status, active from player order by active")
    playerEntries = dbcur.fetchall()

    playerform = AddPlayerForm()

    # When a form is submitted, process it
    if request.method == 'POST':

        # Process new player form
        if playerform.validate_on_submit():

            # Pull submitted data from the form
            playerinitials = request.form['nick']
            playername = request.form['name']
            playeremail = request.form['email']
            playerphone = request.form['phone']
            playerlocation = request.form['location']
            playerifpanumber = request.form['ifpanumber']
            playerpinside = request.form['pinside']
            playernotes = request.form['notes']
            playerstatus = request.form['status']
            playeractive = request.form['active']

            # Add new player record to the database
            dbcur.execute("insert into player (nick, name, email, phone, location, ifpanumber, pinside, notes, status, active) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (playerinitials, playername, playeremail, playerphone, playerlocation, playerifpanumber, playerpinside, playernotes, playerstatus, playeractive))

            conn.commit()

            # Succeeded, so lets display a message
            flash("Added new player - %s" % (playername))

            dbcur.close()
            conn.close()

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

            dbcur.close()
            conn.close()

            return render_template('show_admin_players.html',
                   title="Admin - Manage Players",
                   highlightActive='players',
                   entries=playerEntries,
                   playerform=playerform)

    dbcur.close()
    conn.close()
    return render_template('show_admin_players.html', 
           title="Admin - Manage Players", 
           highlightActive='players', 
           entries=playerEntries,
           playerform=playerform)

@admin.route('/admin/_admin_player_info')
# Get all the admin editable details about a player from the database and return as JSON
def admin_player_info():
    pid = request.args.get('pid', 0, type=int)
    conn = connect_db()
    dbcur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    SQL = "select pid, nick, name, phone, email, location, ifpanumber, pinside, notes, status, active from player where pid=%s;"
    data = (pid, )
    dbcur.execute(SQL, data)
    entries = dbcur.fetchall()
    dbcur.close()
    conn.close()

    # Make API call to IFPA to refresh stored player info

    # Parse out results and compile into JSON
    for entry in entries:
        pid = entry['pid']
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
    conn = connect_db()
    dbcur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    dbcur.execute("select lid, name, address, active, notes from location order by active")
    locations = dbcur.fetchall()

    locationform = AddLocationForm()

    # When a form is submitted, process it
    if request.method == 'POST':

        # Process new location form
        if locationform.validate_on_submit():

            # Pull submitted data from the form
            locationname = request.form['name']
            locationaddress = request.form['address']
            locationprivate = request.form['addressprivate']
            locationtype = request.form['loctype']
            locationnotes = request.form['notes']
            locationactive = request.form['active']

            # Add new location record to the database
            dbcur.execute("insert into location (name, address, addressPrivate, notes, locType, active) values (%s, %s, %s, %s, %s, %s)", (locationname, locationaddress, locationprivate, locationnotes, locationtype, locationactive))

            conn.commit()

            # Succeeded, so lets display a message
            flash("New location added! - %s" % (locationname))

            dbcur.close()
            conn.close()

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

            dbcur.close()
            conn.close()

            return render_template('show_admin_locations.html',
                title="Admin - Manage Locations",
                highlightActive='locations',
                locations=locations,
                locationform=locationform)

    dbcur.close()
    conn.close()
    return render_template('show_admin_locations.html', 
           title="Admin - Manage Locations", 
           highlightActive='locations',
           locations=locations,
           locationform=locationform)

@admin.route('/admin/_admin_location_info')
def admin_location_info():
    lid = request.args.get('lid', 0, type=int)
    conn = connect_db()
    dbcur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    SQL = "select lid, name, address, notes, active from location where lid=%s;"
    data = (lid,)
    dbcur.execute(SQL, data)
    entries = dbcur.fetchall()
    dbcur.close()
    conn.close()

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
    lid = request.args.get('lid', 0, type=int)
    conn = connect_db()
    dbcur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    SQL = "select game.gid, game.mid, game.condition, game.notes, machines.name, machines.abbr, machines.manufacturer, machines.manDate, machines.players, machines.gameType, machines.theme, machines.ipdbURL from game inner join machines on game.mid=machines.mid where game.active = true and game.lid = %s;"
    data = (lid,)
    dbcur.execute(SQL, data)
    entries = dbcur.fetchall()
    dbcur.close()
    conn.close()

    return jsonify(games=entries)

@admin.route('/admin/_update_location_status')
# Update the location status.  Inactive locations are not available for league play/view.
def update_location_status():
    lid = request.args.get('lid', 0, type=int)
    active = request.args.get('active', 0, type=int)
    if active == 1:
        activevalue = True
    elif active == 0:
        activevalue = False
    else:
        activevalue = False

    conn = connect_db()
    dbcur = conn.cursor()
    dbcur.execute("update location set active=%s where lid=%s", (activevalue, lid))
    conn.commit()
    dbcur.close()
    conn.close()
    return jsonify(ret=0)

@admin.route('/admin/content', methods=['GET', 'POST'])
def show_admin_content():
    conn = connect_db()
    dbcur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # Get all posts
    dbcur.execute("select pid, timestamp, title, content, active from posts order by timestamp")
    posts = dbcur.fetchall()

    postform = AddPostForm()

    # Get the current configuration
    dbcur.execute("select leagueName, welcomeText from config where cid=1")
    currentConfig = dbcur.fetchall()

    leaguename = ""
    welcometext = ""

    for entry in currentConfig:
        leaguename = entry['leaguename']
        welcometext = entry['welcometext']

    form = ConfigurationForm(leaguename=leaguename, welcometext=welcometext)

    form.leaguename.data = leaguename
    form.welcometext.data = welcometext

    # When a form is submitted, process it
    if request.method == 'POST':
        # Process new post form
        if postform.validate_on_submit():

            posttitle = request.form['title']
            postcontent = request.form['content']

            dbcur.execute("insert into posts (title, content) values (%s, %s)", (posttitle, postcontent))

            conn.commit()

            flash("New post '%s' created!" % (posttitle))

            dbcur.close()
            conn.close()

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

            dbcur.close()
            conn.close()

            return render_template('show_admin_content.html',
                   title="Admin - Edit Content",
                   highlightActive='content',
                   posts=posts,
                   postform=postform,
                   form=form,
                   leaguename=leaguename,
                   welcometext=welcometext)

        # Process update content form
        if form.validate_on_submit():

            leaguename = request.form['leaguename']
            welcometext = request.form['welcometext']

            dbcur.execute("update config set leagueName=%s, welcomeText=%s where cid=1", (leaguename, welcometext))
            conn.commit()

            flash("Content Saved!")

            dbcur.close()
            conn.close()

            form.leaguename.data = leaguename
            form.welcometext.data = welcometext

            return render_template('show_admin_content.html',
                   title="Admin - Edit Content",
                   highlightActive='content',
                   posts=posts,
                   postform=postform,
                   form=form,
                   leaguename=leaguename,
                   welcometext=welcometext)

        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(u"Error in the %s field - %s" % (getattr(form, field).label.text, error))

            dbcur.close()
            conn.close()

            return render_template('show_admin_content.html',
                   title="Admin - Edit Content",
                   highlightActive='content',
                   posts=posts,
                   postform=postform,
                   form=form,
                   leaguename=leaguename,
                   welcometext=welcometext)

    dbcur.close()
    conn.close()

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
    conn = connect_db()
    dbcur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # Get the current league season (whether started or not)
    dbcur.execute("select sid, timestamp, seasonlength, numtodrop, numofrounds, gamesperround, scoring, seeding, playerorder, machinedrawing, dues, running, historical, active from season where historical=false order by timestamp limit 1")
    currentSeason = dbcur.fetchall()

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

    for entry in currentSeason:
        sid = entry['sid']
        length = entry['seasonlength']
        dropweeks = entry['numtodrop']
        numrounds = entry['numofrounds']
        numgames = entry['gamesperround']
        scoring = entry['scoring']
        seeding = entry['seeding']
        order = entry['playerorder']
        drawing = entry['machinedrawing']
        dues = entry['dues']
        running = entry['running']

    # Get historical league seasons
    dbcur.execute("select sid, timestamp, seasonLength, numToDrop, numOfRounds, gamesPerRound, scoring, seeding, playerOrder, machineDrawing, dues, running, historical, active from season where historical=true order by timestamp")

    historicalSeasons = dbcur.fetchall()

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

                dbcur.execute("insert into season (seasonlength, numtodrop, numofrounds, gamesperround, scoring, seeding, playerorder, machinedrawing, dues) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (seasonLength, dropWeeks, numRounds, numGames, scoring, seeding, playorder, drawing, dues))
                conn.commit()

                flash("New season added!")
            # Update existing season record (if not started)
            elif sid > 0 and not running:

                dbcur = conn.cursor()
                dbcur.execute("update season set seasonlength=%s, numtodrop=%s, numofrounds=%s, gamesperround=%s, scoring=%s, seeding=%s, playerorder=%s, machinedrawing=%s, dues=%s where sid=%s", (seasonLength, dropWeeks, numRounds, numGames, scoring, seeding, playorder, drawing, dues, sid))
                conn.commit()

                flash("Season updated!")

            # If the season has started
            else:
                flash("A season that is currently running canot be modified!")

            dbcur.close()
            conn.close()

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
            
            dbcur.close()
            conn.close()

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

    conn = connect_db()
    dbcur = conn.cursor()
    dbcur.execute("update season set active=%s where sid=%s", (activevalue, sid))
    conn.commit()
    dbcur.close()
    conn.close()
    return jsonify(ret=0)

@admin.route('/admin/data')
def show_admin_data():
    return render_template('show_admin_data.html', title="Admin - Export Data", highlightActive='export')
