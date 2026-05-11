# GET /v1/dex/token/pools

**Summary:** Get token pools

**Description:** Get all pools for a specific token

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **platform** (query) - *Optional*: Platform name
- **address** (query) - *Optional*: Token address
- **size** (query) - *Optional*: None

### Raw Data

```json
{
  "slug": "get-token-pools",
  "summary": "Get token pools",
  "method": "get",
  "description": "Get all pools for a specific token",
  "operationId": "getTokenPools",
  "contentTypes": [],
  "path": "/v1/dex/token/pools",
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
      "name": "size",
      "in": "query",
      "description": null,
      "required": false,
      "schema": {
        "type": "integer",
        "format": "int32",
        "default": 20
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
                "addr": {
                  "type": "string",
                  "description": "Pool address"
                },
                "v24": {
                  "type": "string",
                  "description": "24-hour trading volume"
                },
                "pubAt": {
                  "type": "integer",
                  "description": "Publish timestamp",
                  "format": "int64"
                },
                "t0": {
                  "type": "object",
                  "properties": {
                    "addr": {
                      "type": "string",
                      "description": "Token address"
                    },
                    "lg": {
                      "type": "string",
                      "description": "Token logo URL"
                    },
                    "n": {
                      "type": "string",
                      "description": "Token name"
                    },
                    "sym": {
                      "type": "string",
                      "description": "Token symbol"
                    },
                    "liq": {
                      "type": "string",
                      "description": "Liquidity in native unit"
                    },
                    "liqUsd": {
                      "type": "string",
                      "description": "Liquidity in USD"
                    }
                  },
                  "description": "Basic token info in the pool",
                  "__$ref": "#/components/schemas/Token"
                },
                "t1": {
                  "type": "object",
                  "properties": {
                    "addr": {
                      "type": "string",
                      "description": "Token address"
                    },
                    "lg": {
                      "type": "string",
                      "description": "Token logo URL"
                    },
                    "n": {
                      "type": "string",
                      "description": "Token name"
                    },
                    "sym": {
                      "type": "string",
                      "description": "Token symbol"
                    },
                    "liq": {
                      "type": "string",
                      "description": "Liquidity in native unit"
                    },
                    "liqUsd": {
                      "type": "string",
                      "description": "Liquidity in USD"
                    }
                  },
                  "description": "Basic token info in the pool",
                  "__$ref": "#/components/schemas/Token"
                },
                "bidx": {
                  "type": "integer",
                  "description": "Index of the base token in the pool (0 or 1)",
                  "format": "int32"
                },
                "exid": {
                  "type": "integer",
                  "description": "Exchange ID",
                  "format": "int32"
                },
                "exn": {
                  "type": "string",
                  "description": "Exchange name"
                },
                "liqUsd": {
                  "type": "string",
                  "description": "Liquidity in USD"
                },
                "fa": {
                  "type": "string",
                  "description": "Factory address"
                },
                "lr": {
                  "type": "string",
                  "description": "Locked rate"
                },
                "br": {
                  "type": "string",
                  "description": "Burned rate"
                },
                "top": {
                  "type": "boolean",
                  "description": "Is top pool"
                },
                "mi": {
                  "type": "boolean",
                  "description": "Is meme inner pool"
                }
              },
              "description": "Token's top pool information",
              "__$ref": "#/components/schemas/TokenTopPoolDTO"
            }
          }
        }
      ]
    }
  ]
}
```
