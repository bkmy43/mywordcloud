import os, sys, inspect
import string
import nltk
from nltk.stem.wordnet import WordNetLemmatizer

curdir = os.path.dirname(os.path.relpath(__file__))
libdir = curdir + '/../backend/python-flask-server/swagger_server'

sys.path.insert(0, libdir)
from mywordcloud_data import *
print(curdir, libdir)

sample_data = [dict(filename=curdir + '/hamlet.txt', user_uuid='e2401176-8603-432c-a0e1-462fcecb2b4b'),
               dict(filename=curdir + '/hamingway.txt', user_uuid='5c292fc8-0147-4431-9268-6800dddd0480')]


def fill_db_with_sample_data():
    nltk.download('wordnet')

    for sample in sample_data:
        f = open(sample['filename'])
        text = f.read()
        transtable = str.maketrans('', '', string.punctuation)
        text = text.translate(transtable)
        words = text.split()
        words = [WordNetLemmatizer().lemmatize(word.lower().strip(), 'v') for word in words]

        add_words_to_db(db_connection=get_db_connection(), list_of_words=words, user_uuid=sample['user_uuid'])
        print("Inserted {} words from {} to the database".format(len(words), sample['filename']))


def main():
    fill_db_with_sample_data()

if __name__ == '__main__':
    main()

