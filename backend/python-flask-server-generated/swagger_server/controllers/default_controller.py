import connexion
import six

from swagger_server.models.word_item import WordItem  # noqa: E501
from swagger_server import util


def add_word(word=None):  # noqa: E501
    """adds a word to user statistics

    for particular user adds word usage statistics, including category and count # noqa: E501

    :param word: list of words to add
    :type word: List[]

    :rtype: None
    """
    return 'do some magic!'


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
    return 'do some magic!'
