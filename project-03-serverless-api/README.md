# Project 3: Serverless REST API — Budget Tracker 💰

## Architecture
Client → API Gateway (REST) → Lambda (Python 3.12) → DynamoDB

## API Endpoints

| Method | Path | Function | Description |
|--------|------|----------|-------------|
| POST | /expenses | createExpense | Add a new expense |
| GET | /expenses | getExpenses | List all expenses |
| DELETE | /expenses/{id} | deleteExpense | Remove an expense by ID |

## Services Used

| Service | Purpose | Cost |
|---------|---------|------|
| API Gateway | REST API endpoints | Free tier: 1M calls/month |
| Lambda | Business logic (Python 3.12) | Free tier: 1M invocations/month |
| DynamoDB | NoSQL database (on-demand) | Free tier: 25GB storage |
| IAM | Execution roles | Free |

## DynamoDB Table Design

- **Table name:** expenses
- **Partition key:** id (String)
- **Billing mode:** PAY_PER_REQUEST (on-demand)

## Sample Request (POST /expenses)

```json
{
    "description": "Monthly internet bill",
    "amount": 15000,
    "category": "Utilities",
    "date": "2026-06-01"
}

{
    "message": "Expense created successfully",
    "expense": {
        "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "description": "Monthly internet bill",
        "amount": "15000",
        "category": "Utilities",
        "date": "2026-06-01",
        "createdAt": "2026-06-06T14:30:00.000000"
    }
}

Key Concepts Learned
Serverless architecture — no servers to manage, auto-scales
Lambda proxy integration — passes full HTTP request to function
IAM least privilege — Lambda only has DynamoDB access
HTTP status codes — 200 (OK), 201 (Created), 500 (Error)
CORS — allowing cross-origin browser requests
JSON as data exchange format between services
Finance Analogy
Lambda = variable costing — pay only per invocation ($0.0000002/request). No usage = $0. This is the opposite of EC2 (fixed cost — pay even when idle).

DynamoDB on-demand = flexible budgeting — capacity adjusts to actual activity. Provisioned = fixed budgeting — set in advance regardless of actual usage.

How to Deploy
Create DynamoDB table (expenses, partition key: id)
Create 3 Lambda functions (code in /lambda folder)
Attach AmazonDynamoDBFullAccess to each Lambda role
Create API Gateway REST API
Create /expenses resource + POST & GET methods
Create /expenses/{id} resource + DELETE method
Enable Lambda proxy integration on all methods
Deploy API to 'prod' stage
