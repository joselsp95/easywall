"""
TODO: Doku
"""
from tests import unittest
from tests.web.test_login import TestLogin
from tests.web.utils import (prepare_client, prepare_configuration,
                             restore_configuration)


class TestIndex(unittest.TestCase):
    """
    TODO: Doku
    """

    def setUp(self):
        prepare_configuration()
        self.client = prepare_client()
        self.login = TestLogin()

    def tearDown(self):
        restore_configuration()

    def test_index_logged_out(self):
        """
        TODO: Doku
        """
        response = self.client.get('/')
        self.assertIn(b"Please sign in", response.data)

    def test_index_logged_in(self):
        """
        TODO: Doku
        """
        self.login.log_in(self.client)
        response = self.client.get('/')
        self.assertIn(b"Configure Ports", response.data)
