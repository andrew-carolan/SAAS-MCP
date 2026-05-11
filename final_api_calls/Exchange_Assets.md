GET /__zuplo/docs/exchange
The `exchange-assets` query returns exchange asset information.

Parameters:
- None

CURL Example:
curl -X GET 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false'

JSON Response Example:
{
    "data": [
        {
            "id": "bitcoin",
            "symbol": "btc",
            "name": "Bitcoin",
            ...
        }
    ]
}