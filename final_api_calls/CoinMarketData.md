CoinMarketCap Market Data
GET /pro-api-reference/market-data
Description: Retrieve market data for cryptocurrency coins and other relevant information.
Parameters:
- symbol (string): The symbol of the coin (e.g., BTC-USD)
- limit (integer): The number of results to return (default is 10)
- start_time (integer): The Unix timestamp from which to begin retrieving historical price data
- end_time (integer): The Unix timestamp up to which to retrieve historical price data
JSON Response Example:
```json
{
  "symbol": "BTC-USD",
  "timestamp": 1643723400,
  "last_price_usd": 12345.67,
  "volume_usd_24h": 10000000,
  ...
}
```