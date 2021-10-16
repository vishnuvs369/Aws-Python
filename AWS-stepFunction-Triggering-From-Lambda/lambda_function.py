import json
import boto3
import uuid

client = boto3.client('stepfunctions')

def lambda_handler(event, context):
	#INPUT -> { "TransactionId": "foo", "Type": "PURCHASE"}
	transactionId = str(uuid.uuid1()) #90a0fce-sfhj45-fdsfsjh4-f23f

	input = {'TransactionType': 'REQUEST'}

	response = client.start_execution(
		stateMachineArn='Your state machine ARN',
		name=transactionId,
		input=json.dumps(input)	
		)