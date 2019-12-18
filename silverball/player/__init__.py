import json
import psycopg2
import psycopg2.extras
import requests
from flask import Flask, Blueprint, jsonify, request, session, g, redirect, url_for, abort, render_template, flash, current_app
from flask_openid import OpenID

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


app=Flask(__name__)

player = Blueprint('player', __name__, static_folder='../static', template_folder='../templates')

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

@player.route('/')
def show_home():
    return render_template('show_home.html', title="Home", highlightActive='home')

@player.route('/_update_player_status')
# Update the player's status.  Status specified whether or not the player has paid.
def update_player_status():
    pid = request.args.get('pid', 0, type=int)
    newStatus = request.args.get('newStatus', 0, type=int)
    if newStatus == 1:
        statusvalue = 1
    elif newStatus == 0:
        statusvalue = 0
    else:
        statusvalue = 0

    conn = connect_db()
    dbcur = conn.cursor()
    dbcur.execute("update player set status=%s where pid=%s", (statusvalue, pid))
    conn.commit()
    dbcur.close()
    conn.close()
    return jsonify(ret=0)

@player.route('/_update_player_activity')
# Update the player's activity status.  Inactive players cannot log in and will not show up as players.
def update_player_activity():
    pid = request.args.get('pid', 0, type=int)
    active = request.args.get('active', 0, type=int)
    if active == 1:
        activevalue = True
    elif active == 0:
        activevalue = False
    else:
        activevalue = False

    conn = connect_db()
    dbcur = conn.cursor()
    dbcur.execute("update player set active=%s where pid=%s", (activevalue, pid))
    conn.commit()
    dbcur.close()
    conn.close()
    return jsonify(ret=0)

@player.route('/_update_location_status')
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

@player.route('/players')
def show_players():
    conn = connect_db()
    dbcur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    dbcur.execute("select pid, nick, name, email, phone, location, ifpanumber, pinside, notes, status from player where active=True;")
    entries = dbcur.fetchall()
    dbcur.close()
    conn.close()
    return render_template('show_players.html', title='Players', highlightActive='players', entries=entries)

@player.route('/players/<username>')
def show_player_by_name(username):
    # Show the user profile for the specific name provided
    conn = connect_db()
    dbcur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    SQL = "select pid, nick, name, email, phone, location, ifpanumber, pinside, notes, status, active from player where active=True and nick=%s;"
    data = (username, )
    dbcur.execute(SQL, data)
    entries = dbcur.fetchall()
    dbcur.close()
    conn.close()
    t = '%s Player Profile' % username
    return render_template('show_specific_player.html', title=t, highlightActive='players', entries=entries)

@player.route('/_single_player_profile')
# Get all the details about a player from the database and return as JSON
def single_player_profile():
    pid = request.args.get('pid', 0, type=int)
    conn = connect_db()
    dbcur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    SQL = "select pid, nick, name, phone, location, ifpanumber, pinside, notes, status, active, currentrank, currentwpprvalue, bestfinish, activeevents from player where active=True and pid=%s;"
    data = (pid, )
    dbcur.execute(SQL, data)
    entries = dbcur.fetchall()

    # Parse out results and compile into JSON
    for entry in entries:
        pid = entry['pid']
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
        activeEvents = entry ['activeevents']

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

            dbcur.execute("update player set currentrank=%s, currentwpprvalue=%s, bestfinish=%s, activeevents=%s  where pid=%s", (
                         currentRank, currentWPPRValue, bestFinish, activeEvents, pid))
            conn.commit()

    dbcur.close()
    conn.close()

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
    conn = connect_db()
    dbcur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    dbcur.execute("select location.lid, location.name, location.address, location.notes, count(*) as gamecount from location inner join game on location.lid=game.lid where location.active=true and game.active=true group by location.lid;")
    entries = dbcur.fetchall()
    dbcur.close()
    conn.close()
    return render_template('show_locations.html', 
           title='Locations', 
           highlightActive='locations', 
           entries=entries)

@player.route('/_single_location_info')
def single_location_info():
    lid = request.args.get('lid', 0, type=int)
    conn = connect_db()
    dbcur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    SQL = "select lid, name, address, notes, active from location where active=True and lid=%s;"
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

@player.route('/_games_for_location')
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

# Will query the IFPA api and return a json blob about a particular user
def get_ifpa_player(playerNum):
    ifpa_api_url = "https://api.ifpapinball.com/v1/player/%s?api_key=%s" % (playerNum, current_app.config["IFPA_API_KEY"])

    response = requests.get(ifpa_api_url)

    # response.content = JSON blob
    # response.status_code = Status code

    return response
