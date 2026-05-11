# GET /v1/dex/liquidity-change/list

**Summary:** Get liquidity change list

**Description:** Get liquidity change history for a token

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **platform** (query) - *Optional*: Blockchain platform name (bsc/sol/etc)
- **address** (query) - *Optional*: Token contract address
- **type** (query) - *Optional*: Liquidity change type
- **maker** (query) - *Optional*: Maker address, support comma separated list
- **sortBy** (query) - *Optional*: Field to sort by (currently only supports 'ts')
- **sortType** (query) - *Optional*: Sort direction ('asc' or 'desc', default is 'desc')
- **startTime** (query) - *Optional*: Start timestamp (inclusive)
- **endTime** (query) - *Optional*: End timestamp (inclusive)
- **minVolume** (query) - *Optional*: Minimum USD volume (inclusive)
- **maxVolume** (query) - *Optional*: Maximum USD volume (inclusive)
- **lastId** (query) - *Optional*: Cursor for pagination, format: ts_txHash_logId
- **limit** (query) - *Optional*: Result limit

### Raw Data

```json
{
  "slug": "get-liquidity-change-list",
  "summary": "Get liquidity change list",
  "method": "get",
  "description": "Get liquidity change history for a token",
  "operationId": "getLiquidityChangeList",
  "contentTypes": [],
  "path": "/v1/dex/liquidity-change/list",
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
      "description": "Blockchain platform name (bsc/sol/etc)",
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
      "description": "Token contract address",
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
      "name": "type",
      "in": "query",
      "description": "Liquidity change type",
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
      "name": "maker",
      "in": "query",
      "description": "Maker address, support comma separated list",
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
      "name": "sortBy",
      "in": "query",
      "description": "Field to sort by (currently only supports 'ts')",
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
      "name": "sortType",
      "in": "query",
      "description": "Sort direction ('asc' or 'desc', default is 'desc')",
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
      "name": "startTime",
      "in": "query",
      "description": "Start timestamp (inclusive)",
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
      "name": "endTime",
      "in": "query",
      "description": "End timestamp (inclusive)",
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
      "name": "minVolume",
      "in": "query",
      "description": "Minimum USD volume (inclusive)",
      "required": false,
      "schema": {
        "type": "number"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "maxVolume",
      "in": "query",
      "description": "Maximum USD volume (inclusive)",
      "required": false,
      "schema": {
        "type": "number"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "lastId",
      "in": "query",
      "description": "Cursor for pagination, format: ts_txHash_logId",
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
            "type": "object",
            "properties": {
              "lastId": {
                "type": "string",
                "description": "Last ID for pagination"
              },
              "lcs": {
                "type": "array",
                "description": "List of liquidity change transactions",
                "items": {
                  "type": "object",
                  "properties": {
                    "ts": {
                      "type": "integer",
                      "format": "int64"
                    },
                    "tp": {
                      "type": "string"
                    },
                    "eid": {
                      "type": "integer",
                      "description": "exchange id",
                      "format": "int32"
                    },
                    "en": {
                      "type": "string",
                      "description": "exchange name"
                    },
                    "f": {
                      "type": "string",
                      "description": "factory address"
                    },
                    "t0a": {
                      "type": "string",
                      "description": "Base token address"
                    },
                    "t1a": {
                      "type": "string",
                      "description": "Quote token address"
                    },
                    "t0s": {
                      "type": "string"
                    },
                    "t1s": {
                      "type": "string"
                    },
                    "a0": {
                      "type": "number"
                    },
                    "a1": {
                      "type": "number"
                    },
                    "tu": {
                      "type": "number"
                    },
                    "m": {
                      "type": "string"
                    },
                    "txn": {
                      "type": "string"
                    },
                    "h": {
                      "type": "integer",
                      "format": "int64"
                    },
                    "txId": {
                      "type": "integer",
                      "format": "int64"
                    },
                    "lgid": {
                      "type": "integer",
                      "format": "int64"
                    }
                  },
                  "description": "List of liquidity change transactions",
                  "__$ref": "#/components/schemas/LiquidityChangeDTO"
                }
              },
              "tlu": {
                "type": "number",
                "description": "total liquidity usd value"
              },
              "lpc": {
                "type": "integer",
                "description": "liquidity pool count",
                "format": "int64"
              }
            },
            "description": "Swap list response data",
            "__$ref": "#/components/schemas/LiquidityChangeListResponseDTO"
          }
        }
      ]
    }
  ]
}
```
