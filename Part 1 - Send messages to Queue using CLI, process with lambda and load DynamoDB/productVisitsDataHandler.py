import json
import uuid
import boto3

dynamodb_resource = boto3.resource('dynamodb')
product_visits_table = dynamodb_resource.Table('ProductVisits')

def lambda_handler(event, context):
    print('The event is: ', event)
    for record in event['Records']:
        print('The record is: ', record)
        print('The message body is: ', json.loads(record['body']))
        print('The product id is: ', json.loads(record['body'])['ProductId'])
        
        message_body = json.loads(record['body'])
        
        product_id = message_body['ProductId']
        product_name = message_body['ProductName']
        category = message_body['Category']
        price_per_unit = message_body['PricePerUnit']
        customer_id = message_body['CustomerId']
        customer_name = message_body['CustomerName']
        time_of_visit = message_body['TimeOfVisit']
        ProductVisitKey = str(uuid.uuid4())
        
        item = {'ProductVisitKey': ProductVisitKey, 'product_id': product_id, 'product_name': product_name, 'category': category, 'price_per_unit': price_per_unit, 'customer_id': customer_id, 'customer_name': customer_name, 'time_of_visit': time_of_visit}
        try:
            product_visits_table.put_item(Item = item)
            print('Processed ', ProductVisitKey, ' into the dynamodb Table ProductVisits successfully')
        except Exception as e:
            print('Processing of ', ProductVisitKey, ' into  dynamodb Table ProductVisits has failed with exception ', e)
        
 