from copy import deepcopy
import unittest
import json

import app

BASE_URL = 'http://127.0.0.1:5000/api/v1.0/items'
BAD_ITEM_URL = '{}/5'.format(BASE_URL)
GOOD_ITEM_URL = '{}/3'.format(BASE_URL)


class TestFlaskApi(unittest.TestCase):

    def setUp(self):
        self.backup_items = deepcopy(app.items)  # no references!
        self.app = app.app.test_client()
        self.app.testing = True

    def test_get_one(self):
        response = self.app.get(BASE_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['items'][0]['name'], 'laptop')

    def test_item_not_exist(self):
        response = self.app.get(BAD_ITEM_URL)
        self.assertEqual(response.status_code, 404)

    def tearDown(self):
        # reset app.items to initial state
        app.items = self.backup_items


if __name__ == "__main__":
    unittest.main()