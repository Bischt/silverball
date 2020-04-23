silverball
==========

Description:
------------
App to organize pinball leagues.  Track standings, manage league night check in, track scores, 
manage players, league play locations, schedules/notifications, and admin league details.

Currently this is a high level design document.  As features get fleshed out and completed it 
should probably be updated to reflect more of reality and less of a dream.

Features
--------

**Standings** *(/standings)*

* Show season scores
* View past season scores

**Check-In** *(/checkin)*

* Player confirmation that they are attending league night
* Will be placed in groups for play only if checked in
* Can be locked out if dues not paid (admin override possible)

**Scores** *(/scores)*

* Player (and/or admin) reporting of scores for the active league night

**Players** *(/players)*

* Show player info: nickname, name, contact info, league status, scores
* Jump to specific player with /players/PLAYERID

**Venues** *(/locations)*

* Locations the league plays: names, locations, pins associated with venue
* Pinball machines can be deactivated by admin to remove from league play
* View specific location with /locations/LOCATIONNAME

**Log In** *(/login)*

* Log in using OpenID
* Can edit some user specific info
* Required for user specific actions (score entering, check-in, admin access if enabled)

**Administration** *(/admin)*

* Run League Night *(/admin/runleague)*
  * Start/restart league night
  * Close league night
  * Manual score input
  * Machine/group assignment

* Manage Players *(/admin/players)*
  * Edit player info
  * Add/delete players
  * Toggle whether or not player dues have been paid
  * View historical payment data
  * Can lockout players from checking in if not paid up (and can override on a per night basis)

* Manage Locations *(/admin/locations)*
  * Edit location info
  * Add/delete locations
  * Associate games with locations
  * Toggle active/inactive on each game to withhold from league

* Edit Content *(/admin/content)*
  * Edit welcome text
  * Edit calendar (calendar display settings, i.e. from Facebook, Google Calendar, etc)
  * Make/edit blog post
  * Toggle authentication
  * Update league logo

* Configure League *(/admin/config)*
  * Length of season
  * Number of games played per session
  * Scoring rules/values
  * Number of nights required to quality/receive WPPR points
  * Number of low scores to drop
  * Seeding
  * Rolling groups
  * Game selection
  * League dues

* Export Data *(/admin/data)*
  * Export league standings in IFPA formatted csv
  * Ability to dump league data in other formats
  * Ability to import historical league data?
  * API

Run Locally:
------------
1.  cd to flask directory
2.  `export FLASK_APP=run.py`
    `export FLASK_ENV=development`
3.  Run the app: `flask run`
4.  In browser go to: `http://127.0.0.1:5000/`

Run via Docker:
--------------
1.  In directory with docker-compose.yml: `docker-compose build`
2.  Create & start containers: `docker-compose up`
3.  In browser go to: `http://127.0.0.1`

Shortcut: `docker-compose up --build`