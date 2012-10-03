drop table if exists player;
create table player (
  pid SERIAL primary key not null,
  nick varchar(255) not null,
  name varchar(255),
  email varchar(255),
  phone varchar(25),
  notes text,
  status integer
);

drop table if exists game;
create table game (
  gid SERIAL primary key not null,
  lid integer,
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
  notes text,
  active boolean
);

insert into player (nick, name, email, phone, notes, status) values ('rdare', 'Russell Dare', 'rdare3@gmail.com', '(301)345-2345', 'Awesome guy!', 1);
insert into player (nick, name, email, phone, notes, status) values ('samsam', 'samsonite', 'sam@tortugas.com', '', 'Some T', 1);
insert into player (nick, name, email, phone, notes, status) values ('sliceoflife', 'Dexter Morgan', 'dexter@aol.com', '(716)345-2345', 'Meh', 2);

insert into location (lid, name, address, notes, active) values (1, 'Russells house', '123 any street', 'Awesome place for a beer', True);
insert into location (lid, name, address, notes, active) values (2, 'Pizza Depot', 'Use Apple Maps heh', 'OK', True);
insert into location (lid, name, address, notes, active) values (3, 'Magic Pins', 'Springs Ave', 'Meh', False);

insert into game (lid, name, condition, notes, active) values (1, 'TOM', 'Amazing', 'Still fun', True);
insert into game (lid, name, condition, notes, active) values (1, 'TZ', 'Meh', 'Broken slingshots', True);
insert into game (lid, name, condition, notes, active) values (2, 'AFM', 'OK', 'Getting shopped', False);
insert into game (lid, name, condition, notes, active) values (2, 'Hurricane', 'Best Evar', 'Sweet', True);
insert into game (lid, name, condition, notes, active) values (3, 'RFM', 'OK', 'OK', True);
insert into game (lid, name, condition, notes, active) values (3, 'TAF', 'horrible', 'random resets', False);

