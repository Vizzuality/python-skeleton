import unittest
import json
from ps import app


class BasicTest(unittest.TestCase):

    def setUp(self):
        app.testing = True
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def tearDown(self):
        pass

    def deserialize(self, response):
        return json.loads(response.data).get('data', None)

    def test_v1_hello(self):
        response = self.app.get('/api/v1/psone/hello', follow_redirects=True)
        status_code = response.status_code
        data = self.deserialize(response)
        self.assertEqual(status_code, 200)
        self.assertEqual(data[0].get('attributes').get('word'), 'hello')

    def test_v2_hello(self):
        response = self.app.get('/api/v1/pstwo/hello', follow_redirects=True)
        status_code = response.status_code
        data = self.deserialize(response)
        self.assertEqual(status_code, 200)
        self.assertEqual(data[0].get('attributes').get('word'), 'hello2')
