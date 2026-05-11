# GET /v1/dex/platform/detail

**Summary:** Get platform detail

**Description:** Get detailed information for a specific platform

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **platformName** (query) - *Optional*: Platform name

### Raw Data

```json
{
  "slug": "get-platform-detail",
  "summary": "Get platform detail",
  "method": "get",
  "description": "Get detailed information for a specific platform",
  "operationId": "getPlatformDetail",
  "contentTypes": [],
  "path": "/v1/dex/platform/detail",
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
      "name": "platformName",
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
              "id": {
                "type": "integer",
                "description": "Unique platform ID",
                "format": "int32",
                "example": 14
              },
              "n": {
                "type": "string",
                "description": "Platform name",
                "example": "Ethereum"
              },
              "i": {
                "type": "string",
                "description": "Icon URL for the platform",
                "example": "https://cdn.example.com/icons/eth.png"
              },
              "uf": {
                "type": "string",
                "description": "URL format for block explorer (contract/token)",
                "example": "https://etherscan.io/token/{tokenAddress}"
              },
              "dn": {
                "type": "string",
                "description": "Number of supported DEXs on this platform",
                "example": "12"
              },
              "txuf": {
                "type": "string",
                "description": "URL format for viewing transactions",
                "example": "https://etherscan.io/tx/{txHash}"
              },
              "v": {
                "type": "boolean",
                "description": "Whether the platform is visible in the UI",
                "example": true
              },
              "p": {
                "type": "boolean",
                "description": "Whether the platform is pinned (e.g., prioritized display)",
                "example": false
              },
              "addrUrl": {
                "type": "string",
                "description": "URL format for address explorer",
                "example": "https://etherscan.io/address/{address}"
              },
              "chId": {
                "type": "integer",
                "description": "Internal chain ID",
                "format": "int32",
                "example": 1
              },
              "puf": {
                "type": "string",
                "description": "URL format for pool explorer",
                "example": "https://dexscan.io/pool/{poolAddress}"
              },
              "wcId": {
                "type": "integer",
                "description": "Wrapped native token ID (e.g., WETH)",
                "format": "int32",
                "example": 2001
              },
              "hl": {
                "type": "integer",
                "description": "Whether the platform is highlighted",
                "format": "int32",
                "example": 1
              },
              "ho": {
                "type": "integer",
                "description": "Display order for highlighted platforms",
                "format": "int32",
                "example": 3
              },
              "pltA": {
                "type": "string",
                "description": "platform acronym",
                "example": "ETH"
              },
              "cid": {
                "type": "integer",
                "format": "int32"
              }
            },
            "description": "Data Transfer Object representing a supported blockchain platform",
            "__$ref": "#/components/schemas/PlatformDTO"
          }
        }
      ]
    }
  ]
}
```
