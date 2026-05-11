# GET /v1/dex/token-liquidity/query

**Summary:** Query token liquidity

**Description:** Get liquidity information for a specific token

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **platform** (query) - *Optional*: Platform name
- **address** (query) - *Optional*: Token address
- **interval** (query) - *Optional*: Time interval
- **limit** (query) - *Optional*: Result limit
- **to** (query) - *Optional*: End timestamp
- **needLatest** (query) - *Optional*: Whether to include latest value

### Raw Data

```json
{
  "slug": "query-token-liquidity",
  "summary": "Query token liquidity",
  "method": "get",
  "description": "Get liquidity information for a specific token",
  "operationId": "queryTokenLiquidity",
  "contentTypes": [],
  "path": "/v1/dex/token-liquidity/query",
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
      "description": "Platform name",
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
      "name": "address",
      "in": "query",
      "description": "Token address",
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
      "description": "Time interval",
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
      "name": "limit",
      "in": "query",
      "description": "Result limit",
      "required": false,
      "schema": {
        "type": "integer",
        "format": "int32"
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
      "name": "needLatest",
      "in": "query",
      "description": "Whether to include latest value",
      "required": false,
      "schema": {
        "type": "boolean"
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
                "snapshotTime": {
                  "type": "integer",
                  "format": "int64"
                },
                "liquidityUsd": {
                  "type": "number"
                },
                "liquidity": {
                  "type": "number"
                }
              },
              "__$ref": "#/components/schemas/TokenLiquiditySnapshotDTO"
            }
          }
        }
      ]
    }
  ]
}
```
