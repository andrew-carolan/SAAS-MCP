get-cryptocurrency
URL: https://pro-api.coinmarketcap.com/v1/cryptocurrency/latest
Description: Get the latest data for a specific cryptocurrency.
Parameters:
  - id (string): The ID of the cryptocurrency to retrieve.
    CURL Example: `curl 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/latest?id=12345'`
    JSON Response Example: `{ "data": { "id": "12345", ... } }`