Get Top Gainers and Losers
Method: POST
URL: /pro-api-reference/token/get-top-gainers-and-losers
Description: Retrieve top gainers and losers.
Parameters: None
CURL Example: curl -X POST 'https://pro-api.coinmarketcap.com/v1/token/get-top-gainers-and-losers' -H "Content-Type: application/json" -d '{"query": {"top_gainers": 10, "top_losers": 5}}'
JSON Response Example:
{
    "data": [
        {
            "label": "Get top gainers and losers",
            "to": "/pro-api-reference/token#get-top-gainers-and-losers"
        }
    ]
}