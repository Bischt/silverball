DEBUG = False  # Turns on debugging features in flask

DB_HOST = "localhost"  # Host where the database server will be running
DB_NAME = "silverball"  # The name of the database

PLAYFIELD_API_HOST = "host.docker.internal"  # The host running the Playfield API
PLAYFIELD_API_PORT = "8080"  # The port exposed for the Playfield API service

########################################################################
# SECRET CREDENTIALS
# Copy these variables to instance/config.py and customize them
########################################################################

DB_USER = "APP_SPECIFIC_USER"  # Database username
DB_PASS = "STRONG_PASSWORD"  # Database password

IFPA_API_KEY = "abc123yourkey"  # API Key for IFPA

SECRET_KEY = '0f81ff42be11b667fba040babd646e3b42306b3e'  # Secret to be used for CSRF protection
