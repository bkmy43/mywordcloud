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
('French'),
('Spanish'),
('Arabic'),
('Russian');

DROP TABLE IF EXISTS user_account CASCADE;
CREATE TABLE user_account(
u_id serial primary key,
u_uuid UUID,
u_firstname text,
u_lastname text,
u_native_language integer references user_language(l_id),
u_country text,
u_address text
);
CREATE UNIQUE INDEX name ON user_account (u_uuid);

DROP TABLE IF EXISTS user_word CASCADE;
CREATE TABLE user_record_sessions(
r_id serial primary key,
r_language integer references user_language(l_id),
r_


DROP TABLE IF EXISTS word CASCADE;
CREATE TABLE user_words(
w_id serial primary key,
w_language text
w_word text,

);

