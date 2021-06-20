import json
import boto3

def handler(event, context):
    # TODO implement
    conn = boto3.resource('dynamodb')
    table = conn.Table("datetime1")
    

    table.put_item(
       Item={
            'Hittime' : event['requestContext']['requestTime']
            }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Your Hittime Entry is successfully written to Dynamo DB Version 4 with Hassan '),
        #'body': json.dumps(event)
    }
