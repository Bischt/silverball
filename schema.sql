drop table if exists player;
create table player (
  pid SERIAL primary key not null,
  nick varchar(255),
  name varchar(255),
  email varchar(255),
  phone varchar(25),
  location varchar(255),
  ifpaNumber integer,
  pinside varchar(30),
  notes text,
  status integer,
  active boolean not null
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

insert into player (nick, name, email, phone, location, pinside, notes, status, active) values ('rdare', 'Russell Dare', 'rdare3@gmail.com', '(301)345-2345', 'San Jose, CA', 'Bischt', 'Awesome guy!', 1, True);
insert into player (nick, name, email, phone, location, pinside, notes, status, active) values ('samsam', 'samsonite', 'sam@tortugas.com', '', 'Fresno, CA', '', 'Some T', 1, True);
insert into player (nick, name, email, phone, location, pinside, notes, status, active) values ('sliceoflife', 'Dexter Morgan', 'dexter@aol.com', '(716)345-2345', 'Sunnyvale, CA', '', 'Meh', 0, False);

insert into location (lid, name, address, notes, active) values (1, 'Russells house', '123 any street', 'Awesome place for a beer', True);
insert into location (lid, name, address, notes, active) values (2, 'Pizza Depot', 'Use Apple Maps heh', 'OK', True);
insert into location (lid, name, address, notes, active) values (3, 'Magic Pins', 'Springs Ave', 'Meh', False);

insert into game (lid, name, condition, notes, active) values (1, 'TOM', 'Amazing', 'Still fun', True);
insert into game (lid, name, condition, notes, active) values (1, 'TZ', 'Meh', 'Broken slingshots', True);
insert into game (lid, name, condition, notes, active) values (2, 'AFM', 'OK', 'Getting shopped', False);
insert into game (lid, name, condition, notes, active) values (2, 'Hurricane', 'Best Evar', 'Sweet', True);
insert into game (lid, name, condition, notes, active) values (3, 'RFM', 'OK', 'OK', True);
insert into game (lid, name, condition, notes, active) values (3, 'TAF', 'horrible', 'random resets', False);


--
-- Auto generated data
--
 INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Hoyt','Fritz Clark','scelerisque.lorem.ipsum@risus.com','(608) 488-5887','OR','Joshua','sem, vitae aliquam eros turpis non enim. Mauris quis turpis vitae purus gravida sagittis. Duis gravida. Praesent eu nulla at sem molestie sodales. Mauris blandit enim consequat purus. Maecenas libero','0','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Griffith','Buckminster Rogers','malesuada@Nunc.com','(659) 110-9487','ON','Elliott','augue scelerisque mollis. Phasellus libero mauris, aliquam eu, accumsan sed, facilisis vitae, orci. Phasellus dapibus quam quis diam. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis','1','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Kibo','Tobias Emerson','Pellentesque.tincidunt.tempus@consectetuermauris.com','(977) 442-3533','ID','Sydnee','elit fermentum risus, at fringilla purus mauris a nunc. In at pede. Cras vulputate velit eu sem. Pellentesque ut ipsum ac mi eleifend egestas. Sed pharetra, felis eget varius ultrices,','1','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Branden','Malik Morton','molestie.in.tempus@diamluctus.edu','(866) 364-9081','OR','Harlan','dolor dapibus gravida. Aliquam tincidunt, nunc ac mattis ornare, lectus ante dictum mi, ac mattis velit justo nec ante. Maecenas mi felis, adipiscing fringilla, porttitor vulputate, posuere vulputate, lacus. Cras','0','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Rudyard','Vincent Solis','facilisis.vitae.orci@Maecenasiaculis.edu','(793) 879-4969','Ontario','Dana','ornare placerat, orci lacus vestibulum lorem, sit amet ultricies sem magna nec quam. Curabitur vel lectus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec dignissim','1','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Aquila','Nehru Dickerson','gravida@purus.edu','(366) 345-5125','NB','Shaeleigh','leo. Cras vehicula aliquet libero. Integer in magna. Phasellus dolor elit, pellentesque a, facilisis non, bibendum sed, est. Nunc laoreet lectus quis massa. Mauris vestibulum, neque sed dictum eleifend, nunc','0','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('McKenzie','Alexander Morse','Quisque.nonummy.ipsum@ullamcorperDuis.com','(815) 242-7762','Vermont','Richard','nisi a odio semper cursus. Integer mollis. Integer tincidunt aliquam arcu. Aliquam ultrices iaculis odio. Nam interdum enim non nisi. Aenean eget metus. In nec orci. Donec nibh. Quisque nonummy','0','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Uma','Josiah Hamilton','vel.turpis.Aliquam@Donecfelis.ca','(589) 961-4867','South Dakota','Eleanor','pharetra. Quisque ac libero nec ligula consectetuer rhoncus. Nullam velit dui, semper et, lacinia vitae, sodales at, velit. Pellentesque ultricies dignissim lacus. Aliquam rutrum lorem ac risus. Morbi metus. Vivamus','1','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Cairo','Len Walls','Nullam@nuncsed.com','(797) 645-6328','New Jersey','Rebekah','a, malesuada id, erat. Etiam vestibulum massa rutrum magna. Cras convallis convallis dolor. Quisque tincidunt pede ac urna. Ut tincidunt vehicula risus. Nulla eget metus eu erat semper rutrum. Fusce','0','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Evan','Rafael Woodward','fringilla@Phasellusdapibus.edu','(256) 526-2808','NT','Chava','sodales elit erat vitae risus. Duis a mi fringilla mi lacinia mattis. Integer eu lacus. Quisque imperdiet, erat nonummy ultricies ornare, elit elit fermentum risus, at fringilla purus mauris a','1','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Lila','Uriel Estrada','dolor@tincidunt.com','(964) 179-7213','Kentucky','Thane','faucibus ut, nulla. Cras eu tellus eu augue porttitor interdum. Sed auctor odio a purus. Duis elementum, dui quis accumsan convallis, ante lectus convallis est, vitae sodales nisi magna sed','1','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Martena','Palmer Cabrera','rutrum.lorem@elit.com','(384) 680-0980','Alaska','Elliott','orci. Ut sagittis lobortis mauris. Suspendisse aliquet molestie tellus. Aenean egestas hendrerit neque. In ornare sagittis felis. Donec tempor, est ac mattis semper, dui lectus rutrum urna, nec luctus felis','1','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Hector','Harrison Schultz','Aliquam.ultrices@congueIn.org','(983) 311-7798','QC','Randall','vitae odio sagittis semper. Nam tempor diam dictum sapien. Aenean massa. Integer vitae nibh. Donec est mauris, rhoncus id, mollis nec, cursus a, enim. Suspendisse aliquet, sem ut cursus luctus,','1','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Iliana','Aladdin Harmon','in@loremvitaeodio.edu','(977) 565-7968','NT','Marcia','lacus. Mauris non dui nec urna suscipit nonummy. Fusce fermentum fermentum arcu. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Phasellus ornare. Fusce mollis. Duis','0','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Abigail','Elijah Norris','lacinia.Sed@Integereulacus.edu','(261) 258-9054','NS','Leila','ut, nulla. Cras eu tellus eu augue porttitor interdum. Sed auctor odio a purus. Duis elementum, dui quis accumsan convallis, ante lectus convallis est, vitae sodales nisi magna sed dui.','1','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Beck','Zachary Berger','auctor@nuncid.com','(262) 278-3832','Newfoundland and Labrador','Dorothy','neque vitae semper egestas, urna justo faucibus lectus, a sollicitudin orci sem eget massa. Suspendisse eleifend. Cras sed leo. Cras vehicula aliquet libero. Integer in magna. Phasellus dolor elit, pellentesque','1','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Zephr','Dale Durham','dui.semper.et@posuere.org','(334) 640-8686','ON','Ima','at, egestas a, scelerisque sed, sapien. Nunc pulvinar arcu et pede. Nunc sed orci lobortis augue scelerisque mollis. Phasellus libero mauris, aliquam eu, accumsan sed, facilisis vitae, orci. Phasellus dapibus','1','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Fay','Bruce Graves','sapien.Aenean.massa@egestasFusce.edu','(939) 552-0271','NL','Lunea','venenatis a, magna. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam laoreet, libero et tristique pellentesque, tellus sem mollis dui, in sodales elit erat vitae risus. Duis a mi','1','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Cooper','Melvin Sanford','nisl.elementum.purus@semutcursus.ca','(178) 171-0273','YT','Hilel','Mauris ut quam vel sapien imperdiet ornare. In faucibus. Morbi vehicula. Pellentesque tincidunt tempus risus. Donec egestas. Duis ac arcu. Nunc mauris. Morbi non sapien molestie orci tincidunt adipiscing. Mauris','1','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('TaShya','Jordan Hill','diam.Proin.dolor@dolor.org','(176) 984-7919','Illinois','Nadine','justo eu arcu. Morbi sit amet massa. Quisque porttitor eros nec tellus. Nunc lectus pede, ultrices a, auctor non, feugiat nec, diam. Duis mi enim, condimentum eget, volutpat ornare, facilisis','1','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Nissim','Dane Holt','mollis.nec@nequeetnunc.edu','(708) 316-9044','Newfoundland and Labrador','Yardley','sit amet, dapibus id, blandit at, nisi. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Proin vel nisl. Quisque fringilla euismod enim. Etiam gravida molestie arcu.','1','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Clinton','Tyler Mcfadden','elit.pede.malesuada@liberonecligula.edu','(930) 100-9316','Oregon','Jasper','gravida nunc sed pede. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Proin vel arcu eu odio tristique pharetra. Quisque ac libero nec ligula consectetuer rhoncus.','1','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Eric','Drake Holcomb','nibh.enim.gravida@vehiculaet.com','(937) 130-1411','Arkansas','Kato','quis turpis vitae purus gravida sagittis. Duis gravida. Praesent eu nulla at sem molestie sodales. Mauris blandit enim consequat purus. Maecenas libero est, congue a, aliquet vel, vulputate eu, odio.','1','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Maggy','Roth Foley','tempor.diam@Aliquamerat.edu','(225) 519-2223','Prince Edward Island','Timon','Curabitur massa. Vestibulum accumsan neque et nunc. Quisque ornare tortor at risus. Nunc ac sem ut dolor dapibus gravida. Aliquam tincidunt, nunc ac mattis ornare, lectus ante dictum mi, ac','0','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Jack','Fuller Church','interdum.libero.dui@per.com','(283) 295-7576','Alberta','Leandra','elit, pretium et, rutrum non, hendrerit id, ante. Nunc mauris sapien, cursus in, hendrerit consectetuer, cursus et, magna. Praesent interdum ligula eu enim. Etiam imperdiet dictum magna. Ut tincidunt orci','0','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Joshua','Wesley Walls','eleifend@ligula.com','(336) 745-0646','AK','Gray','amet luctus vulputate, nisi sem semper erat, in consectetuer ipsum nunc id enim. Curabitur massa. Vestibulum accumsan neque et nunc. Quisque ornare tortor at risus. Nunc ac sem ut dolor','1','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Judith','Jack Shields','auctor@DuisgravidaPraesent.edu','(244) 678-2537','Yukon','Dean','magnis dis parturient montes, nascetur ridiculus mus. Proin vel nisl. Quisque fringilla euismod enim. Etiam gravida molestie arcu. Sed eu nibh vulputate mauris sagittis placerat. Cras dictum ultricies ligula. Nullam','0','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Tanisha','Eric Walter','aliquam.iaculis.lacus@eleifendnon.edu','(432) 656-0149','District of Columbia','Danielle','semper egestas, urna justo faucibus lectus, a sollicitudin orci sem eget massa. Suspendisse eleifend. Cras sed leo. Cras vehicula aliquet libero. Integer in magna. Phasellus dolor elit, pellentesque a, facilisis','1','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Melanie','Dustin Bartlett','turpis.Aliquam.adipiscing@Donecconsectetuer.ca','(204) 347-5031','CA','Meredith','et magnis dis parturient montes, nascetur ridiculus mus. Proin vel arcu eu odio tristique pharetra. Quisque ac libero nec ligula consectetuer rhoncus. Nullam velit dui, semper et, lacinia vitae, sodales','0','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Lane','Isaac Barker','enim@nislsem.ca','(564) 585-8106','British Columbia','Kirby','ac tellus. Suspendisse sed dolor. Fusce mi lorem, vehicula et, rutrum eu, ultrices sit amet, risus. Donec nibh enim, gravida sit amet, dapibus id, blandit at, nisi. Cum sociis natoque','0','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Cedric','Maxwell Lloyd','pellentesque.eget@sed.com','(286) 133-4810','Maine','Caldwell','bibendum sed, est. Nunc laoreet lectus quis massa. Mauris vestibulum, neque sed dictum eleifend, nunc risus varius orci, in consequat enim diam vel arcu. Curabitur ut odio vel est tempor','1','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Yuri','Dennis Raymond','interdum.Sed@ametconsectetuer.ca','(703) 211-8151','Newfoundland and Labrador','Lillian','orci. Ut semper pretium neque. Morbi quis urna. Nunc quis arcu vel quam dignissim pharetra. Nam ac nulla. In tincidunt congue turpis. In condimentum. Donec at arcu. Vestibulum ante ipsum','0','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Sophia','Steel Francis','et@pedeac.com','(142) 912-2244','Ontario','Fatima','nec, eleifend non, dapibus rutrum, justo. Praesent luctus. Curabitur egestas nunc sed libero. Proin sed turpis nec mauris blandit mattis. Cras eget nisi dictum augue malesuada malesuada. Integer id magna','0','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Camden','Nolan Rosales','Ut.tincidunt.orci@elitAliquam.ca','(559) 863-0553','IL','Kelsie','egestas rhoncus. Proin nisl sem, consequat nec, mollis vitae, posuere at, velit. Cras lorem lorem, luctus ut, pellentesque eget, dictum placerat, augue. Sed molestie. Sed id risus quis diam luctus','0','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Kuame','Murphy Stein','et.netus.et@nequeMorbi.org','(235) 181-9673','New Brunswick','Mara','Fusce dolor quam, elementum at, egestas a, scelerisque sed, sapien. Nunc pulvinar arcu et pede. Nunc sed orci lobortis augue scelerisque mollis. Phasellus libero mauris, aliquam eu, accumsan sed, facilisis','0','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Lareina','Kevin Odom','cursus.luctus@feugiatnec.edu','(397) 711-2103','Prince Edward Island','Gregory','amet massa. Quisque porttitor eros nec tellus. Nunc lectus pede, ultrices a, auctor non, feugiat nec, diam. Duis mi enim, condimentum eget, volutpat ornare, facilisis eget, ipsum. Donec sollicitudin adipiscing','1','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Vivien','Merritt Rojas','diam.luctus@gravidasagittis.org','(550) 679-3505','MB','Dane','diam. Duis mi enim, condimentum eget, volutpat ornare, facilisis eget, ipsum. Donec sollicitudin adipiscing ligula. Aenean gravida nunc sed pede. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur','1','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Montana','Benjamin Green','scelerisque@et.org','(326) 182-0499','Nova Scotia','Cally','ultricies ornare, elit elit fermentum risus, at fringilla purus mauris a nunc. In at pede. Cras vulputate velit eu sem. Pellentesque ut ipsum ac mi eleifend egestas. Sed pharetra, felis','1','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Anne','Solomon Estrada','rutrum.justo.Praesent@semperNam.org','(415) 948-6468','Massachusetts','Gareth','Vivamus nisi. Mauris nulla. Integer urna. Vivamus molestie dapibus ligula. Aliquam erat volutpat. Nulla dignissim. Maecenas ornare egestas ligula. Nullam feugiat placerat velit. Quisque varius. Nam porttitor scelerisque neque. Nullam','0','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Keefe','Yuli Daniels','at@arcu.ca','(669) 301-8067','MS','Kim','ornare, libero at auctor ullamcorper, nisl arcu iaculis enim, sit amet ornare lectus justo eu arcu. Morbi sit amet massa. Quisque porttitor eros nec tellus. Nunc lectus pede, ultrices a,','1','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Mannix','Fulton Mccoy','sit@eunibh.ca','(661) 428-3594','Florida','Chantale','vel, faucibus id, libero. Donec consectetuer mauris id sapien. Cras dolor dolor, tempus non, lacinia at, iaculis quis, pede. Praesent eu dui. Cum sociis natoque penatibus et magnis dis parturient','0','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Chastity','Elton Ratliff','sed.hendrerit@Mauris.com','(178) 934-1869','ND','Rosalyn','facilisis lorem tristique aliquet. Phasellus fermentum convallis ligula. Donec luctus aliquet odio. Etiam ligula tortor, dictum eu, placerat eget, venenatis a, magna. Lorem ipsum dolor sit amet, consectetuer adipiscing elit.','1','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Xander','Ira Henderson','ultricies.sem.magna@purusinmolestie.com','(764) 962-7562','North Carolina','Basia','gravida molestie arcu. Sed eu nibh vulputate mauris sagittis placerat. Cras dictum ultricies ligula. Nullam enim. Sed nulla ante, iaculis nec, eleifend non, dapibus rutrum, justo. Praesent luctus. Curabitur egestas','0','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Gil','Benjamin Mccormick','tristique.senectus.et@sapien.ca','(782) 158-5547','MT','Signe','Maecenas ornare egestas ligula. Nullam feugiat placerat velit. Quisque varius. Nam porttitor scelerisque neque. Nullam nisl. Maecenas malesuada fringilla est. Mauris eu turpis. Nulla aliquet. Proin velit. Sed malesuada augue','0','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Jerome','Uriah Sanchez','non@nonummyultriciesornare.edu','(981) 760-0658','BC','Imani','ornare, facilisis eget, ipsum. Donec sollicitudin adipiscing ligula. Aenean gravida nunc sed pede. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Proin vel arcu eu odio','1','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Chandler','Erasmus Maddox','at.pede.Cras@tellusAenean.edu','(738) 837-9139','YT','Marvin','massa. Suspendisse eleifend. Cras sed leo. Cras vehicula aliquet libero. Integer in magna. Phasellus dolor elit, pellentesque a, facilisis non, bibendum sed, est. Nunc laoreet lectus quis massa. Mauris vestibulum,','0','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Shafira','Finn Ballard','ligula@temporarcu.edu','(206) 380-0647','Mississippi','Avram','urna et arcu imperdiet ullamcorper. Duis at lacus. Quisque purus sapien, gravida non, sollicitudin a, malesuada id, erat. Etiam vestibulum massa rutrum magna. Cras convallis convallis dolor. Quisque tincidunt pede','1','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Megan','Clark Diaz','aliquam.eu.accumsan@dictumeu.edu','(216) 436-0551','MD','Charissa','ultrices sit amet, risus. Donec nibh enim, gravida sit amet, dapibus id, blandit at, nisi. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Proin vel nisl.','0','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Lila','Bruno Phillips','mattis.Integer.eu@semperrutrumFusce.org','(963) 174-6183','Indiana','Abbot','malesuada fames ac turpis egestas. Aliquam fringilla cursus purus. Nullam scelerisque neque sed sem egestas blandit. Nam nulla magna, malesuada vel, convallis in, cursus et, eros. Proin ultrices. Duis volutpat','0','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Anastasia','Timon Rodgers','Fusce.mi.lorem@nequeMorbiquis.com','(763) 369-5670','Pennsylvania','Danielle','vel, faucibus id, libero. Donec consectetuer mauris id sapien. Cras dolor dolor, tempus non, lacinia at, iaculis quis, pede. Praesent eu dui. Cum sociis natoque penatibus et magnis dis parturient','0','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Mariko','Brian Meadows','nec@sempercursus.edu','(108) 375-6016','Saskatchewan','Craig','enim. Sed nulla ante, iaculis nec, eleifend non, dapibus rutrum, justo. Praesent luctus. Curabitur egestas nunc sed libero. Proin sed turpis nec mauris blandit mattis. Cras eget nisi dictum augue','1','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Raya','Lev Joseph','Mauris@tinciduntdui.org','(816) 916-8433','South Carolina','Hayley','eu nulla at sem molestie sodales. Mauris blandit enim consequat purus. Maecenas libero est, congue a, aliquet vel, vulputate eu, odio. Phasellus at augue id ante dictum cursus. Nunc mauris','1','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Haviva','Clark Mcpherson','elementum.purus@interdum.edu','(576) 157-7493','Ohio','Bo','Fusce mollis. Duis sit amet diam eu dolor egestas rhoncus. Proin nisl sem, consequat nec, mollis vitae, posuere at, velit. Cras lorem lorem, luctus ut, pellentesque eget, dictum placerat, augue.','0','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Maisie','James Reilly','varius@velconvallisin.com','(915) 962-6673','Oregon','Nevada','auctor odio a purus. Duis elementum, dui quis accumsan convallis, ante lectus convallis est, vitae sodales nisi magna sed dui. Fusce aliquam, enim nec tempus scelerisque, lorem ipsum sodales purus,','0','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Larissa','Jelani Mcfadden','enim.Suspendisse.aliquet@risus.com','(942) 533-0393','ON','Harlan','Etiam imperdiet dictum magna. Ut tincidunt orci quis lectus. Nullam suscipit, est ac facilisis facilisis, magna tellus faucibus leo, in lobortis tellus justo sit amet nulla. Donec non justo. Proin','1','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Eric','Colton Dennis','ornare.elit@luctusipsumleo.com','(929) 323-5769','Connecticut','Kiayada','at, velit. Cras lorem lorem, luctus ut, pellentesque eget, dictum placerat, augue. Sed molestie. Sed id risus quis diam luctus lobortis. Class aptent taciti sociosqu ad litora torquent per conubia','0','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Malcolm','Stewart Golden','eu.odio@ipsumporta.org','(458) 841-7730','Illinois','Rigel','enim. Mauris quis turpis vitae purus gravida sagittis. Duis gravida. Praesent eu nulla at sem molestie sodales. Mauris blandit enim consequat purus. Maecenas libero est, congue a, aliquet vel, vulputate','1','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Nicholas','Colby Barber','cursus@velfaucibusid.com','(122) 858-6438','British Columbia','David','Donec feugiat metus sit amet ante. Vivamus non lorem vitae odio sagittis semper. Nam tempor diam dictum sapien. Aenean massa. Integer vitae nibh. Donec est mauris, rhoncus id, mollis nec,','1','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Vanna','Silas Berry','et.ipsum.cursus@posuere.ca','(264) 676-8527','AZ','Carolyn','non dui nec urna suscipit nonummy. Fusce fermentum fermentum arcu. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Phasellus ornare. Fusce mollis. Duis sit amet','0','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Jasper','Hilel Franklin','varius.Nam@sapien.edu','(798) 604-0617','Illinois','Plato','auctor non, feugiat nec, diam. Duis mi enim, condimentum eget, volutpat ornare, facilisis eget, ipsum. Donec sollicitudin adipiscing ligula. Aenean gravida nunc sed pede. Cum sociis natoque penatibus et magnis','1','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Jescie','Clark Blake','penatibus@aliquetProin.edu','(958) 128-8882','Nunavut','Candice','fermentum metus. Aenean sed pede nec ante blandit viverra. Donec tempus, lorem fringilla ornare placerat, orci lacus vestibulum lorem, sit amet ultricies sem magna nec quam. Curabitur vel lectus. Cum','0','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Ima','Lucian Boone','Donec@lorem.edu','(976) 271-0748','Newfoundland and Labrador','Evelyn','sit amet diam eu dolor egestas rhoncus. Proin nisl sem, consequat nec, mollis vitae, posuere at, velit. Cras lorem lorem, luctus ut, pellentesque eget, dictum placerat, augue. Sed molestie. Sed','1','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Henry','Keith Patterson','sit.amet@anteNunc.edu','(584) 782-2094','Nunavut','Denton','risus, at fringilla purus mauris a nunc. In at pede. Cras vulputate velit eu sem. Pellentesque ut ipsum ac mi eleifend egestas. Sed pharetra, felis eget varius ultrices, mauris ipsum','1','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Bryar','Cameron Hester','enim.commodo@Vestibulumanteipsum.edu','(956) 205-5738','Missouri','Fletcher','Phasellus dolor elit, pellentesque a, facilisis non, bibendum sed, est. Nunc laoreet lectus quis massa. Mauris vestibulum, neque sed dictum eleifend, nunc risus varius orci, in consequat enim diam vel','1','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Myles','Hoyt Harrington','tellus@Duiscursus.edu','(263) 269-8793','DC','Channing','Nam nulla magna, malesuada vel, convallis in, cursus et, eros. Proin ultrices. Duis volutpat nunc sit amet metus. Aliquam erat volutpat. Nulla facilisis. Suspendisse commodo tincidunt nibh. Phasellus nulla. Integer','0','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Ciara','Melvin Hess','quis.tristique@mollisPhaselluslibero.org','(561) 677-9938','Florida','Laith','id enim. Curabitur massa. Vestibulum accumsan neque et nunc. Quisque ornare tortor at risus. Nunc ac sem ut dolor dapibus gravida. Aliquam tincidunt, nunc ac mattis ornare, lectus ante dictum','1','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Blake','Keith Mays','aliquet.odio.Etiam@sit.com','(614) 261-3281','California','Noble','tincidunt, nunc ac mattis ornare, lectus ante dictum mi, ac mattis velit justo nec ante. Maecenas mi felis, adipiscing fringilla, porttitor vulputate, posuere vulputate, lacus. Cras interdum. Nunc sollicitudin commodo','1','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Kaitlin','Neil Walter','velit.eu.sem@semeget.org','(369) 721-2483','British Columbia','Yasir','Curabitur egestas nunc sed libero. Proin sed turpis nec mauris blandit mattis. Cras eget nisi dictum augue malesuada malesuada. Integer id magna et ipsum cursus vestibulum. Mauris magna. Duis dignissim','0','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Dillon','Flynn Gross','metus.Aliquam@faucibus.org','(991) 627-5907','NU','Ocean','lorem fringilla ornare placerat, orci lacus vestibulum lorem, sit amet ultricies sem magna nec quam. Curabitur vel lectus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.','0','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Mason','Xenos Jennings','mollis@magnatellusfaucibus.ca','(762) 451-5143','MT','Vivian','metus sit amet ante. Vivamus non lorem vitae odio sagittis semper. Nam tempor diam dictum sapien. Aenean massa. Integer vitae nibh. Donec est mauris, rhoncus id, mollis nec, cursus a,','0','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Shafira','Philip Rios','in.magna.Phasellus@MaurisnullaInteger.org','(922) 799-9351','Ontario','Vance','Praesent luctus. Curabitur egestas nunc sed libero. Proin sed turpis nec mauris blandit mattis. Cras eget nisi dictum augue malesuada malesuada. Integer id magna et ipsum cursus vestibulum. Mauris magna.','1','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Josiah','Barrett Mckenzie','ante.Maecenas.mi@tinciduntdui.ca','(832) 434-6136','FL','Ruth','ac orci. Ut semper pretium neque. Morbi quis urna. Nunc quis arcu vel quam dignissim pharetra. Nam ac nulla. In tincidunt congue turpis. In condimentum. Donec at arcu. Vestibulum ante','1','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Martina','Daniel Dalton','sagittis@tellus.org','(312) 196-2396','British Columbia','Naida','ultricies ornare, elit elit fermentum risus, at fringilla purus mauris a nunc. In at pede. Cras vulputate velit eu sem. Pellentesque ut ipsum ac mi eleifend egestas. Sed pharetra, felis','0','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Maris','Arden Vazquez','arcu.ac.orci@dolor.ca','(946) 567-7763','Alberta','Inga','in aliquet lobortis, nisi nibh lacinia orci, consectetuer euismod est arcu ac orci. Ut semper pretium neque. Morbi quis urna. Nunc quis arcu vel quam dignissim pharetra. Nam ac nulla.','1','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Herrod','Kennedy Velazquez','fermentum.fermentum@rutrumjustoPraesent.edu','(772) 666-1239','AB','McKenzie','Morbi quis urna. Nunc quis arcu vel quam dignissim pharetra. Nam ac nulla. In tincidunt congue turpis. In condimentum. Donec at arcu. Vestibulum ante ipsum primis in faucibus orci luctus','1','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Candice','Isaiah Kidd','mollis.lectus.pede@magna.org','(360) 437-6943','AZ','Preston','ornare placerat, orci lacus vestibulum lorem, sit amet ultricies sem magna nec quam. Curabitur vel lectus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec dignissim','0','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Gage','Perry Melendez','ut@porttitor.org','(963) 599-5333','NB','Jaime','non arcu. Vivamus sit amet risus. Donec egestas. Aliquam nec enim. Nunc ut erat. Sed nunc est, mollis non, cursus non, egestas a, dui. Cras pellentesque. Sed dictum. Proin eget','0','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Sierra','Barclay Castaneda','elit.pellentesque.a@diamDuismi.com','(840) 547-8868','AB','Indigo','Vestibulum ut eros non enim commodo hendrerit. Donec porttitor tellus non magna. Nam ligula elit, pretium et, rutrum non, hendrerit id, ante. Nunc mauris sapien, cursus in, hendrerit consectetuer, cursus','1','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Allegra','Lewis Conner','In@feugiat.edu','(724) 209-2539','ID','Ora','sollicitudin orci sem eget massa. Suspendisse eleifend. Cras sed leo. Cras vehicula aliquet libero. Integer in magna. Phasellus dolor elit, pellentesque a, facilisis non, bibendum sed, est. Nunc laoreet lectus','0','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Shaine','Alexander Harmon','et.malesuada@porta.edu','(515) 787-1081','Illinois','Maia','consectetuer ipsum nunc id enim. Curabitur massa. Vestibulum accumsan neque et nunc. Quisque ornare tortor at risus. Nunc ac sem ut dolor dapibus gravida. Aliquam tincidunt, nunc ac mattis ornare,','0','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Matthew','Henry Ramos','amet.ornare@liberoMorbiaccumsan.ca','(897) 148-6163','MD','Leandra','fermentum risus, at fringilla purus mauris a nunc. In at pede. Cras vulputate velit eu sem. Pellentesque ut ipsum ac mi eleifend egestas. Sed pharetra, felis eget varius ultrices, mauris','0','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Jackson','Brett Herring','consectetuer.adipiscing.elit@acmattissemper.com','(221) 111-8157','Delaware','Autumn','tristique pharetra. Quisque ac libero nec ligula consectetuer rhoncus. Nullam velit dui, semper et, lacinia vitae, sodales at, velit. Pellentesque ultricies dignissim lacus. Aliquam rutrum lorem ac risus. Morbi metus.','0','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Urielle','Carter Dixon','libero@Intincidunt.com','(258) 571-6827','NT','Uriel','imperdiet, erat nonummy ultricies ornare, elit elit fermentum risus, at fringilla purus mauris a nunc. In at pede. Cras vulputate velit eu sem. Pellentesque ut ipsum ac mi eleifend egestas.','0','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Tatum','Oleg Dawson','metus.Aenean.sed@odioPhasellus.ca','(156) 472-2104','NV','Brynne','feugiat tellus lorem eu metus. In lorem. Donec elementum, lorem ut aliquam iaculis, lacus pede sagittis augue, eu tempor erat neque non quam. Pellentesque habitant morbi tristique senectus et netus','1','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Quinn','Rajah Richardson','lobortis.ultrices@Proinultrices.org','(228) 233-8700','New Brunswick','Wallace','eu eros. Nam consequat dolor vitae dolor. Donec fringilla. Donec feugiat metus sit amet ante. Vivamus non lorem vitae odio sagittis semper. Nam tempor diam dictum sapien. Aenean massa. Integer','1','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Demetria','Hiram Jimenez','primis.in@augue.ca','(997) 600-3137','AB','Amos','ipsum leo elementum sem, vitae aliquam eros turpis non enim. Mauris quis turpis vitae purus gravida sagittis. Duis gravida. Praesent eu nulla at sem molestie sodales. Mauris blandit enim consequat','0','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Belle','Lawrence Patterson','Duis.volutpat@Nullam.org','(439) 338-9980','AB','Harding','malesuada fames ac turpis egestas. Aliquam fringilla cursus purus. Nullam scelerisque neque sed sem egestas blandit. Nam nulla magna, malesuada vel, convallis in, cursus et, eros. Proin ultrices. Duis volutpat','0','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Tyrone','Damon Walker','ac@condimentumDonec.ca','(480) 923-8566','Nevada','Kellie','erat volutpat. Nulla facilisis. Suspendisse commodo tincidunt nibh. Phasellus nulla. Integer vulputate, risus a ultricies adipiscing, enim mi tempor lorem, eget mollis lectus pede et risus. Quisque libero lacus, varius','1','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Donovan','Rashad Obrien','ac.nulla.In@penatibusetmagnis.org','(314) 363-2566','West Virginia','Tatum','in consequat enim diam vel arcu. Curabitur ut odio vel est tempor bibendum. Donec felis orci, adipiscing non, luctus sit amet, faucibus ut, nulla. Cras eu tellus eu augue porttitor','0','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Yasir','Carl Petersen','orci.adipiscing@infaucibus.edu','(318) 949-4667','British Columbia','Len','risus a ultricies adipiscing, enim mi tempor lorem, eget mollis lectus pede et risus. Quisque libero lacus, varius et, euismod et, commodo at, libero. Morbi accumsan laoreet ipsum. Curabitur consequat,','0','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Reuben','Stone Mcintyre','netus.et@porttitorerosnec.com','(286) 407-1021','Idaho','Tobias','ridiculus mus. Aenean eget magna. Suspendisse tristique neque venenatis lacus. Etiam bibendum fermentum metus. Aenean sed pede nec ante blandit viverra. Donec tempus, lorem fringilla ornare placerat, orci lacus vestibulum','0','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Dawn','Finn Sandoval','turpis.non@eunullaat.org','(590) 918-5593','Yukon','Katell','Aenean eget magna. Suspendisse tristique neque venenatis lacus. Etiam bibendum fermentum metus. Aenean sed pede nec ante blandit viverra. Donec tempus, lorem fringilla ornare placerat, orci lacus vestibulum lorem, sit','1','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Lara','Gareth Snider','libero.Donec.consectetuer@aliquet.edu','(443) 192-1940','TX','Wanda','consequat enim diam vel arcu. Curabitur ut odio vel est tempor bibendum. Donec felis orci, adipiscing non, luctus sit amet, faucibus ut, nulla. Cras eu tellus eu augue porttitor interdum.','1','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Wynter','Colin Camacho','mi.fringilla@nequeSed.ca','(245) 479-7899','Saskatchewan','Hyacinth','Quisque purus sapien, gravida non, sollicitudin a, malesuada id, erat. Etiam vestibulum massa rutrum magna. Cras convallis convallis dolor. Quisque tincidunt pede ac urna. Ut tincidunt vehicula risus. Nulla eget','0','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Wynne','Mohammad Myers','neque.venenatis@sitametdapibus.edu','(702) 416-9549','Newfoundland and Labrador','Rudyard','Aenean sed pede nec ante blandit viverra. Donec tempus, lorem fringilla ornare placerat, orci lacus vestibulum lorem, sit amet ultricies sem magna nec quam. Curabitur vel lectus. Cum sociis natoque','0','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Baker','Honorato Ingram','est@eu.ca','(873) 843-0857','Alberta','Karyn','Suspendisse tristique neque venenatis lacus. Etiam bibendum fermentum metus. Aenean sed pede nec ante blandit viverra. Donec tempus, lorem fringilla ornare placerat, orci lacus vestibulum lorem, sit amet ultricies sem','1','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Jin','Cedric Gould','quam.vel.sapien@consequatpurusMaecenas.com','(332) 110-3947','New Brunswick','Elaine','libero lacus, varius et, euismod et, commodo at, libero. Morbi accumsan laoreet ipsum. Curabitur consequat, lectus sit amet luctus vulputate, nisi sem semper erat, in consectetuer ipsum nunc id enim.','1','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Iliana','Jack Booth','neque@velit.org','(558) 971-2733','NB','Adara','arcu. Vivamus sit amet risus. Donec egestas. Aliquam nec enim. Nunc ut erat. Sed nunc est, mollis non, cursus non, egestas a, dui. Cras pellentesque. Sed dictum. Proin eget odio.','0','0');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Harriet','Vernon Vance','Sed.diam.lorem@ascelerisque.org','(433) 188-9860','Michigan','Miriam','a, aliquet vel, vulputate eu, odio. Phasellus at augue id ante dictum cursus. Nunc mauris elit, dictum eu, eleifend nec, malesuada ut, sem. Nulla interdum. Curabitur dictum. Phasellus in felis.','0','1');
INSERT INTO player (nick,name,email,phone,location,pinside,notes,status,active) VALUES ('Channing','Kaseem Adkins','non@interdumCurabiturdictum.ca','(359) 192-3012','YT','Halla','sodales nisi magna sed dui. Fusce aliquam, enim nec tempus scelerisque, lorem ipsum sodales purus, in molestie tortor nibh sit amet orci. Ut sagittis lobortis mauris. Suspendisse aliquet molestie tellus.','1','1');






