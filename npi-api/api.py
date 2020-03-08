import flask
from flask import request
import sqlite3
import json


#######################################################################################
# CONSTANTS #
#######################################################################################
NPI_DB_FILE = 'data/npi.db'
NPI_TABLE_NAME = 'tblNpi'
NPI_COLUMN_NAME = 'NPI'


app = flask.Flask(__name__)
app.config["DEBUG"] = True


#######################################################################################
# HELPER FUNCTIONS #
#######################################################################################
def query_npi_id(c, npi_id):
    # you could use 'one' param from stackoverflow to return only 1x result (use this when joining many results)
    c.execute('SELECT * FROM {table} WHERE {column}={npi_id}'.
              format(table=NPI_TABLE_NAME, column=NPI_COLUMN_NAME, npi_id=npi_id))
    query_result = [dict((c.description[i][0], value)
              for i, value in enumerate(row)) for row in c.fetchall()]
    json_output = json.loads(str(query_result[0]).replace("\'", "\""))
    return json_output


#######################################################################################
# API ENDPOINTS #
#######################################################################################
# @app.route('/', methods=['GET'])
# def home():
#     return "<h1>NPI Data Web Interface</h1><p>This site is a prototype API that enables users to access NPI data.</p>"


@app.route('/api/v1.0/provider', methods=['GET'])
def query_example():
    conn = sqlite3.connect(NPI_DB_FILE)
    cur = conn.cursor()

    npi_to_query = request.args.get('npiId')
    json_response = query_npi_id(cur, npi_to_query)

    npi = json_response['NPI']
    type_code = json_response['EntityTypeCode']
    provider_business_name = json_response['ProviderOrganizationNameLegalBusinessName']
    provider_address = json_response['ProviderFirstLineBusinessMailingAddress']
    provider_state = json_response['ProviderBusinessMailingAddressStateName']
    return '''<h3>NPI: {}</h3>
              <h3>EntityTypeCode: {}</h1>
              <h3>ProviderOrganizationNameLegalBusinessName: {}</h1>
              <h3>ProviderFirstLineBusinessMailingAddress: {}</h1>
              <h3>ProviderBusinessMailingAddressStateName: {}</h1>'''.format(npi,
                                                                             type_code,
                                                                             provider_business_name,
                                                                             provider_address,
                                                                             provider_state)


#######################################################################################
# MAIN #
#######################################################################################
app.run()  # http://127.0.0.1:5000/api/v1.0/provider?npiId=1003022070
