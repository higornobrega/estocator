import json
import unittest

from app import app


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get("/")
        self.assertEqual(json.loads(
            response.data.decode("utf-8")), {"hello": "Flask!"})
