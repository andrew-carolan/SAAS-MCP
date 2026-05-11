# POST /v1/dex/token/price/batch

**Summary:** Batch get token prices

**Description:** Get prices for multiple tokens in one request

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key

### Raw Data

```json
{
  "slug": "batch-get-token-prices",
  "summary": "Batch get token prices",
  "method": "post",
  "description": "Get prices for multiple tokens in one request",
  "operationId": "batchGetTokenPrice",
  "contentTypes": [
    "application/json"
  ],
  "path": "/v1/dex/token/price/batch",
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
    "content": [
      {
        "mediaType": "application/json",
        "encoding": [],
        "examples": [],
        "schema": {
          "type": "object",
          "properties": {
            "tokens": {
              "type": "array",
              "description": "List of platform-address pairs",
              "items": {
                "type": "object",
                "properties": {
                  "platform": {
                    "type": "string"
                  },
                  "address": {
                    "type": "string"
                  }
                },
                "description": "List of platform-address pairs",
                "__$ref": "#/components/schemas/PlatformAddress"
              }
            }
          },
          "description": "Batch price query request",
          "__$ref": "#/components/schemas/DqueryBatchPriceRequestDTO"
        }
      }
    ],
    "description": null,
    "required": true
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
                "pid": {
                  "type": "integer",
                  "description": "Platform ID",
                  "format": "int32"
                },
                "pdex": {
                  "type": "string",
                  "description": "Platform dexer name"
                },
                "pcid": {
                  "type": "integer",
                  "description": "Platform crypto ID",
                  "format": "int32"
                },
                "a": {
                  "type": "string",
                  "description": "Token address"
                },
                "n": {
                  "type": "string",
                  "description": "Token name"
                },
                "sym": {
                  "type": "string",
                  "description": "Token symbol"
                },
                "lg": {
                  "type": "string",
                  "description": "Logo URL"
                },
                "p": {
                  "type": "number",
                  "description": "Current price (USD)"
                },
                "pc1h": {
                  "type": "number",
                  "description": "Price change in last 1 hour (percentage)"
                },
                "pc24h": {
                  "type": "number",
                  "description": "Price change in last 24 hours (percentage)"
                },
                "pc7d": {
                  "type": "number",
                  "description": "Price change in last 7 days (percentage)"
                },
                "v24h": {
                  "type": "number",
                  "description": "24-hour trading volume (USD)"
                },
                "l": {
                  "type": "number",
                  "description": "Liquidity (USD)"
                },
                "ts": {
                  "type": "integer",
                  "description": "Timestamp of price data",
                  "format": "int64"
                },
                "mc": {
                  "type": "number",
                  "description": "Market cap"
                }
              },
              "description": "Token price information",
              "__$ref": "#/components/schemas/TokenPriceDTO"
            }
          }
        }
      ]
    }
  ]
}
```
