npi_type='2'
state='OR'
zip_code='977031970'

param_map = {
    npi_type: "EntityTypeCode",
    state: "ProviderBusinessMailingAddressStateName",
    zip_code: "ProviderBusinessMailingAddressPostalCode"
}

# dynamically assemble query based on qty of params
query_string = "SELECT * from tblNpi WHERE "
for param in param_map.keys():
    if param is not None:
        query_string += str(param_map[param]) + " = '" + str(param) + "' AND "
query_string = query_string[:-5] + ";"
print(query_string)
