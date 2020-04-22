drop table if exists player;
create table player (
  pid SERIAL primary key not null,
  nick varchar(255),
  name varchar(255),
  email varchar(255),
  phone varchar(25),
  location varchar(255),
  ifpanumber varchar(10),
  pinside varchar(30),
  notes text,
  status integer,
  active boolean not null,
  currentrank integer,
  currentwpprvalue double precision,
  bestfinish integer,
  activeevents integer
);

drop table if exists game;
create table game (
  gid SERIAL primary key not null,
  lid integer,
  mid integer,
  name varchar(255) not null,
  condition text,
  notes text,
  active boolean
);

drop table if exists location;
create table location (
  lid SERIAL primary key not null,
  name varchar(255) not null,
  address varchar(255),
  addressPrivate boolean,
  notes text,
  locType integer,
  active boolean
);

drop table if exists machines;
create table machines (
  mid SERIAL primary key not null,
  name varchar(255) not null,
  abbr varchar(50),
  manufacturer varchar(150),
  manDate varchar(100),
  players varchar(2),
  gameType varchar(5),
  theme varchar(150),
  ipdbURL varchar(150)
);

drop table if exists season;
create table season (
  sid SERIAL primary key not null,
  timestamp timestamp not null default CURRENT_TIMESTAMP,
  seasonLength integer not null,
  numToDrop integer not null,
  numOfRounds integer not null,
  gamesPerRound integer not null, 
  scoring varchar(150) not null,
  seeding varchar(150) not null,
  playerOrder varchar(150) not null,
  machineDrawing varchar(150) not null,
  dues double precision default 0.00,
  running boolean not null default False,
  historical boolean not null default False,
  active boolean not null default True
);

drop table if exists config;
create table config (
  cid integer primary key not null,
  leagueName varchar(255),
  welcomeText text
);
insert into config (cid, leagueName, welcomeText) values (1, '', '');

drop table if exists posts;
create table posts (
  pid SERIAL primary key not null,
  timestamp timestamp not null default CURRENT_TIMESTAMP,
  title varchar(255) not null,
  content text not null,
  active boolean not null default True
);

---------------------------------------------------------
-- Test tables for league scoring/team matching/voting --
---------------------------------------------------------
drop table if exists sessions;
create table sessions (
  season_id integer primary key not null,
  session_id integer not null,
  lid integer
  
);

drop table if exists scores;
create table scores (
  score_id SERIAL primary key not null,
  session_id integer,
  pid integer,
  gid integer,
  score bigint
);

drop table if exists teams;
create table teams (
  t_id integer,
  pid integer
);

drop table if exists voting;
create table voting ( 
  gid integer,
  pid integer,
  vote boolean
);

