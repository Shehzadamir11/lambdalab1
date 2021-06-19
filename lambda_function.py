import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    conn = boto3.resource('dynamodb')
    table = conn.Table("datetime")
    

    table.put_item(
       Item={
            'Hittime' : event['requestContext']['requestTime']
            }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Serverless API via github third try to see the difference and is it still working fine '),
        #'body': json.dumps(event)
    }
