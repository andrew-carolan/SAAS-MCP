# GET /v1/dex/holders/tag_count

**Summary:** Get holder tag count

**Description:** Get detailed information for holders tag count

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **platform** (query) - *Required*: None
- **tokenAddress** (query) - *Required*: None

### Raw Data

```json
{
  "slug": "get-holder-tag-count",
  "summary": "Get holder tag count",
  "method": "get",
  "description": "Get detailed information for holders tag count",
  "operationId": "getHolderTagCount",
  "contentTypes": [],
  "path": "/v1/dex/holders/tag_count",
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
      "description": null,
      "required": true,
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
      "description": null,
      "required": true,
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
              "holders": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "tag": {
                      "type": "string"
                    },
                    "hc": {
                      "type": "string"
                    },
                    "tb": {
                      "type": "string"
                    },
                    "hr": {
                      "type": "string"
                    }
                  },
                  "__$ref": "#/components/schemas/HolderTagItem"
                }
              },
              "platformId": {
                "type": "integer",
                "format": "int32"
              },
              "tokenAddress": {
                "type": "string"
              }
            },
            "__$ref": "#/components/schemas/HolderTagCountVO"
          }
        }
      ]
    }
  ]
}
```
