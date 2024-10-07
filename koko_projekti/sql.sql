CREATE TABLE ports
(
	id				INT			auto_increment
		PRIMARY KEY,
	iso_country	    VARCHAR(3)	NULL,
	name			VARCHAR(40)	NULL,
	type			VARCHAR(40)	NULL,
	country		    VARCHAR(40)	NULL,
	price			INT			NULL,
	ident			VARCHAR(40)	NULL,
	owner			VARCHAR(40)	NULL,
	lvl			    INT			NULL
)

CHARSET = LATIN1;

CREATE TABLE player
(
	name		VARCHAR(40)
		PRIMARY KEY,
	money		INT,
	position	INT
)

CHARSET = LATIN1;

CREATE TABLE property
(
	owner	VARCHAR(40)	NOT NULL,
	id		INT			NOT NULL,
	PRIMARY KEY (owner, id),
	FOREIGN KEY (owner) REFERENCES player(name),
	FOREIGN KEY (id)    REFERENCES ports(id)
)

CHARSET = LATIN1;

CREATE TABLE airpoly_results
(
	peli_id		INT			auto_increment
		PRIMARY KEY,
	pyörät		INT			NOT NULL,
	voittaja	VARCHAR(40)	NOT NULL,
	pääoma		INT			NOT NULL
)

CHARSET = LATIN1
;


CREATE TABLE stats_minigames (
    player_name		VARCHAR(255),
    minigames_won 	INT,
    minigames_lost  INT,
    km_won 			INT,
    km_lost 		INT
	);

CREATE TABLE stats_airport (
   player_name 		VARCHAR(255),
   airports_visited VARCHAR(255)
);


create table player_information(
	ID 			int not null auto_increment,
	first_name 	varchar(40),
	last_name 	varchar(40),
	ident 		varchar(40),
	age 		int(11),
	primary key (ID)
);

create table player_goal(
	ID 				int not null auto_increment,
	first_name 		varchar(40),
	player_level 	varchar(40),
	continet 		varchar(40),
	ident 			varchar(40),
	player_points 	int(50),
	player_fuel 	int( 11),
	primary key (ID)
);

create table goal_reached(
	player_information_ID 	int,
	player_goal_ID 			int,
	primary key (player_information_ID, player_goal_ID),
	foreign key (player_information_ID) references player_information(ID),
	foreign key (player_goal_ID) 		references player_goal(ID)
 
);