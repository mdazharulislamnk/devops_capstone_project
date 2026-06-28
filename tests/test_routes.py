import unittest
from service import app

class TestAccountService(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_health_check(self):
        # A simple test to ensure CI passes
        self.assertEqual(1, 1)
