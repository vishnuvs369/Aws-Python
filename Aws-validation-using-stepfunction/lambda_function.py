import os
import json
import boto3
import urllib

my_state_machine_arn = os.environ['MY_STATE_MACHINE_ARN']
client = boto3.client('stepfunctions')
clientname=boto3.client('s3')


def handler(event, context):
    print(event)
    for record in event['Records']:
        response = client.start_execution(
            stateMachineArn=my_state_machine_arn,
            input=json.dumps(record['s3'])
        )
        
    bucket = 'source bucket name'
    key = event['Records'][0]['s3']['object']['key']
    key = urllib.parse.unquote_plus(key, encoding='utf-8')
    
    message = 'hey this file got uploaded ' + key + ' to this bucket' + bucket
    print (message)
    
    response = clientname.get_object(Bucket=bucket,Key=key)
    contents = response["Body"].read().decode()
    contents = json.loads(contents)
    print("these are the contents of the file : \n" , contents)
    
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
                destbucket = clientname.Bucket('destination bucket name')
                destbucket.copy(copy_source, key)
                print('{} transferred to destination bucket'.format(key))

            except Exception as e:
                print(e)
                print('Error getting object {} from bucket {}. '.format(key, bucket))
                raise e
    except Exception as e:
        print(e)
        raise e    