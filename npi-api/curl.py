import os

tests = """
# provider
curl http://127.0.0.1:5000/npi-api/v1.0/provider?npiId=1376064311
# endpoint
curl http://127.0.0.1:5000/npi-api/v1.0/endpoint?npiId=1376064311
# bad provider
curl http://127.0.0.1:5000/npi-api/v1.0/provider?npiId=1376000000
# bad endpoint
curl http://127.0.0.1:5000/npi-api/v1.0/endpoint?npiId=1376000000


"""

out = list()
for line in tests.strip().split('\n'):
    print('\n{}'.format(line))
    if not line.startswith('#'):
        cmd = line.strip()
        out.append(os.system(cmd))
print(out)
