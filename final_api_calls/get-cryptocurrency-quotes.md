get-cryptocurrency-quotes
URL: https://pro-api.coinmarketcap.com/v1/cryptocurrency/{id}/quotes/latest
Description: Get the latest quotes for a specific cryptocurrency.
Parameters:
  - id (string): The ID of the cryptocurrency to retrieve.
    CURL Example: `curl 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/12345/quotes/latest'`
    JSON Response Example: `{ "data": { ... } }`