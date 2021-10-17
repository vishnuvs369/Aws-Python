import json
import boto3


client = boto3.client('stepfunctions')

def lambda_handler(event, context):
	
	input = {'TransactionType': 'REQUEST'}

	response = client.start_execution(
		stateMachineArn='Your state machine ARN',
		input=json.dumps(input)	
		)