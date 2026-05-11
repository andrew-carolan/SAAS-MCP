# GET /v1/dex/holders/trend/list

**Summary:** Get holder trend list

**Description:** Get detailed information for holders trend list

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **platform** (query) - *Optional*: Platform name or id
- **tokenAddress** (query) - *Optional*: Token  address
- **interval** (query) - *Optional*: Kline interval: 1d
- **from** (query) - *Optional*: start timestamp
- **to** (query) - *Optional*: End timestamp
- **limit** (query) - *Optional*: Number of to load

### Raw Data

```json
{
  "slug": "get-holder-trend-list",
  "summary": "Get holder trend list",
  "method": "get",
  "description": "Get detailed information for holders trend list",
  "operationId": "getHoldTrendList",
  "contentTypes": [],
  "path": "/v1/dex/holders/trend/list",
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
      "name": "platform",
      "in": "query",
      "description": "Platform name or id",
      "required": false,
      "schema": {
        "type": "string"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "tokenAddress",
      "in": "query",
      "description": "Token  address",
      "required": false,
      "schema": {
        "type": "string"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "interval",
      "in": "query",
      "description": "Kline interval: 1d",
      "required": false,
      "schema": {
        "type": "string"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "from",
      "in": "query",
      "description": "start timestamp",
      "required": false,
      "schema": {
        "type": "integer",
        "format": "int64"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "to",
      "in": "query",
      "description": "End timestamp",
      "required": false,
      "schema": {
        "type": "integer",
        "format": "int64"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "limit",
      "in": "query",
      "description": "Number of to load",
      "required": false,
      "schema": {
        "type": "integer",
        "format": "int32"
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
                "ts": {
                  "type": "integer",
                  "format": "int64"
                },
                "endTs": {
                  "type": "integer",
                  "format": "int64"
                },
                "platform": {
                  "type": "integer",
                  "format": "int32"
                },
                "tokenAddress": {
                  "type": "string"
                },
                "holders": {
                  "type": "integer",
                  "format": "int64"
                },
                "holdingRatioOfTop100": {
                  "type": "string"
                },
                "holdingRatioOfTop50": {
                  "type": "string"
                },
                "holdingRatioOfTop10": {
                  "type": "string"
                },
                "totalBalanceOfTop100": {
                  "type": "string"
                },
                "totalBalanceOfTop50": {
                  "type": "string"
                },
                "totalBalanceOfTop10": {
                  "type": "string"
                },
                "biggerThan10DHolders": {
                  "type": "integer",
                  "format": "int64"
                },
                "avgBalanceAllHolders": {
                  "type": "string"
                },
                "avgBalanceOfTop100": {
                  "type": "string"
                },
                "avgPositionCostOfTop100": {
                  "type": "string"
                },
                "avgSellPriceOfTop100": {
                  "type": "string"
                },
                "tagHolder": {
                  "type": "string"
                },
                "avgBalanceUSDAllHolders": {
                  "type": "string"
                },
                "avgBalanceUSDOfTop100": {
                  "type": "string"
                },
                "tagHolderTTHM": {
                  "type": "string"
                },
                "price": {
                  "type": "string"
                }
              },
              "__$ref": "#/components/schemas/HolderTrendVO"
            }
          }
        }
      ]
    }
  ]
}
```
