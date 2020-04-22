import psycopg2
import psycopg2.extras
from flask import Flask, Blueprint, jsonify, request, session, g, redirect, abort, flash

from silverball import player
from silverball import admin

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

    except psycopg2.Error as e:
        print("I am unable to connect to the database: {}".format(e.pgerror))


if __name__ == '__main__':
    app.run(debug=app.config["DEBUG"])
