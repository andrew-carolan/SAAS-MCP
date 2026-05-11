Dex API Token
Method: POST
URL: /pro-api-reference/token/batch-query-tokens
Description: Retrieve batch query tokens.
Parameters: None
CURL Example: curl -X POST 'https://pro-api.coinmarketcap.com/v1/token/batch-query-tokens' -H "Content-Type: application/json" -d '{"query": ["token 1", "token 2", ...]}'
JSON Response Example:
{
    "data": [
        {
            "label": "Batch query tokens",
            "to": "/pro-api-reference/token#batch-query-tokens"
        }
    ]
}