import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.insert(0, currentdir)

from mywordcloud_data import *
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


SAMPLE_FILE = '../hamlet.txt'

def fill_db_with_shakespeare():
    f = open(SAMPLE_FILE)

    text = f.read()
    text = text.replace("'", "")
    words = text.split()
    print(len(words))

    add_words_to_db(get_db_connection(), words)


def display_wordcloud(words):
    wordcloud = WordCloud(width=1000, height=500).generate(' '.join(words))
    plt.figure(figsize=(15, 8))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

    # wordcloud.to_file("word_cloud.png")

# fill_db_with_shakespeare()
# display_wordcloud(get_words_from_db(get_db_connection()))
