import json
import boto3

sqs = boto3.client('sqs')

def lambda_handler(event, context):
    print('The event is: ', event)
    print('The type of event is: ', type(event))
    
    try:
        sqs.send_message(QueueUrl = 'https://sqs.us-east-1.amazonaws.com/100163808729/ProductVisitsDataQueue', MessageBody = json.dumps(event))
        print('Message sent to SQS queue successfully')
    except Exception as e:
        print('Message delivery to SQS queue has failed with exception ', e)
