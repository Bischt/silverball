import sys
import psycopg2
import psycopg2.extras
from flask import Flask, Blueprint, jsonify, request, session, g, redirect, abort, flash
#from flask_openid import OpenID

from silverball import player
from silverball import admin

# Ensure we are using utf8 so we don't get odd encoding problems
#reload(sys)
#sys.setdefaultencoding('utf8')

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py', silent=True)

app.register_blueprint(player.player)
app.register_blueprint(admin.admin)

# Debugging.  Turn this off when done!
app.debug = app.config["DEBUG"]


# Connect to database
def connect_db():
    try:
        conn_string = "dbname=%s user=%s host=%s password=%s" % (app.config["DB_NAME"],
                                                                 app.config["DB_USER"],
                                                                 app.config["DB_HOST"],
                                                                 app.config["DB_PASS"])
        return psycopg2.connect(conn_string)
        print("DB connection successful!")
    except:
        print("I am unable to connect to the database")
        exit(1)


# Initialize database
#def init_db():
#    print("Initializing database...")

#    conn = connect_db()
#    dbcur = conn.cursor()

#    try:
#        procedures = open('schema.sql', 'r').read()
#        dbcur.execute(procedures)
#        dbcur.execute("COMMIT")
#        print("Database schema initialized!")
#    except psycopg2.DatabaseError, e:
#        print("\nEXCEPTION: procedures :{}\n".format(str(e)))
#        exit(1)


if __name__ == '__main__':
    app.run(debug=app.config["DEBUG"])
