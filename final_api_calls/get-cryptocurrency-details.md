get-cryptocurrency-details
URL: https://pro-api.coinmarketcap.com/v1/cryptocurrency/{id}
Description: Get detailed information about a specific cryptocurrency.
Parameters:
  - id (string): The ID of the cryptocurrency to retrieve.
    CURL Example: `curl 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/12345'`
    JSON Response Example: `{ "data": { "id": "12345", ... } }`