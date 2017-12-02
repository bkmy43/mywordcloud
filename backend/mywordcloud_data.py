import sqlalchemy

DB_HOST = 'mywordcloud.cuhcnlmjs7ol.us-east-2.rds.amazonaws.com'
DB_PORT = 5432
DB_USER = 'mywordcloud'
DB_PASSWORD = 'redischool'
DB_NAME = 'mywordcloud'

def connect_to_database():
    conn_string = 'postgresql://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_NAME
    return sqlalchemy.create_engine(conn_string, client_encoding='utf8').connect()

#
# DROP TABLE IF EXISTS user_words CASCADE;
# CREATE TABLE user_words(
# w_id serial primary key,
# w_user_id integer references user_account(u_id),
# w_language text,
# w_word text,
# w_count integer
# );

def add_words(list_of_words):
    counted_words = dict()
    sql = "INSERT INTO user_words(w_word, w_count) VALUES "
    for word in list_of_words:
        if word in counted_words:
            counted_words[word] += 1
        else:
            counted_words[word] = 1

    print(counted_words)
    #
    # first_value = True
    # for word in counted_words:
    #     if first_value:
    #         delimiter = ''
    #     else:
    #         delimiter = ','
    #     sql += "%('%',%)" % (delimiter, word, counted_words[word])

    print(sql)
    conn = connect_to_database()
    conn.execute(sql_sales)

add_words(['aaa', 'bbb', 'aaa'])