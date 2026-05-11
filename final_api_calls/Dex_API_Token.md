Dex API Token
Method: POST
URL: /pro-api-reference/token
Description: Retrieve trending tokens.
Parameters: None
CURL Example: curl -X POST 'https://pro-api.coinmarketcap.com/v1/token' -H "Content-Type: application/json" -d '{"query": "trending tokens"}'
JSON Response Example:
{
    "data": [
        {
            "label": "Get trending tokens",
            "to": "/pro-api-reference/token#get-trending-tokens"
        }
    ]
}