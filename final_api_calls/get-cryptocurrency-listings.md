get-cryptocurrency-listings
URL: https://pro-api.coinmarketcap.com/v1/cryptocurrency/{id}/listings/latest
Description: Get the latest listings for a specific cryptocurrency.
Parameters:
  - id (string): The ID of the cryptocurrency to retrieve.
    CURL Example: `curl 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/12345/listings/latest'`
    JSON Response Example: `{ "data": { ... } }`