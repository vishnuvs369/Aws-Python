import json
import boto3
import urllib
from jsonschema import validate
from jsonschema import exceptions


s3 = boto3.resource('s3')
clientname=boto3.client('s3')
client = boto3.client('stepfunctions')

mySchema = {
    "type": "object",
    "properties": {
        "name":  {"type": "string"},
        "age":   {"type": "number"},
        "TransactionType": {
                   "type": "string",
                   "enum": [ "REQUEST", "RESPONSE", "FAIL" ]
           },
    },
}

def validateJson(jsonData):
    try:
        validate(instance=jsonData, schema=mySchema)
    except mySchema.exceptions.ValidationError as err:
        return False
    return True

    
def lambda_handler(event, context):
    bucket = 'initialbucket369'
    key = event['Records'][0]['s3']['object']['key']
    key = urllib.parse.unquote_plus(key, encoding='utf-8')
    
    message = 'hey this file got uploaded ' + key + ' to this bucket' + bucket
    print (message)
    
    response = clientname.get_object(Bucket=bucket,Key=key)
    contents = response["Body"].read().decode()
    contents = json.loads(contents)
    response = client.start_execution(
		stateMachineArn='arn:aws:states:us-east-1:151977413327:stateMachine:MyStateMachine',
		input=json.dumps(contents)	
		)

    isValid = validateJson(contents)
    if isValid:
        print(contents)
        print("Given JSON data is Valid")
        print("these are the contents of the file : \n" , contents)
    else:
        print(contents)
        print("Given JSON data is InValid")
        
    
    