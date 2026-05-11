CMC Index
Method: GET
URL: /pro-api-reference/cmc-index
Description: Retrieve CoinMarketCap Index.
Parameters: None
CURL Example: curl -X GET 'https://pro-api.coinmarketcap.com/v1/cmc-index'
JSON Response Example:
{
    "data": [
        {
            "label": "CoinMarketCap 100 Index Historical",
            "to": "/pro-api-reference/cmc-index#coinmarketcap-100-index-historical"
        },
        {
            "label": "CoinMarketCap 100 Index Latest",
            "to": "/pro-api-reference/cmc-index#coinmarketcap-100-index-latest"
        },
        ...
    ]
}