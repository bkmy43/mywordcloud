import os, sys, inspect
import string
import nltk
from nltk.stem.wordnet import WordNetLemmatizer

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.insert(0, currentdir)

from mywordcloud_data import *
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


SAMPLE_FILE = '../hamlet.txt'


def fill_db_with_shakespeare():
    f = open(SAMPLE_FILE)

    text = f.read()
    transtable = str.maketrans('', '', string.punctuation)
    text = text.translate(transtable)
    words = text.split()

    nltk.download('wordnet')
    words = [WordNetLemmatizer().lemmatize(word.lower().strip(), 'v') for word in words]

    add_words_to_db(get_db_connection(), words)
    print("Inserted {} words from text file to the database".format(len(words)))


def display_wordcloud(words):
    wordcloud = WordCloud(width=640, height=1136, background_color='BLACK',
                          collocations=False,
                          stopwords=STOPWORDS).generate(' '.join(words))
    plt.figure(figsize=(15, 8))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

    # wordcloud.to_file("word_cloud.png")

# fill_db_with_shakespeare()
display_wordcloud(get_words_from_db(get_db_connection()))
