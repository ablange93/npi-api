from copy import deepcopy
import unittest
import json
from api import app


BASE_URL = 'http://127.0.0.1:5000/npi-api/v1.0'
PROVIDER_GOOD_URL = '{}/provider?npiId=1376064311'.format(BASE_URL)
ENDPOINT_GOOD_URL = '{}/endpoint?npiId=1376064311'.format(BASE_URL)

PROVIDER_BAD_URL = '{}/provider?npiId=1376000000'.format(BASE_URL)
ENDPOINT_BAD_URL = '{}/endpoint?npiId=1376000000'.format(BASE_URL)


class TestFlaskApi(unittest.TestCase):

    def setUp(self):
        self.backup_items = deepcopy(app.items)  # no references!
        self.app = app.app.test_client()
        self.app.testing = True

    def test_get_provider(self):
        response = self.app.get(PROVIDER_GOOD_URL)  # 1376064311
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['NPI'], 1376064311)

    # def test_item_not_exist(self):
    #     response = self.app.get(BAD_ITEM_URL)
    #     self.assertEqual(response.status_code, 404)
    #
    # def tearDown(self):
    #     # reset app.items to initial state
    #     app.items = self.backup_items


if __name__ == "__main__":
    unittest.main()