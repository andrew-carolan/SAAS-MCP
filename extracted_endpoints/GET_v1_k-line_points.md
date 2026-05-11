# GET /v1/k-line/points

**Summary:** Get K-line points

**Description:** Get K-line price points for a token.

Response Format: Each point is an array with 3 elements:
- **[0]** price: Token price
- **[1]** volume: Trading volume
- **[2]** timestamp: UNIX timestamp (seconds)

Example: ``[[1.23, 50000, 1705363200], ...]``

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **platform** (query) - *Optional*: Platform name or id
- **address** (query) - *Optional*: Token or pool address
- **interval** (query) - *Optional*: Kline interval: 1s/5s/30s/1min/3min/5min/15min/30min/1h/2h/4h/6h/8h/12h/1d/3d/1w/1m
- **from** (query) - *Optional*: Start timestamp (UNIX epoch)
- **to** (query) - *Optional*: End timestamp (UNIX epoch)
- **unit** (query) - *Optional*: Kline unit: usd, native, quote
- **limit** (query) - *Optional*: Number of points to load
- **pm** (query) - *Optional*: Kline type: p (price), m (marketcap)

### Raw Data

```json
{
  "slug": "get-k-line-points",
  "summary": "Get K-line points",
  "method": "get",
  "description": "Get K-line price points for a token.\n\nResponse Format: Each point is an array with 3 elements:\n- **[0]** price: Token price\n- **[1]** volume: Trading volume\n- **[2]** timestamp: UNIX timestamp (seconds)\n\nExample: ``[[1.23, 50000, 1705363200], ...]``",
  "operationId": "getKlinePoints",
  "contentTypes": [],
  "path": "/v1/k-line/points",
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
      "name": "address",
      "in": "query",
      "description": "Token or pool address",
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
      "description": "Kline interval: 1s/5s/30s/1min/3min/5min/15min/30min/1h/2h/4h/6h/8h/12h/1d/3d/1w/1m",
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
      "description": "Start timestamp (UNIX epoch)",
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
      "description": "End timestamp (UNIX epoch)",
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
      "name": "unit",
      "in": "query",
      "description": "Kline unit: usd, native, quote",
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
      "description": "Number of points to load",
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
      "name": "pm",
      "in": "query",
      "description": "Kline type: p (price), m (marketcap)",
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
              "type": "array",
              "items": {
                "type": "number"
              }
            }
          }
        }
      ]
    }
  ]
}
```
