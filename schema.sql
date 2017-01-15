drop table if exists player;
create table player (
  pid SERIAL primary key not null,
  nick varchar(255),
  name varchar(255),
  email varchar(255),
  phone varchar(25),
  location varchar(255),
  ifpanumber integer,
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

-- Tables to hold historic data (lazy sharding)
--drop table if exists history;
--crate table history (

--);

--drop table if exists historic_scores;
--create table historic_scores (

--);
---------------------------------------------------------
---------------------------------------------------------


insert into location (lid, name, address, notes, active) values (1, 'Russells house', '123 any street', 'Awesome place for a beer', True);
insert into location (lid, name, address, notes, active) values (2, 'Pizza Depot', 'Use Apple Maps heh', 'OK', True);
insert into location (lid, name, address, notes, active) values (3, 'Magic Pins', 'Springs Ave', 'Meh', False);

insert into game (lid, name, condition, notes, active) values (1, 'TOM', 'Amazing', 'Still fun', True);
insert into game (lid, name, condition, notes, active) values (1, 'TZ', 'Meh', 'Broken slingshots', True);
insert into game (lid, name, condition, notes, active) values (2, 'AFM', 'OK', 'Getting shopped', False);
insert into game (lid, name, condition, notes, active) values (2, 'Hurricane', 'Best Evar', 'Sweet', True);
insert into game (lid, name, condition, notes, active) values (3, 'RFM', 'OK', 'OK', True);
insert into game (lid, name, condition, notes, active) values (3, 'TAF', 'horrible', 'random resets', False);

