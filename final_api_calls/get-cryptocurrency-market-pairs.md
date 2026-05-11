get-cryptocurrency-market-pairs
URL: https://pro-api.coinmarketcap.com/v1/cryptocurrency/{id}/market-pairs/latest
Description: Get the latest market pairs for a specific cryptocurrency.
Parameters:
  - id (string): The ID of the cryptocurrency to retrieve.
    CURL Example: `curl 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/12345/market-pairs/latest'`
    JSON Response Example: `{ "data": { ... } }`