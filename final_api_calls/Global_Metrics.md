get /global-metrics/quotes/historical
Get the historical quotes for global metrics.
Parameters:
- Metric (string): The metric to filter by.

Example CURL Request:
curl -X GET 'https://api.coinmarketcap.com/v1/global-metrics/quotes/historical?metric=altcoin-season-index'

Example JSON Response:
{
    "data": [
        {
            "id": 123456,
            "symbol": "",
            "time": "2022-01-01T00:00:00Z",
            "open": null,
            "high": null,
            "low": null,
            "close": null
        }
    ]
}