from app import app
import re
import json

import unittest

class FlaskAppTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        pass

    def test_posts_data(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.post('/cache',
            data=json.dumps({'data': 'boo yah'}),
            content_type='application/json',
            )

        json_result = json.loads(result.data)
        id = json_result['id']

        self.assertEqual(result.status_code, 200)
        self.assertTrue(is_uuid(id))

        result = self.app.get('/cache?id='+json_result['id'])
        json_result = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(id, json_result['id'])
        self.assertEqual(json_result['data'], 'boo yah')



def is_uuid(uuid):
# Found method on stackoverflow; figured it was okay to swipe for testing purposes
    UUID_PATTERN = re.compile(r'^[\da-f]{8}-([\da-f]{4}-){3}[\da-f]{12}$', re.IGNORECASE)

    if UUID_PATTERN.match(uuid):
        return True
    else:
        return False
