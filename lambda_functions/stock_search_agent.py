import requests
import json

def search_top_stocks():
    # In a production scenario, we might use a stock API to fetch the top 10 performing stocks
    # For this example, we return a mock list of stock tickers
    stock_tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'FB', 'NVDA', 'NFLX', 'ADBE', 'PYPL']
    
    return {
        'statusCode': 200,
        'body': json.dumps(stock_tickers)
    }

# Example invocation
if __name__ == "__main__":
    result = search_top_stocks()
    print(result)