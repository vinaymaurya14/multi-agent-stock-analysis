import pandas as pd
import json

def analyze_stock_performance(event, context):
    stock_data = json.loads(event['body'])  # Receive stock data
    
    performance_report = {}
    for ticker, data in stock_data.items():
        df = pd.DataFrame(data)
        df['Normalized'] = df['Close'].pct_change() * 100
        total_change = (df['Close'].iloc[-1] - df['Close'].iloc[0]) / df['Close'].iloc[0] * 100
        performance_report[ticker] = total_change

    best_performer = max(performance_report, key=performance_report.get)
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'best_performer': best_performer,
            'performance': performance_report[best_performer]
        })
    }

# Example invocation
if __name__ == "__main__":
    event = {
        'body': json.dumps({
            'AAPL': {'Close': [150.0, 160.0, 155.0]},
            'MSFT': {'Close': [200.0, 210.0, 215.0]}
        })
    }
    result = analyze_stock_performance(event, None)
    print(result)