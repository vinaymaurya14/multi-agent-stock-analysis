import boto3
import json
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StockPerformanceReports')

def store_in_dynamodb(event, context):
    data = json.loads(event['body'])  # Receive best performer and performance
    best_performer = data['best_performer']
    performance = data['performance']

    table.put_item(
        Item={
            'StockTicker': best_performer,
            'Date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'Performance': performance
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Performance report saved successfully.')
    }

# Example invocation
if __name__ == "__main__":
    event = {
        'body': json.dumps({'best_performer': 'AAPL', 'performance': 10.5})
    }
    result = store_in_dynamodb(event, None)
    print(result)