import json
import boto3
import urllib3

REGION = "us-east-1"
SECRET_NAME = "mygithubkey"
API_URL = "https://api.github.com/************"


def lambda_handler(event, context):
  
  http = urllib3.PoolManager()
  api_key = get_api_key()
  response = http.request('GET', f"{API_URL}", headers=api_key)

  if response.status != 200:
    return {
      "statusCode": response.status,
      "errorMessage": "Could not retreive data"
    }
  

  return {
        'statusCode': 200,
        'body': response.data.decode('utf8')
    }


def get_api_key():
  session = boto3.session.Session()
  client = session.client(
      service_name='secretsmanager',
      region_name=REGION
  )
  get_secret_value_response = client.get_secret_value(
      SecretId=SECRET_NAME
  )
  secrets_response = get_secret_value_response['SecretString']

  return json.loads(secrets_response)