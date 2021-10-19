from __future__ import print_function

import json
import urllib
import boto3
import datetime



s3 = boto3.resource('s3')
clientname=boto3.client('s3')

def lambda_handler(message,context):
    bucket = 'initialbucket369'
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
                destbucket = s3.Bucket('finalbucket369')
                destbucket.copy(copy_source, key)
                print('{} transferred to destination bucket'.format(key))

            except Exception as e:
                print(e)
                print('Error getting object {} from bucket {}. '.format(key, bucket))
                raise e
    except Exception as e:
        print(e)
        raise e


        #1. Log input message
    print('Received message from Step Function:')
    print(message)
    
    #2. Construct response
    response = {}
    response['TransactionType'] = message['TransactionType']
    response['Timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    response['Message'] = 'Hello from Process Request!'
    
    #3. Return response
    print(response)
    
    return (response)