CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

DROP TABLE IF EXISTS user_language CASCADE;
CREATE TABLE user_language(
l_id serial primary key,
l_language text
);

INSERT INTO user_language (l_language)
VALUES
('English'),
('German'),
('French'),
('Spanish'),
('Arabic'),
('Russian');

DROP TABLE IF EXISTS record_session_category CASCADE;
CREATE TABLE record_session_category(
c_id serial primary key,
c_category text
);
INSERT INTO record_session_category (c_category)
VALUES
('Family'),
('Friends'),
('Business');

DROP TABLE IF EXISTS user_account CASCADE;
CREATE TABLE user_account(
u_id serial primary key,
u_uuid UUID NOT NULL,
u_firstname text NOT NULL,
u_lastname text NOT NULL,
u_native_language integer references user_language(l_id),
u_country text,
u_address text
);
CREATE UNIQUE INDEX name ON user_account (u_uuid);

INSERT INTO user_account (u_uuid, u_firstname, u_lastname)
VALUES
('36ff545d-ca5a-4855-985b-eda712781efb','John', 'Miller'),
(uuid_generate_v4(), 'Merry', 'Shelly'),
(uuid_generate_v4(), 'Fyodor', 'Raskolnikow');


DROP TABLE IF EXISTS user_record_sessions CASCADE;
CREATE TABLE user_record_sessions(
r_id serial primary key,
r_created timestamp,
r_language integer references user_language(l_id)
);


DROP TABLE IF EXISTS user_words CASCADE;
CREATE TABLE user_words(
w_id serial primary key,
w_user_id integer references user_account(u_id),
w_language text,
w_word text,
w_count integer
);


