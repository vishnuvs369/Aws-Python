import json


def hello(event, context):
    body = {
        "message": "This is My Serverless lambda successfully executed!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    