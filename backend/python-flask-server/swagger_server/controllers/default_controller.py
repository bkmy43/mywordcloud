import connexion
import six
import os
import sys
import inspect

from swagger_server.models.word_item import WordItem  # noqa: E501
from swagger_server import util

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, currentdir)

from mywordcloud_data import *


def add_word(word=None):  # noqa: E501
    """adds a word to user statistics

    for particular user adds word usage statistics, including category and count # noqa: E501

    :param word: list of words to add
    :type word: List[]

    :rtype: None
    """
    add_words_to_db(get_db_connection(), word)


def get_words(user_uuid, language, skip=None, limit=None):  # noqa: E501
    """searches statistics over words usage in the database for particular user and language

    By passing in the appropriate options (user_id, language), you can search for statistics over word usage in mywordcloud database  # noqa: E501

    :param user_uuid: user id is required to search for words
    :type user_uuid: str
    :param language: language to limit the search to
    :type language: str
    :param skip: number of records to skip for pagination
    :type skip: int
    :param limit: maximum number of records to return
    :type limit: int

    :rtype: List[WordItem]
    """

    return get_word_stats_from_db(get_db_connection(), user_uuid, language, skip, limit)


def get_wordcloud(user_uuid, language):  # noqa: E501
    """visualizes wordcloud for specified user and language as a picture

    By passing in the appropriate options (user_id, language), you can generate wordcloud picture as png  # noqa: E501

    :param user_uuid: user id is required to search for words
    :type user_uuid: str
    :param language: language to limit the search to
    :type language: str

    :rtype: image/png
    """
    return get_wordcloud_image(db_connection=get_db_connection(),user_uuid=user_uuid, language=language)

def get_image(word):  # noqa: E501
    """gets first picture from google image search by given word

    By passing in the word you can get an image from google for it # noqa: E501

    :param word: word to search google for
    :type word: str

    :rtype: image/*
    """
    return get_image_from_google(word=word)
