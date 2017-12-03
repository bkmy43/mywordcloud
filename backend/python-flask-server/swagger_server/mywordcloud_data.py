import sqlalchemy, json
import os
import sys
import inspect
import json

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, currentdir)

from mywordcloud_data import *
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

DB_HOST = 'mywordcloud.cuhcnlmjs7ol.us-east-2.rds.amazonaws.com'
DB_PORT = 5432
DB_USER = 'mywordcloud'
DB_PASSWORD = 'redischool'
DB_NAME = 'mywordclouddb'

DB_CONNECTION = None

def get_db_connection():
    global DB_CONNECTION
    if DB_CONNECTION:
        return DB_CONNECTION

    conn_string = 'postgresql://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_NAME
    DB_CONNECTION = sqlalchemy.create_engine(conn_string, client_encoding='utf8').connect()
    return DB_CONNECTION


def get_user_id_by_uuid(db_connection, user_uuid):
    sql = "SELECT u_id from user_account WHERE u_uuid ='{}'".format(user_uuid)
    res = db_connection.execute(sql).fetchone()
    return res[0]


def get_language_id_by_name(db_connection, language):
    sql = "SELECT l_id from user_language WHERE l_language ='{}'".format(language)
    res = db_connection.execute(sql).fetchone()
    return res[0]


def add_words_to_db(db_connection, list_of_words, user_uuid = '36ff545d-ca5a-4855-985b-eda712781efb',
                    language='English'):
    if not list_of_words:
        return

    user_id = get_user_id_by_uuid(db_connection, user_uuid)
    language_id = get_language_id_by_name(db_connection, language)

    counted_words = dict()
    sql = "INSERT INTO user_word(w_word, w_count, w_user_id, w_language_id) VALUES "
    for word in list_of_words:
        if word in counted_words:
            counted_words[word] += 1
        else:
            counted_words[word] = 1

    first_value = True
    for word in counted_words:
        if first_value:
            delimiter = ''
            first_value = False
        else:
            delimiter = ', '
        sql += "{}('{}', {}, {}, {})".format(delimiter, word, counted_words[word], user_id, language_id)

    db_connection.execute(sql)


def get_words_from_db(db_connection, user_uuid='36ff545d-ca5a-4855-985b-eda712781efb', language='English'):

    user_id = get_user_id_by_uuid(db_connection, user_uuid)
    language_id = get_language_id_by_name(db_connection, language)

    words = list()
    sql = "SELECT w_word, w_count FROM user_word WHERE w_user_id={} AND w_language_id={}".format(user_id, language_id)
    result = db_connection.execute(sql)

    for row in result:
        for _ in range(row[1]):
            words.append(row[0])

    return words


def get_word_stats_from_db(db_connection, user_uuid='36ff545d-ca5a-4855-985b-eda712781efb', language='English'):
    user_id = get_user_id_by_uuid(db_connection, user_uuid)
    language_id = get_language_id_by_name(db_connection, language)

    sql = u"SELECT w_word, 'general', w_count FROM user_word WHERE w_user_id={} AND w_language_id={}".format(user_id, language_id)

    result = db_connection.execute(sql)
    word_stats = list()
    for row in result:
        word_stats.append({'word':row[0], 'category':row[1], 'count': row[2]})

    return word_stats


def get_wordcloud_image(db_connection, user_uuid='36ff545d-ca5a-4855-985b-eda712781efb', language='English'):
    words = get_words_from_db(db_connection)
    wordcloud = WordCloud(width=1000, height=500).generate(' '.join(words))
    wordcloud.to_file("wordcloud.png")
    html = '<img src="wordcloud.png">​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​'
    return html


# print(get_word_stats_from_db(get_db_connection()))
# print(get_wordcloud_image(get_db_connection()))