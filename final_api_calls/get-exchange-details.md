get-exchange-details
URL: https://pro-api.coinmarketcap.com/v1/exchange/{id}
Description: Get detailed information about a specific exchange.
Parameters:
  - id (string): The ID of the exchange to retrieve.
    CURL Example: `curl 'https://pro-api.coinmarketcap.com/v1/exchange/67890'`
    JSON Response Example: `{ "data": { "id": "67890", ... } }`