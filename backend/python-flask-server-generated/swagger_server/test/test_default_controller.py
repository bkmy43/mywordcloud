# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.word_item import WordItem  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_add_word(self):
        """Test case for add_word

        adds a word to user statistics
        """
        word = [List[str]()]
        response = self.client.open(
            '/redi/mywordcloud/1.0.0/words',
            method='POST',
            data=json.dumps(word),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_words(self):
        """Test case for get_words

        searches statistics over words usage in the database for particular user and language
        """
        query_string = [('user_uuid', 'user_uuid_example'),
                        ('language', 'language_example'),
                        ('skip', 1),
                        ('limit', 50)]
        response = self.client.open(
            '/redi/mywordcloud/1.0.0/words',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
