import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('expenses')

def lambda_handler(event, context):
    try:
        expense_id = event['pathParameters']['id']
        
        table.delete_item(Key={'id': expense_id})
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'message': f'Expense {expense_id} deleted successfully'
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
