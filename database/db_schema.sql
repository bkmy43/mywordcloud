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
r_language_id integer references user_language(l_id)
);


DROP TABLE IF EXISTS user_word CASCADE;
CREATE TABLE user_word(
w_id serial primary key,
w_user_id integer references user_account(u_id),
w_language_id integer references user_language(l_id),
w_word text,
w_count integer
);

CREATE OR REPLACE VIEW v_words_by_language
AS
SELECT u_uuid,
       l_language,
       count(*) AS number_of_words
  FROM user_account
  JOIN user_word ON w_user_id = u_id
  JOIN user_language ON w_language_id = l_id
 GROUP BY u_uuid,
          l_language
 ORDER BY count(*) DESC;

CREATE OR REPLACE VIEW public.v_user_word_total AS 
 SELECT user_account.u_uuid,
    user_language.l_language,
    user_word.w_word,
    sum(user_word.w_count) AS w_total_count
   FROM user_account
     JOIN user_word ON user_word.w_user_id = user_account.u_id
     JOIN user_language ON user_word.w_language_id = user_language.l_id
  GROUP BY user_account.u_uuid, user_language.l_language, user_word.w_word
  ORDER BY (sum(user_word.w_count)) DESC;