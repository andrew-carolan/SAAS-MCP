get /exchange/market-pairs/latest
Get an updated list of active market pairs for the exchange.
Parameters:
- Symbol (string): The cryptocurrency symbol to filter market pairs by.

Example CURL Request:
curl -X GET 'https://api.coinmarketcap.com/v1/exchange/market-pairs/latest?symbol=ETHUSDT'

Example JSON Response:
{
    "data": [
        {
            "id": 123456,
            "symbol": "ETHUSDT",
            "name": "Ethereum USDT",
            "is_active": true
        }
    ]
}