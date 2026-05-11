get-exchange
URL: https://pro-api.coinmarketcap.com/v1/exchange/latest
Description: Get the latest data for a specific exchange.
Parameters:
  - id (string): The ID of the exchange to retrieve.
    CURL Example: `curl 'https://pro-api.coinmarketcap.com/v1/exchange/latest?id=67890'`
    JSON Response Example: `{ "data": { "id": "67890", ... } }`