import flask
from flask import request
import sqlite3
import json


#######################################################################################
# CONSTANTS #
#######################################################################################
NPI_DB_FILE = 'data/npi.db'
NPI_TABLE_NAME = 'tblNpi'
ENDPOINT_TABLE_NAME = 'tblEndpoint'
NPI_COLUMN_NAME = 'NPI'


app = flask.Flask(__name__)
app.config["DEBUG"] = True


#######################################################################################
# HELPER FUNCTIONS #
#######################################################################################
def query_npi(c, npi_id):
    # you could use 'one' param from stackoverflow to return only 1x result (use this when joining many results)
    c.execute('SELECT * FROM {table} WHERE {column}={npi_id}'.
              format(table=NPI_TABLE_NAME, column=NPI_COLUMN_NAME, npi_id=npi_id))
    query_result = [dict((c.description[i][0], value)
              for i, value in enumerate(row)) for row in c.fetchall()]
    json_output = json.loads(str(query_result[0]).replace("\'", "\""))
    return json_output


def query_endpoint(c, npi_id):
    c.execute('SELECT * FROM {table} WHERE {column}={npi_id}'.
              format(table=ENDPOINT_TABLE_NAME, column=NPI_COLUMN_NAME, npi_id=npi_id))
    query_result = [dict((c.description[i][0], value)
              for i, value in enumerate(row)) for row in c.fetchall()]
    # if len(query_result) == 0:
    #     out = "bad request HTTP error"
    # else:
    out = json.loads(str(query_result[0]).replace("\'", "\""))
    return out

#######################################################################################
# API ENDPOINTS #
#######################################################################################
@app.route('/npi-api/v1.0/', methods=['GET'])
def home():
    return "<h1>NPI Data Web Interface</h1><p>This site is a prototype API that enables users to access NPI data.</p>"


@app.route('/npi-api/v1.0/provider', methods=['GET'])
def provider():
    conn = sqlite3.connect(NPI_DB_FILE)
    cur = conn.cursor()

    npi_to_query = request.args.get('npiId')
    json_response = query_npi(cur, npi_to_query)
    conn.close()
    return str(json_response)


@app.route('/npi-api/v1.0/endpoint', methods=['GET'])
def endpoint():
    conn = sqlite3.connect(NPI_DB_FILE)
    cur = conn.cursor()

    npi_to_query = request.args.get('npiId')
    json_response = query_endpoint(cur, npi_to_query)
    conn.close()
    return str(json_response)


#######################################################################################
# MAIN #
#######################################################################################
app.run()  # http://127.0.0.1:5000/api/v1.0/provider?npiId=1376000000
# conn = sqlite3.connect(NPI_DB_FILE)
# cur = conn.cursor()
# # 1376064311 # good
# # 1376000000 # bad
# resp = query_endpoint(cur, 1376000000)
# print(resp)
# conn.close()
