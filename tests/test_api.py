import unittest


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
