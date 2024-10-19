import yfinance as yf
import json

def fetch_stock_data(event, context):
    stock_tickers = json.loads(event['body'])  # Receive stock tickers as input
    stock_data = {}
    
    for ticker in stock_tickers:
        stock = yf.Ticker(ticker)
        stock_history = stock.history(period='3mo')
        stock_data[ticker] = stock_history.to_dict()

    return {
        'statusCode': 200,
        'body': json.dumps(stock_data)
    }

# Example invocation
if __name__ == "__main__":
    event = {
        'body': json.dumps(['AAPL', 'MSFT', 'GOOGL'])
    }
    result = fetch_stock_data(event, None)
    print(result)