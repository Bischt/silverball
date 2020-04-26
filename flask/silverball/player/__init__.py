import json
import requests
from flask import Flask, Blueprint, jsonify, request, session, g, redirect, url_for, abort, render_template, flash, \
    current_app

from ..backend import PlayfieldAPI

app = Flask(__name__)

player = Blueprint('player', __name__, static_folder='../static', template_folder='../templates')

playfield = PlayfieldAPI("host.docker.internal", "8080")


@player.route('/')
def show_home():
    return render_template('show_home.html', title="Home", highlightActive='home')


@player.route('/_update_player_status')
# Update the player's status.  Status specified whether or not the player has paid.
def update_player_status():
    player_id = request.args.get('player_id', 0, type=str)
    newStatus = request.args.get('newStatus', 0, type=int)
    if newStatus == 1:
        statusvalue = 1
    elif newStatus == 0:
        statusvalue = 0
    else:
        statusvalue = 0

    data = (player_id, str(statusvalue),)
    retval = playfield.api_request("get", "player", "set_status", data)

    return jsonify(ret=0)


@player.route('/_update_player_activity')
# Update the player's activity status.  Inactive players cannot log in and will not show up as players.
def update_player_activity():
    player_id = request.args.get('player_id', 0, type=str)
    active = request.args.get('active', 0, type=int)
    if active == 1:
        activevalue = True
    elif active == 0:
        activevalue = False
    else:
        activevalue = False

    data = (player_id, str(activevalue),)
    retval = playfield.api_request("get", "player", "set_active", data)

    return jsonify(ret=0)


@player.route('/_update_location_status')
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


@player.route('/players')
def show_players():
    # Query api for active players
    player_json = playfield.api_request("get", "player", "active_players", None)

    # If error querying API flash message to user
    if player_json is not "Error" and player_json is not None:
        entries = playfield.parse_json(player_json)
    else:
        flash("Problem accessing Playfield API")
        entries = {}

    return render_template('show_players.html', title='Players', highlightActive='players', entries=entries)


@player.route('/players/<player_id>')
def show_player_by_name(player_id):
    # Show the user profile for the specific name provided
    player_json = playfield.api_request("get", "player", "player_by_id", player_id)

    # If error querying API flash message to user
    if player_json is not "Error" and player_json is not None:
        entries = playfield.parse_json(player_json)
    else:
        flash("Problem accessing Playfield API")
        entries = {}

    for single_player in entries:
        t = '%s Player Profile' % single_player["name"]
    return render_template('show_specific_player.html', title=t, highlightActive='players', entries=entries)


@player.route('/_single_player_profile')
# Get all the details about a player from the database and return as JSON
def single_player_profile():
    pid = request.args.get('player_id', 0, type=str)

    player_json = playfield.api_request("get", "player", "player_by_id", pid)

    # If error querying API flash message to user
    if player_json is not "Error" and player_json is not None:
        entries = playfield.parse_json(player_json)
    else:
        flash("Problem accessing Playfield API")
        entries = {}

    # Parse out results and compile into JSON
    for entry in entries:
        pid = entry['player_id']
        nick = entry['nick']
        name = entry['name']
        phone = entry['phone']
        location = entry['location']
        ifpanumber = entry['ifpanumber']
        pinside = entry['pinside']
        notes = entry['notes']
        status = entry['status']
        active = entry['active']
        currentRank = entry['currentrank']
        currentWPPRValue = entry['currentwpprvalue']
        bestFinish = entry['bestfinish']
        activeEvents = entry['activeevents']

    # Make API call to IFPA to refresh stored player info if there is an ifpa number associated with the player
    statusCode = ""

    if ifpanumber != "":
        response = get_ifpa_player(ifpanumber)
        statusCode = response.status_code

        # If status code 200 update database with new cached data
    if statusCode == 200:
        ifpadata = json.loads(response.content)
        currentRank = ifpadata["player_stats"]["current_wppr_rank"]
        currentWPPRValue = ifpadata["player_stats"]["current_wppr_value"]
        bestFinish = ifpadata["player_stats"]["best_finish"]
        activeEvents = ifpadata["player_stats"]["total_active_events"]

        # TODO: Find way to cache ifpa data in a sane way

    return jsonify(pid=pid,
                   nick=nick,
                   name=name,
                   ifpanumber=ifpanumber,
                   phone=phone,
                   location=location,
                   pinside=pinside,
                   notes=notes,
                   status=status,
                   active=active,
                   statuscode=statusCode,
                   currentrank=currentRank,
                   currentwpprvalue=currentWPPRValue,
                   bestfinish=bestFinish,
                   activeevents=activeEvents)


@player.route('/standings')
def show_standings():
    return render_template('show_standings.html', title='Standings', highlightActive='standings')


@player.route('/checkin')
def show_checkin():
    return render_template('show_checkin.html', title='Check In', highlightActive='checkin')


@player.route('/scores')
def show_scores():
    return render_template('show_scores.html', title='Scores', highlightActive='scores')


@player.route('/locations')
def show_locations():
    location_json = playfield.api_request("get", "location", "playable_locations", None)

    # If error querying API flash message to user
    if location_json is not "Error" and location_json is not None:
        entries = playfield.parse_json(location_json)
    else:
        flash("Problem accessing Playfield API")
        entries = {}

    return render_template('show_locations.html',
                           title='Locations',
                           highlightActive='locations',
                           entries=entries)


@player.route('/_single_location_info')
def single_location_info():
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
        lid = entry['location_id']
        name = entry['name']
        address = entry['address']
        notes = entry['notes']
        active = entry['active']

        return jsonify(lid=lid, name=name, address=address, notes=notes, active=active)


@player.route('/_games_for_location')
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


# Will query the IFPA api and return a json blob about a particular user
def get_ifpa_player(playerNum):
    ifpa_api_url = "https://api.ifpapinball.com/v1/player/%s?api_key=%s" % (
    playerNum, current_app.config["IFPA_API_KEY"])

    response = requests.get(ifpa_api_url)

    # response.content = JSON blob
    # response.status_code = Status code

    return response
