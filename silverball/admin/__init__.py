import psycopg2
import psycopg2.extras
from flask import Flask, Blueprint, jsonify, request, session, g, redirect, url_for, abort, render_template, flash, current_app
from flask_openid import OpenID

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app=Flask(__name__)
with app.app_context():
  current_app.config.from_object('config')

admin = Blueprint('admin', __name__, static_url_path='/admin', static_folder='../static', template_folder='../templates')

# Connect to database
def connect_db():
  try:
    conn_string = "dbname=%s user=%s host=%s password=%s" % (app.config["DB_NAME"], app.config["DB_USER"], app.config["DB_HOST"], app.config["DB_PASS"])
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
  return render_template('show_admin.html', title="Admin - Run League", highlightActive='runleague', entries=entries, locations=locations)

@admin.route('/admin/players')
def show_admin_players():
  return render_template('show_admin_players.html', title="Admin - Manage Players", highlightActive='players')

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
