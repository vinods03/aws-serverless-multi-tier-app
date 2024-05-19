import json
import boto3
import csv
s3 = boto3.client('s3')

def lambda_handler(event, context):
    print('The event is: ', event)
    for record in event['Records']:
        print('The record is: ', record)
        print('The record event is: ', record['eventName'])
        
        if record['eventName'] == 'INSERT':
        
            print('The data we need is: ', record['dynamodb']['NewImage'])
            product_visit_key = record['dynamodb']['NewImage']['ProductVisitKey']['S']
            customer_id = record['dynamodb']['NewImage']['customer_id']['S']
            customer_name = record['dynamodb']['NewImage']['customer_name']['S']
            product_id = record['dynamodb']['NewImage']['product_id']['S']
            product_name = record['dynamodb']['NewImage']['product_name']['S']
            category = record['dynamodb']['NewImage']['category']['S']
            price_per_unit = record['dynamodb']['NewImage']['price_per_unit']['S']
            time_of_visit = record['dynamodb']['NewImage']['time_of_visit']['S']
            
            year = time_of_visit.split('T')[0][0:4]
            month = time_of_visit.split('T')[0][5:7]
            day = time_of_visit.split('T')[0][8:10]
            hour = time_of_visit.split('T')[1][0:2]
            
            print('product_visit_key: ', product_visit_key)
            print('customer_id: ', customer_id)
            print('customer_name: ', customer_name)
            print('product_id: ', product_id)
            print('product_name: ', product_name)
            print('category: ', category)
            print('price_per_unit: ', price_per_unit)
            print('time_of_visit: ', time_of_visit)
            
            print('year: ', year)
            print('month: ', month)
            print('day: ', day)
            print('hour: ', hour)
            
            field_names = ['product_visit_key', 'customer_id', 'customer_name', 'product_id', 'product_name', 'category', 'price_per_unit', 'time_of_visit']
            row_of_data = [product_visit_key, customer_id, customer_name, product_id, product_name, category, price_per_unit, time_of_visit]
            s3_key_prefix = 'data/' + year + '/' +  month + '/' +  day + '/' +  hour + '/' + product_visit_key
            
            print('s3_key_prefix is: ', s3_key_prefix)
            
            temp_file = '/tmp/temp_file.csv'
            
            with open(temp_file, 'w') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(field_names)
                csvwriter.writerow(row_of_data)
            
            try:
                s3.upload_file(temp_file, 'product-visits-datalake-vinod', s3_key_prefix)
                print('Upload into S3 bucket successful')
            except Exception as e:
                print('Upload into S3 bucket failed with exception ', e)
                
        else:
            print('Nothing to add in data lake')
                
    
            
        