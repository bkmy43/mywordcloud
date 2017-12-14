import sqlalchemy, json
import os
import sys
import inspect
import io

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, currentdir)

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


def add_words_to_db(db_connection, list_of_words, user_uuid='36ff545d-ca5a-4855-985b-eda712781efb',
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


def get_word_stats_from_db(db_connection, user_uuid='36ff545d-ca5a-4855-985b-eda712781efb',
                           language='English', skip=None, limit=None):
    sql = u"SELECT w_word, 'general', w_total_count " \
          u"FROM v_user_word_total " \
          u"WHERE u_uuid='{}' AND l_language='{}'" \
          u"ORDER BY w_total_count DESC".format(user_uuid, language)

    if limit is not None:
        sql += u" LIMIT {}".format(limit)
    if skip is not None:
        sql += u" OFFSET {}".format(skip)

    result = db_connection.execute(sql)
    word_stats = list()
    for row in result:
        word_stats.append(dict(word=row[0], category=row[1], count=row[2]))

    return word_stats


def get_words_from_db(db_connection, user_uuid='36ff545d-ca5a-4855-985b-eda712781efb', language='English'):
    word_stats = get_word_stats_from_db(db_connection, user_uuid, language)
    words = list()

    for w in word_stats:
        for _ in range(w['count']):
            words.append(w['word'])
    return words


def get_wordcloud_image(db_connection, user_uuid='36ff545d-ca5a-4855-985b-eda712781efb', language='English'):
    words = get_words_from_db(db_connection, user_uuid, language)
    wordcloud = WordCloud(width=640, height=1136, background_color='BLACK',
                          collocations=False,
                          stopwords=STOPWORDS).generate(' '.join(words))

    output = io.BytesIO()
    wordcloud.to_image().save(output, format='PNG')
    return output.getvalue()


# get_wordcloud_image(get_db_connection())
