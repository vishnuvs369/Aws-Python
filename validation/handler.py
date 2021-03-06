import os
import json
import boto3
import urllib
from jsonschema import validate
from jsonschema import exceptions

clientname=boto3.client('s3')

mySchema = {
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
        validate(instance=jsonData, schema=mySchema)
    except mySchema.exceptions.ValidationError as err:
        return False
    return True

    
def lambda_handler(event, context):
    bucket = 'initial369'
    key = event['Records'][0]['s3']['object']['key']
    key = urllib.parse.unquote_plus(key, encoding='utf-8')
    
    message = 'hey this file got uploaded ' + key + ' to this bucket' + bucket
    print (message)
    
    response = clientname.get_object(Bucket=bucket,Key=key)
    contents = response["Body"].read().decode()
    contents = json.loads(contents)

    isValid = validateJson(contents)
    if isValid:
        print(contents)
        print("Given JSON data is Valid")
        print("these are the contents of the file : \n" , contents)
    else:
        print(contents)
        print("Given JSON data is InValid")
        
    
    try:
        response = clientname.list_objects(
            Bucket=bucket,
            MaxKeys=5
        )
        

        for record in response['Contents']:
            key = record['Key']
            copy_source = {
                'Bucket': bucket,
                'Key': key
            }
            try:
                destbucket = clientname.Bucket('final369')
                destbucket.copy(copy_source, key)
                print('{} transferred to destination bucket'.format(key))

            except Exception as e:
                print(e)
                print('Error getting object {} from bucket {}. '.format(key, bucket))
                raise e
    except Exception as e:
        print(e)
        raise e