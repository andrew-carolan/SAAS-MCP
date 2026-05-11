get /exchange/listings/latest
Get an updated list of active listings for the exchange.
Parameters:
- Symbol (string): The cryptocurrency symbol to filter listings by.

Example CURL Request:
curl -X GET 'https://api.coinmarketcap.com/v1/exchange/listings/latest?symbol=BTCUSDT'

Example JSON Response:
{
    "data": [
        {
            "id": 123456,
            "symbol": "BTCUSDT",
            "name": "Bitcoin USDT",
            "is_active": true
        }
    ]
}