# GET /v1/dex/token/price

**Summary:** Get token price

**Description:** Get current price for a specific token

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **platform** (query) - *Optional*: Platform name
- **address** (query) - *Optional*: Token address

### Raw Data

```json
{
  "slug": "get-token-price",
  "summary": "Get token price",
  "method": "get",
  "description": "Get current price for a specific token",
  "operationId": "getTokenPrice",
  "contentTypes": [],
  "path": "/v1/dex/token/price",
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
      ]
    }
  ]
}
```
