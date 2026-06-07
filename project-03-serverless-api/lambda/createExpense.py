import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('expenses')

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        
        item = {
            'id': str(uuid.uuid4()),
            'description': body.get('description', 'No description'),
            'amount': str(body.get('amount', 0)),
            'category': body.get('category', 'General'),
            'date': body.get('date', datetime.now().strftime('%Y-%m-%d')),
            'createdAt': datetime.now().isoformat()
        }
        
        table.put_item(Item=item)
        
        return {
            'statusCode': 201,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'message': 'Expense created successfully',
                'expense': item
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
