get /exchange/quotes/historical
Get the historical quotes for a specific cryptocurrency.
Parameters:
- Symbol (string): The cryptocurrency symbol to filter by.

Example CURL Request:
curl -X GET 'https://api.coinmarketcap.com/v1/exchange/quotes/historical?symbol=BTCUSDT'

Example JSON Response:
{
    "data": [
        {
            "id": 123456,
            "symbol": "BTCUSDT",
            "time": "2022-01-01T00:00:00Z",
            "open": 12345.67,
            "high": 12346.78,
            "low": 12344.99,
            "close": 12345.56
        }
    ]
}