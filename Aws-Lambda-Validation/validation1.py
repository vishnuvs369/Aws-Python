import json
from jsonschema import validate
from jsonschema import exceptions

# Describe what kind of json you expect.
studentSchema = {
    "type": "object",
    "properties": {
        "name":  {"type": "string"},
        "age":   {"type": "number"},
        "type": {
                   "type": "string",
                   "enum": [ "Req", "Resp", "Fail" ]
           },
    },
}

def validateJson(jsonData):
    try:
        validate(instance=jsonData, schema=studentSchema)
    except exceptions.ValidationError as err:
        return False
    return True

# Convert json to python object.
jsonData = json.loads('{"name": "jane doe", "age": "25", "type" : "Req"}')
# validate it
isValid = validateJson(jsonData)
if isValid:
    print(jsonData)
    print("Given JSON data is Valid")
else:
    print(jsonData)
    print("Given JSON data is InValid")

# Convert json to python object.
jsonData = json.loads('{"name": "jane doe", "age": 25, "type" : "Resp"}')
# validate it
isValid = validateJson(jsonData)
if isValid:
    print(jsonData)
    print("Given JSON data is Valid")
else:
    print(jsonData)
    print("Given JSON data is InValid")