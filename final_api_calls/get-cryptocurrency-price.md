get-cryptocurrency-price
URL: https://pro-api.coinmarketcap.com/v1/cryptocurrency/{id}/price
Description: Get the current price for a specific cryptocurrency.
Parameters:
  - id (string): The ID of the cryptocurrency to retrieve.
    CURL Example: `curl 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/12345/price'`
    JSON Response Example: `{ "data": { ... } }`