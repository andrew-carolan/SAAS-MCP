# GET /v4/dex/networks/list

**Summary:** CoinMarketCap ID Map

**Description:** Returns a list of all networks to unique CoinMarketCap ids.Per our Best Practices we recommend utilizing CMC ID instead of network symbols to securely identify networks with our other endpoints and in your own application logic. Each network returned includes typical identifiers such as name, symbol, and token_address for flexible mapping to id.

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **start** (query) - *Optional*: Optionally offset the start (1-based index) of the paginated list of items to return.
- **limit** (query) - *Optional*: Optionally specify the number of results to return. Use this parameter and the 
"start" parameter to determine your own pagination size.
- **sort** (query) - *Optional*: Default:`"id"`
Valid values: `"id"` `"name"`
What field to sort the list of networks by.
- **sort_dir** (query) - *Optional*: Default:`"desc"`
Valid values: `"desc"` `"asc"`
The direction in which to order networks against the specified sort.
- **aux** (query) - *Optional*: Default:`""`
Valid values: `"alternativeName"` `"cryptocurrencyId"` `"cryptocurrenySlug"` `"wrappedTokenId"` `"wrappedTokenSlug"` `"tokenExplorerUrl"` `"poolExplorerUrl"` `"transactionHashUrl"`
Optionally specify a comma-separated list of supplemental data fields to return.

### Raw Data

```json
{
  "slug": "coinmarketcap-id-map-3",
  "summary": "CoinMarketCap ID Map",
  "method": "get",
  "description": "Returns a list of all networks to unique CoinMarketCap ids.Per our Best Practices we recommend utilizing CMC ID instead of network symbols to securely identify networks with our other endpoints and in your own application logic. Each network returned includes typical identifiers such as name, symbol, and token_address for flexible mapping to id.",
  "operationId": "getNetworks",
  "contentTypes": [],
  "path": "/v4/dex/networks/list",
  "deprecated": null,
  "extensions": {},
  "servers": [
    {
      "url": "https://pro-api.coinmarketcap.com",
      "description": null
    }
  ],
  "parameters": [
    {
      "name": "X-CMC_PRO_API_KEY",
      "in": "header",
      "description": "Your CoinMarketCap Pro API key",
      "required": true,
      "schema": {
        "type": "string",
        "default": "YOUR_API_KEY"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "start",
      "in": "query",
      "description": "Optionally offset the start (1-based index) of the paginated list of items to return.",
      "required": false,
      "schema": {
        "type": "string",
        "default": "1"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "limit",
      "in": "query",
      "description": "Optionally specify the number of results to return. Use this parameter and the \n\"start\" parameter to determine your own pagination size.",
      "required": false,
      "schema": {
        "type": "string",
        "default": "50"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "sort",
      "in": "query",
      "description": "Default:`\"id\"`\nValid values: `\"id\"` `\"name\"`\nWhat field to sort the list of networks by.",
      "required": false,
      "schema": {
        "type": "string",
        "default": "id"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "sort_dir",
      "in": "query",
      "description": "Default:`\"desc\"`\nValid values: `\"desc\"` `\"asc\"`\nThe direction in which to order networks against the specified sort.",
      "required": false,
      "schema": {
        "type": "string",
        "default": "desc"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "aux",
      "in": "query",
      "description": "Default:`\"\"`\nValid values: `\"alternativeName\"` `\"cryptocurrencyId\"` `\"cryptocurrenySlug\"` `\"wrappedTokenId\"` `\"wrappedTokenSlug\"` `\"tokenExplorerUrl\"` `\"poolExplorerUrl\"` `\"transactionHashUrl\"`\nOptionally specify a comma-separated list of supplemental data fields to return.",
      "required": false,
      "schema": {
        "type": "string"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    }
  ],
  "security": [
    {
      "schemes": [
        {
          "scopes": [],
          "scheme": {
            "name": "ApiKeyAuth",
            "type": "apiKey",
            "description": "Your CoinMarketCap Pro API key. Get one at https://pro.coinmarketcap.com/signup",
            "in": "header",
            "paramName": "X-CMC_PRO_API_KEY",
            "scheme": null,
            "bearerFormat": null,
            "openIdConnectUrl": null,
            "flows": null
          }
        }
      ]
    }
  ],
  "requestBody": {
    "content": [],
    "description": null,
    "required": null
  },
  "responses": [
    {
      "statusCode": "200",
      "links": null,
      "description": "OK",
      "content": [
        {
          "examples": [],
          "mediaType": "application/json",
          "encoding": null,
          "schema": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer",
                  "description": "The unique CoinMarketCap ID for this network.",
                  "format": "int32"
                },
                "name": {
                  "type": "string",
                  "description": "The name of this network."
                },
                "alternativeName": {
                  "type": "string",
                  "description": "The alternate name for this network."
                },
                "cryptocurrencyId": {
                  "type": "string",
                  "description": "The unique CoinMarketCap identifier for the cryptocurrency associated with this network."
                },
                "cryptocurrencySlug": {
                  "type": "string",
                  "description": "The slug(URL-friendly name) for the associated cryptocurrency"
                },
                "wrappedTokenId": {
                  "type": "string",
                  "description": "The unique identifier for the wrapped token on this network."
                },
                "wrappedTokenSlug": {
                  "type": "string",
                  "description": "The slug(URL-friendly name) for the wrapped token on this network."
                },
                "tokenExplorerUrl": {
                  "type": "string",
                  "description": "The URL for exploring tokens on this network."
                },
                "poolExplorerUrl": {
                  "type": "string",
                  "description": "The URL for exploring liquidity pools on this network."
                },
                "transactionHashUrl": {
                  "type": "string",
                  "description": "The URL for exploring transaction hashes on this network."
                },
                "network_slug": {
                  "type": "string",
                  "description": "The slug of the network the spot pair is on."
                }
              },
              "__$ref": "#/components/schemas/NetworkInfoDTO"
            }
          }
        }
      ]
    }
  ]
}
```
