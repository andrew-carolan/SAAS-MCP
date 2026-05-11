# GET /v1/dex/search

**Summary:** Search tokens

**Description:** Search for tokens by keyword

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **q** (query) - *Optional*: Search keyword
- **platform** (query) - *Optional*: Platform filter
- **sort** (query) - *Optional*: Sort field
- **limit** (query) - *Optional*: Result limit
- **code** (query) - *Optional*: Code filter

### Raw Data

```json
{
  "slug": "search-tokens",
  "summary": "Search tokens",
  "method": "get",
  "description": "Search for tokens by keyword",
  "operationId": "search",
  "contentTypes": [],
  "path": "/v1/dex/search",
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
      "name": "q",
      "in": "query",
      "description": "Search keyword",
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
      "name": "platform",
      "in": "query",
      "description": "Platform filter",
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
      "name": "sort",
      "in": "query",
      "description": "Sort field",
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
      "name": "code",
      "in": "query",
      "description": "Code filter",
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
              "total": {
                "type": "integer",
                "format": "int32"
              },
              "tks": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "pltId": {
                      "type": "integer",
                      "format": "int32"
                    },
                    "plt": {
                      "type": "string"
                    },
                    "plti": {
                      "type": "integer",
                      "format": "int32"
                    },
                    "n": {
                      "type": "string"
                    },
                    "s": {
                      "type": "string"
                    },
                    "addr": {
                      "type": "string"
                    },
                    "pt": {
                      "type": "integer",
                      "format": "int64"
                    },
                    "lt": {
                      "type": "integer",
                      "format": "int64"
                    },
                    "w": {
                      "type": "string"
                    },
                    "x": {
                      "type": "string"
                    },
                    "l": {
                      "type": "string"
                    },
                    "pu": {
                      "type": "string"
                    },
                    "pc24h": {
                      "type": "number",
                      "format": "float"
                    },
                    "dec": {
                      "type": "integer",
                      "format": "int32"
                    },
                    "tsup": {
                      "type": "string"
                    },
                    "fpt": {
                      "type": "integer",
                      "format": "int64"
                    },
                    "fpct": {
                      "type": "integer",
                      "format": "int64"
                    },
                    "v24h": {
                      "type": "number"
                    },
                    "fdv": {
                      "type": "number"
                    },
                    "mc": {
                      "type": "number"
                    },
                    "liq": {
                      "type": "number"
                    },
                    "ts": {
                      "type": "integer",
                      "format": "int64"
                    },
                    "lf": {
                      "type": "integer",
                      "format": "int32"
                    },
                    "cid": {
                      "type": "integer",
                      "format": "int32"
                    },
                    "bnCid": {
                      "type": "string"
                    },
                    "ut24h": {
                      "type": "integer",
                      "format": "int64"
                    },
                    "ecs": {
                      "type": "integer",
                      "description": "Binance exclusive code, 1 - exclusive",
                      "format": "int32"
                    },
                    "ssc": {
                      "type": "number",
                      "description": "Search relevance score",
                      "format": "float"
                    },
                    "pin": {
                      "type": "string",
                      "description": "Comma-separated pinned types based on sort fields: ido,alpha,trending or null"
                    }
                  },
                  "__$ref": "#/components/schemas/SearchResultDTO"
                }
              }
            },
            "__$ref": "#/components/schemas/SearchResponseDTO"
          }
        }
      ]
    }
  ]
}
```
