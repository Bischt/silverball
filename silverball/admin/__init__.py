import psycopg2
import psycopg2.extras
from flask import Flask, Blueprint, jsonify, request, session, g, redirect, url_for, abort, render_template, flash, current_app
from flask_openid import OpenID

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app=Flask(__name__)

admin = Blueprint('admin', __name__, static_url_path='/admin', static_folder='../static', template_folder='../templates')

# Connect to database
def connect_db():
    try:
        conn_string = "dbname=%s user=%s host=%s password=%s" % (current_app.config["DB_NAME"], 
                                                                 current_app.config["DB_USER"], 
                                                                 current_app.config["DB_HOST"], 
                                                                 current_app.config["DB_PASS"])
        return psycopg2.connect(conn_string)
        print "DB connection successful!"
    except:
        print "I am unable to connect to the database"
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
    return render_template('show_admin.html', title="Admin - Run League", highlightActive='runleague', 
                           entries=entries, locations=locations)

@admin.route('/admin/players')
def show_admin_players():
    conn = connect_db()
    dbcur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    dbcur.execute("select pid, nick, name, email, phone, location, ifpanumber, pinside, notes, status, active from player order by active")
    playerEntries = dbcur.fetchall()
    dbcur.close()
    conn.close()
    return render_template('show_admin_players.html', title="Admin - Manage Players", highlightActive='players', 
                           entries=playerEntries)

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

    return jsonify(pid=pid, nick=nick, name=name, phone=phone, email=email, location=location, ifpanumber=ifpanumber,
                   pinside=pinside, notes=notes, status=status, active=active)

@admin.route('/admin/locations')
def show_admin_locations():
    return render_template('show_admin_locations.html', title="Admin - Manage Locations", highlightActive='locations')

@admin.route('/admin/content')
def show_admin_content():
    return render_template('show_admin_content.html', title="Admin - Edit Content", highlightActive='content')

@admin.route('/admin/config')
def show_admin_config():
    return render_template('show_admin_config.html', title="Admin - Configure League", highlightActive='configure')

@admin.route('/admin/data')
def show_admin_data():
    return render_template('show_admin_data.html', title="Admin - Export Data", highlightActive='export')
