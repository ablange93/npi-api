# npi-api

This is a Flask API that can be used to access provider and endpoint information using NPI identifiers.
<br/>https://npiregistry.cms.hhs.gov/
<br/>
<br/>
# Providers
To query provider information, pass in a npiId value using the below API call:<br/>
http://host:port/npi-api/v1.0/provider?npiId=npi-id-goes-here
<br/>
See 'provider_response.json' in resources/ to see what the API response looks like.


# Endpoints
To query endpoint information, pass in a npiId value using the below API call:<br/>
"http://host:port/npi-api/v1.0/endpoint?npiId=<npi-id>"
<br/>
See 'endpoint_response.json' in resources/ to see what the API response looks like.