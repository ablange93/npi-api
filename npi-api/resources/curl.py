import os

tests = """
# provider
curl http://127.0.0.1:5000/npi-api/v1.0/provider?npiId=1003022070


# endpoint
curl http://127.0.0.1:5000/npi-api/v1.0/endpoint?npiId=1376064311

# discover provider
curl http://127.0.0.1:5000/npi-api/v1.0/discover_provider?npi_type=1?state=NC?ProviderBusinessMailingAddressPostalCode=282199305


# bad provider
curl http://127.0.0.1:5000/npi-api/v1.0/provider?npiId=199295555


# bad endpoint
curl http://127.0.0.1:5000/npi-api/v1.0/endpoint?npiId=199295555


"""

out = list()
for line in tests.strip().split('\n'):
    print('\n{}'.format(line))
    if not line.startswith('#'):
        cmd = line.strip()
        out.append(os.system(cmd))
print(out)
