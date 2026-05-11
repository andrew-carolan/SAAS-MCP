# GET /v1/dex/tokens/transactions

**Summary:** Get swap list

**Description:** Get swap/trade history for a token

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **platform** (query) - *Optional*: Blockchain platform name (bsc/sol/etc)
- **address** (query) - *Optional*: Token contract address
- **type** (query) - *Optional*: Transaction type (0 for buy, 1 for sell)
- **types** (query) - *Optional*: Transaction types filter, supports: buy, sell, open, close, add, reduce
- **maker** (query) - *Optional*: Maker address, support comma separated list
- **sortBy** (query) - *Optional*: Field to sort by (currently only supports 'time')
- **sortType** (query) - *Optional*: Sort direction ('asc' or 'desc', default is 'desc')
- **startTime** (query) - *Optional*: Start timestamp (inclusive)
- **endTime** (query) - *Optional*: End timestamp (inclusive)
- **minVolume** (query) - *Optional*: Minimum volume (inclusive)
- **maxVolume** (query) - *Optional*: Maximum volume (inclusive)
- **lastId** (query) - *Optional*: Cursor for pagination, format: ts_txHash_logId
- **limit** (query) - *Optional*: Result limit
- **version** (query) - *Optional*: Version

### Raw Data

```json
{
  "slug": "get-swap-list",
  "summary": "Get swap list",
  "method": "get",
  "description": "Get swap/trade history for a token",
  "operationId": "getSwapList",
  "contentTypes": [],
  "path": "/v1/dex/tokens/transactions",
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
      "description": "Transaction type (0 for buy, 1 for sell)",
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
      "name": "types",
      "in": "query",
      "description": "Transaction types filter, supports: buy, sell, open, close, add, reduce",
      "required": false,
      "schema": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "style": null,
      "explode": true,
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
      "description": "Field to sort by (currently only supports 'time')",
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
      "description": "Minimum volume (inclusive)",
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
      "description": "Maximum volume (inclusive)",
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
    },
    {
      "name": "version",
      "in": "query",
      "description": "Version",
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
            "type": "object",
            "properties": {
              "swaps": {
                "type": "array",
                "description": "List of swap transactions",
                "items": {
                  "type": "object",
                  "properties": {
                    "ts": {
                      "type": "integer",
                      "description": "Transaction time (timestamp)",
                      "format": "int64"
                    },
                    "tp": {
                      "type": "string",
                      "description": "Transaction type (buy/sell)"
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
                      "type": "string",
                      "description": "Base token symbol"
                    },
                    "t1s": {
                      "type": "string",
                      "description": "Quote token symbol"
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
                    "a0": {
                      "type": "number",
                      "description": "Base token amount"
                    },
                    "a1": {
                      "type": "number",
                      "description": "Quote token amount"
                    },
                    "t0pu": {
                      "type": "number",
                      "description": "Price in USD"
                    },
                    "t1pu": {
                      "type": "number",
                      "description": "Price in USD"
                    },
                    "q": {
                      "type": "number",
                      "description": "Price in quote"
                    },
                    "v": {
                      "type": "number",
                      "description": "Total transaction value in USD"
                    },
                    "qi": {
                      "type": "integer",
                      "description": "quoteIndex",
                      "format": "int32"
                    },
                    "ma": {
                      "type": "string",
                      "description": "Maker address"
                    },
                    "ex": {
                      "type": "boolean",
                      "description": "exclude"
                    },
                    "txtp": {
                      "type": "integer",
                      "description": "exclude",
                      "format": "int32"
                    },
                    "tx": {
                      "type": "string",
                      "description": "Transaction hash"
                    },
                    "h": {
                      "type": "integer",
                      "description": "height",
                      "format": "int64"
                    },
                    "txId": {
                      "type": "integer",
                      "description": "txId",
                      "format": "int64"
                    },
                    "lgid": {
                      "type": "integer",
                      "description": "Log ID",
                      "format": "int64"
                    },
                    "t0t": {
                      "type": "boolean",
                      "description": "t0top"
                    },
                    "t1t": {
                      "type": "boolean",
                      "description": "t1top"
                    },
                    "tags": {
                      "type": "array",
                      "description": "holder tags",
                      "items": {
                        "type": "object",
                        "properties": {
                          "name": {
                            "type": "string",
                            "description": "Tag type"
                          },
                          "value": {
                            "type": "integer",
                            "description": "Tag value",
                            "format": "int32"
                          }
                        },
                        "description": "Tag of swap tx",
                        "__$ref": "#/components/schemas/TagDTO"
                      }
                    },
                    "tc": {
                      "type": "integer",
                      "description": "transaction count",
                      "format": "int64"
                    },
                    "kn": {
                      "type": "string",
                      "description": "kol name"
                    },
                    "kpn": {
                      "type": "string",
                      "description": "kol public name"
                    },
                    "klu": {
                      "type": "string",
                      "description": "kol logo url"
                    },
                    "t0pt": {
                      "type": "string",
                      "description": "Token0 position type (open/close/add/reduce)"
                    },
                    "t1pt": {
                      "type": "string",
                      "description": "Token1 position type (open/close/add/reduce)"
                    }
                  },
                  "description": "Swap transaction data",
                  "__$ref": "#/components/schemas/TradeHistoryDTO"
                }
              },
              "lastId": {
                "type": "string",
                "description": "Last ID for pagination"
              }
            },
            "description": "Swap list response data",
            "__$ref": "#/components/schemas/SwapListResponseDTO"
          }
        }
      ]
    }
  ]
}
```
