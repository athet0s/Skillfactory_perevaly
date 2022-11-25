-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS pereval_areas_id_seq;

-- Table Definition
CREATE TABLE "public"."pereval_areas" (
    "id" int8 NOT NULL DEFAULT nextval('pereval_areas_id_seq'::regclass),
    "id_parent" int8 NOT NULL,
    "title" text,
    PRIMARY KEY ("id")
);

-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS pereval_added_id_seq;

-- Table Definition
CREATE TABLE "public"."pereval_images" (
    "id" int4 NOT NULL DEFAULT nextval('pereval_added_id_seq'::regclass),
    "date_added" timestamp DEFAULT now(),
    "img" bytea NOT NULL,
    "title" text,
    PRIMARY KEY ("id")
);

-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS untitled_table_200_id_seq;

-- Table Definition
CREATE TABLE "public"."spr_activities_types" (
    "id" int4 NOT NULL DEFAULT nextval('untitled_table_200_id_seq'::regclass),
    "title" text,
    PRIMARY KEY ("id")
);

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS users_id_seq;

-- Table Definition
CREATE TABLE "public"."users" (
    "id" int4 NOT NULL DEFAULT nextval('users_id_seq'::regclass),
    "fam" text,	"name" text,	"otc" text,
	"phone" text,
	"email" text NOT NULL,
	CONSTRAINT email_unique UNIQUE (email),
    PRIMARY KEY ("id")
);

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS coords_id_seq;

-- Table Definition
CREATE TABLE "public"."coords" (
    "id" int4 NOT NULL DEFAULT nextval('coords_id_seq'::regclass),
    "latitude" real,
    "longitude" real,
    "height" integer,
    PRIMARY KEY ("id")
);

-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS pereval_id_seq;

-- Table Definition
CREATE TABLE "public"."pereval_added" (
    "id" int4 NOT NULL DEFAULT nextval('pereval_id_seq'::regclass),
    "date_added" timestamp,
    "status" text NOT NULL,
    "beauty_title" text,
	"title" text,
	"other_titles" text,
	"connect" text,
	"add_time" timestamp,
	"level_winter" text,
	"level_summer" text,
	"level_autumn" text,
	"level_spring" text,
	"coord_id" int4 NOT NULL,
	"user_id" int4 NOT NULL, 
	FOREIGN KEY (coord_id) REFERENCES coords(id) ON DELETE CASCADE,
	FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    PRIMARY KEY ("id")
);

-- Table Definition
CREATE TABLE "public"."pereval_added_pereval_images" (
	"pereval_id" int4 NOT NULL,
	"image_id" int4 NOT NULL, 
	FOREIGN KEY (pereval_id) REFERENCES pereval_added(id) ON DELETE CASCADE,
    FOREIGN KEY (image_id) REFERENCES pereval_images(id) ON DELETE CASCADE,
    PRIMARY KEY (pereval_id, image_id)
);

INSERT INTO "public"."spr_activities_types" ("id", "title") VALUES
(1, '„„u„Š„{„€„}'),
(2, '„|„„w„y'),
(3, '„{„p„„„p„}„p„‚„p„~'),
(4, '„q„p„z„t„p„‚„{„p'),
(5, '„„|„€„„'),
(6, '„ƒ„„|„p„r'),
(7, '„r„u„|„€„ƒ„y„„u„t'),
(8, '„p„r„„„€„}„€„q„y„|„'),
(9, '„}„€„„„€„ˆ„y„{„|'),
(10, '„„p„‚„…„ƒ'),
(11, '„r„u„‚„‡„€„}');

INSERT INTO "public"."pereval_areas" ("id", "id_parent", "title") VALUES
(0, 0, '„P„|„p„~„u„„„p „H„u„}„|„‘'),
(1, 0, '„P„p„}„y„‚„€-„@„|„p„z'),
(65, 0, '„@„|„„„p„z'),
(66, 65, '„R„u„r„u„‚„€-„X„…„z„ƒ„{„y„z „‡„‚„u„q„u„„'),
(88, 65, '„_„w„~„€-„X„…„z„ƒ„{„y„z „‡„‚„u„q„u„„'),
(92, 65, '„K„p„„„…„~„ƒ„{„y„z „‡„‚„u„q„u„„'),
(105, 1, '„U„p„~„ƒ„{„y„u „s„€„‚„'),
(106, 1, '„C„y„ƒ„ƒ„p„‚„ƒ„{„y„z „‡„‚„u„q„u„„ („…„‰„p„ƒ„„„€„{ „x„p„„p„t„~„u„u „„u„‚„u„r„p„|„p „@„~„x„€„q)'),
(131, 1, '„M„p„„„‰„y„~„ƒ„{„y„z „s„€„‚„~„„z „…„x„u„|'),
(133, 1, '„C„€„‚„~„„z „…„x„u„| „S„p„{„p„|„y, „S„…„‚„{„u„ƒ„„„p„~„ƒ„{„y„z „‡„‚„u„q„u„„'),
(137, 1, '„B„„ƒ„€„{„y„z „@„|„p„z'),
(147, 1, '„K„y„‰„y„{-„@„|„p„z „y „B„€„ƒ„„„€„‰„~„„z „@„|„p„z'),
(367, 375, '„@„|„p„t„p„s„|„p„‚'),
(375, 0, '„S„p„r„‚'),
(384, 0, '„R„p„‘„~„'),
(386, 65, '„V„‚„u„q„u„„ „L„y„ƒ„„„r„‘„s„p'),
(387, 65, '„I„r„p„~„€„r„ƒ„{„y„z „‡„‚„u„q„u„„'),
(388, 65, '„M„p„ƒ„ƒ„y„r „M„…„~„s„…„~-„S„p„z„s„p'),
(389, 65, '„V„‚„u„q„u„„ „W„p„s„p„~-„Y„y„q„„„„…'),
(390, 65, '„V„‚„u„q„u„„ „X„y„‡„p„‰„u„r„p („R„p„z„|„„s„u„})'),
(391, 65, '„Y„p„„Š„p„|„„ƒ„{„y„z „‡„‚„u„q„u„„'),
(392, 65, '„V„‚„u„q„u„„ „_„w„~„„z „@„|„„„p„z'),
(393, 65, '„V„‚„u„q„u„„ „M„€„~„s„€„|„„ƒ„{„y„z „@„|„„„p„z'),
(398, 384, '„H„p„„p„t„~„„z „R„p„‘„~'),
(399, 384, '„B„€„ƒ„„„€„‰„~„„z „R„p„‘„~'),
(402, 384, '„K„…„x„~„u„ˆ„{„y„z „@„|„p„„„p„…'),
(459, 65, '„K„…„‚„p„z„ƒ„{„y„z „‡„‚„u„q„u„„');
