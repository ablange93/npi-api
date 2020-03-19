from api import app
from flask import json


def test_add():
    response = app.test_client().get(
        'http://127.0.0.1:5000/npi-api/v1.0/provider?npiId=1376064311',
    )
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['NPI'] == 1376064311
