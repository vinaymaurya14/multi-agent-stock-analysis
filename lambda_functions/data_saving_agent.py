import boto3
import pandas as pd
from io import StringIO
import json

s3_client = boto3.client('s3')

def save_to_s3(event, context):
    stock_data = json.loads(event['body'])  # Get stock data
    bucket_name = 'your-s3-bucket-name'
    
    for ticker, data in stock_data.items():
        df = pd.DataFrame(data)
        csv_buffer = StringIO()
        df.to_csv(csv_buffer)
        
        # Save CSV to S3
        s3_client.put_object(
            Bucket=bucket_name, 
            Key=f'{ticker}_stock_data.csv',
            Body=csv_buffer.getvalue()
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Stock data saved successfully.')
    }

# Example invocation
if __name__ == "__main__":
    event = {
        'body': json.dumps({'AAPL': {'Date': ['2023-10-01'], 'Close': [150.0]}})
    }
    result = save_to_s3(event, None)
    print(result)