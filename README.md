# Multi-Agent Stock Analysis Workflow

## Overview

This project automates the process of analyzing the top 10 performing stocks over a 3-month period using AWS services. It uses multiple Lambda functions for fetching, saving, and analyzing stock data. AWS Step Functions orchestrate the process, and EventBridge schedules the workflow every 5 days.

## Repository Structure

```bash
multi-agent-stock-analysis/
│
├── lambda_functions/
│   ├── stock_search_agent.py            # Lambda function for searching top stocks
│   ├── data_fetching_agent.py           # Lambda function for fetching stock data
│   ├── data_saving_agent.py             # Lambda function for saving data to S3
│   ├── data_analysis_agent.py           # Lambda function for analyzing stock performance
│   ├── store_performance_dynamodb.py    # Lambda function for storing analysis in DynamoDB
│
├── step_functions/
│   └── step_functions.json              # Step Functions state machine definition
│
├── eventbridge/
│   └── eventbridge_cron_rule.txt        # EventBridge cron expression for scheduling the workflow
│
├── requirements.txt                     # Python dependencies for the Lambda functions
├── README.md                            # Project overview, setup, and instructions
└── .gitignore
```

## Lambda Functions

1. **Stock Search Agent** (`lambda_functions/stock_search_agent.py`):
   - Searches for the top 10 performing stocks.

2. **Data Fetching Agent** (`lambda_functions/data_fetching_agent.py`):
   - Fetches historical stock data from Yahoo Finance.

3. **Data Saving Agent** (`lambda_functions/data_saving_agent.py`):
   - Saves stock data to an S3 bucket as CSV.

4. **Data Analysis Agent** (`lambda_functions/data_analysis_agent.py`):
   - Analyzes stock performance and determines the top-performing stock.

5. **Store Performance in DynamoDB** (`lambda_functions/store_performance_dynamodb.py`):
   - Stores the final stock performance report in a DynamoDB table.

## Step Functions

- The Step Functions workflow is defined in `step_functions/step_functions.json`.

## EventBridge

- The workflow is scheduled to run every 5 days using the cron expression defined in `eventbridge/eventbridge_cron_rule.txt`.

## Setup Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-repo-url/multi-agent-stock-analysis.git
cd multi-agent-stock-analysis
```
### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Deploy Lambda Functions

- Upload the Lambda functions to AWS and configure the appropriate IAM roles for accessing S3, DynamoDB, and other AWS services.

### Step 4: Set Up Step Functions

- Use the Step Functions JSON file to create the state machine in AWS Step Functions.

### Step 5: Schedule with EventBridge

- Set up an EventBridge rule using the cron expression provided to schedule the workflow every 5 days.

#### **6. `.gitignore`**

Add a `.gitignore` file to prevent unnecessary files from being uploaded to the repository.

```txt
# Ignore Python cache and virtual environments
__pycache__/
*.pyc
.venv/
env/