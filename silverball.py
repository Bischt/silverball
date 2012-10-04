########################
# config.ini
########################
# Imports
import psycopg2
import psycopg2.extras
from flask import Flask, jsonify, request, session, g, redirect, url_for, abort, render_template, flash
from flaskext.openid import OpenID

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Configuration
DB_HOST = 'localhost'
DB_NAME = 'silverball'
DB_USER = 'dwai'
DB_PASS = 'silverball'

########################
########################

app = Flask(__name__)
app.config.from_object(__name__)

# Debugging.  Turn this off when done!
app.debug = True

# Config for OpenID
app.config.update(
  DATABASE_URI = 'sqlite:////tmp/flask-openid.db',
  SECRET_KEY = 'H383QRf63oDYz8jvIFX64x63',
)

# Connect to database
def connect_db():
  try:
    return psycopg2.connect("dbname='silverball' user='dwai' host='localhost' password='silverball'")
    print "DB connection successful!"
  except:
    print "I am unable to connect to the database"
    exit(1)

# Initialize database
def init_db():
  print "Initializing database..."
  
  conn = connect_db()
  dbcur = conn.cursor()

  try:
    procedures = open('schema.sql','r').read()
    dbcur.execute(procedures)
    dbcur.execute("COMMIT")
    print "Database schema initialized!"
  except psycopg2.DatabaseError, e:
    print
    print "EXCEPTION: procedures :%s" % str(e)
    print
    exit(1)

@app.route('/')
def show_home():
  return render_template('show_home.html', title="Home", highlightActive='home')

@app.route('/admin')
def show_admin():
  return render_template('show_admin.html', title="Admin")

@app.route('/players')
def show_players():
  conn = connect_db()
  dbcur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
  dbcur.execute("select pid, nick, name, email, phone, location, pinside, notes, status from player where active=True;")
  entries = dbcur.fetchall()
  dbcur.close()
  conn.close()
  return render_template('show_players.html', title='Players', highlightActive='players', entries=entries)

@app.route('/players/<username>')
def show_player_by_name(username):
	# Show the user profile for the specific name provided
	conn = connect_db()
	dbcur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
	SQL = "select pid, nick, name, phone, location, pinside, notes, status, active from player where active=True and nick=%s;"
	data = (username, )
	dbcur.execute(SQL, data)
	entries = dbcur.fetchall()
	dbcur.close()
	conn.close()
	t = '%s Player Profile' % username
	return render_template('show_specific_player.html', title=t, highlightActive='players', entries=entries)

@app.route('/_single_player_profile')
# Get all the details about a player from the database and return as JSON
def single_player_profile():
  pid = request.args.get('pid', 0, type=int)
  conn = connect_db()
  dbcur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
  SQL = "select pid, nick, name, phone, location, pinside, notes, status, active from player where active=True and pid=%s;"
  data = (pid, )
  dbcur.execute(SQL, data)
  entries = dbcur.fetchall()
  dbcur.close()
  conn.close()

  # Parse out results and compile into JSON
  for entry in entries:
    pid = entry['pid']
    nick = entry['nick']
    name = entry['name']
    phone = entry['phone']
    location = entry['location']
    pinside = entry['pinside']
    notes = entry['notes']
    status = entry['status']
    active = entry['active']

  return jsonify(pid=pid, nick=nick, name=name, phone=phone, location=location, pinside=pinside, notes=notes, status=status, active=active)

@app.route('/standings')
def show_standings():
  return render_template('show_standings.html', title='Standings', highlightActive='standings')

@app.route('/locations')
def show_locations():
  conn = connect_db()
  dbcur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
  dbcur.execute("select lid, name, address, notes, active from location where active=True;")
  entries = dbcur.fetchall()
  dbcur.close()
  conn.close()
  return render_template('show_locations.html', title='Locations', highlightActive='locations', entries=entries)

@app.route('/_single_location_info')
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

##########################################
# OPENID CONFIGURATION
##########################################

# Setup flask-openid
oid = OpenID(app, '/tmp')

# Setup sqlalchemy
engine = create_engine(app.config['DATABASE_URI'])
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

# Initialize SQLite DB
def init_auth_db():
  Base.metadata.create_all(bind=engine)

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  name = Column(String(60))
  email = Column(String(200))
  openid = Column(String(200))

  def __init__(self, name, email, openid):
    self.name = name
    self.email = email
    self.openid = openid

@app.before_request
def before_request():
  g.user = None
  if 'openid' in session:
    g.user = User.query.filter_by(openid=session['openid']).first()

@app.after_request
def after_request(response):
  db_session.remove()
  return response

@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
  # Processes the login.  Will call oid.try_login to start OpenID
  # If we are already logged in, go back to where we came from
  if g.user is not None:
    return redirect(oid.get_next_url())
  if request.method == 'POST':
    openid = request.form.get('openid')
    if openid:
      return oid.try_login(openid, ask_for=['email', 'fullname', 'nickname'])
  
  return render_template('login.html', title='Login', next=oid.get_next_url(),
                         error=oid.fetch_error())

@oid.after_login
def create_or_login(resp):
  """This is called when login with OpenID succeeded and it's not
  necessary to figure out if this is the users's first login or not.
  This function has to redirect otherwise the user will be presented
  with a terrible URL which we certainly don't want.
  """
  session['openid'] = resp.identity_url
  user = User.query.filter_by(openid=resp.identity_url).first()
  if user is not None:
    flash(u'Successfully signed in')
    g.user = user
    return redirect(oid.get_next_url())
  return redirect(url_for('create_profile', next=oid.get_next_url(),
                            name=resp.fullname or resp.nickname,
                            email=resp.email))

@app.route('/create-profile', methods=['GET', 'POST'])
def create_profile():
  """If this is the user's first login, the create_or_login function
  will redirect here so that the user can set up his profile.
  """
  if g.user is not None or 'openid' not in session:
    return redirect(url_for('index'))
  if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    if not name:
      flash(u'Error: you have to provide a name')
    elif '@' not in email:
      flash(u'Error: you have to enter a valid email address')
    else:
      flash(u'Profile successfully created')
      db_session.add(User(name, email, session['openid']))
      db_session.commit()
      return redirect(oid.get_next_url())
  return render_template('create_profile.html', title='Create Profile', next_url=oid.get_next_url())


@app.route('/profile', methods=['GET', 'POST'])
def edit_profile():
  """Updates a profile"""
  if g.user is None:
    abort(401)
  form = dict(name=g.user.name, email=g.user.email)
  if request.method == 'POST':
    if 'delete' in request.form:
      db_session.delete(g.user)
      db_session.commit()
      session['openid'] = None
      flash(u'Profile deleted')
      return redirect(url_for('index'))
    form['name'] = request.form['name']
    form['email'] = request.form['email']
    if not form['name']:
      flash(u'Error: you have to provide a name')
    elif '@' not in form['email']:
      flash(u'Error: you have to enter a valid email address')
    else:
      flash(u'Profile successfully created')
      g.user.name = form['name']
      g.user.email = form['email']
      db_session.commit()
      return redirect(url_for('edit_profile'))
  return render_template('edit_profile.html', title='Profile', form=form)


@app.route('/logout')
def logout():
  session.pop('openid', None)
  flash(u'You have been signed out')
  return redirect(oid.get_next_url())

##########################################
##########################################

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
