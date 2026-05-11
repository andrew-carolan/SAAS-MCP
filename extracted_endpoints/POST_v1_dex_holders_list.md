# POST /v1/dex/holders/list

**Summary:** Get holders list

**Description:** Get detailed information for holders list

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key

### Raw Data

```json
{
  "slug": "get-holders-list",
  "summary": "Get holders list",
  "method": "post",
  "description": "Get detailed information for holders list",
  "operationId": "getHolders",
  "contentTypes": [
    "application/json"
  ],
  "path": "/v1/dex/holders/list",
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
    "content": [
      {
        "mediaType": "application/json",
        "encoding": [],
        "examples": [],
        "schema": {
          "type": "object",
          "properties": {
            "tokenAddress": {
              "type": "string",
              "description": "Token contract address",
              "example": "0x1234567890abcdef1234567890abcdef12345678"
            },
            "platform": {
              "type": "string",
              "description": "Blockchain platform",
              "example": "ethereum"
            },
            "tag": {
              "type": "string",
              "description": "tag enum [tag_all, tag_kol, tag_smart_money, tag_whale, tag_bot, tag_sniper, tag_dev]",
              "example": "tag_all"
            }
          },
          "description": "holders request",
          "__$ref": "#/components/schemas/DqueryHoldersRequestDTO"
        }
      }
    ],
    "description": null,
    "required": true
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
                    "blockHeight": {
                      "type": "integer",
                      "format": "int64"
                    },
                    "firstActiveTime": {
                      "type": "integer",
                      "format": "int64"
                    },
                    "netBuyAmount": {
                      "type": "string"
                    },
                    "realizedPnlPercent": {
                      "type": "string"
                    },
                    "spotPosition": {
                      "type": "string"
                    },
                    "buyVolume": {
                      "type": "string"
                    },
                    "sellVolume": {
                      "type": "string"
                    },
                    "buyUsd": {
                      "type": "string"
                    },
                    "sellUsd": {
                      "type": "string"
                    },
                    "buyCount": {
                      "type": "string"
                    },
                    "sellCount": {
                      "type": "string"
                    },
                    "avgBuyPriceUsd": {
                      "type": "string"
                    },
                    "avgSellPriceUsd": {
                      "type": "string"
                    },
                    "realizedPnl": {
                      "type": "string"
                    },
                    "actualBalance": {
                      "type": "string"
                    },
                    "price": {
                      "type": "string"
                    },
                    "walletAddress": {
                      "type": "string"
                    },
                    "tokenAddress": {
                      "type": "string"
                    },
                    "platformId": {
                      "type": "integer",
                      "format": "int32"
                    },
                    "percent": {
                      "type": "string"
                    },
                    "balance": {
                      "type": "string"
                    },
                    "totalSupply": {
                      "type": "string"
                    },
                    "tokenAccount": {
                      "type": "string"
                    },
                    "logoUrl": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "publicName": {
                      "type": "string"
                    },
                    "tags": {
                      "type": "string"
                    },
                    "addressExplorerUrl": {
                      "type": "string"
                    },
                    "symbol": {
                      "type": "string"
                    },
                    "nativeBalance": {
                      "type": "string"
                    },
                    "fundingSource": {
                      "type": "string"
                    },
                    "fundingTime": {
                      "type": "integer",
                      "format": "int64"
                    },
                    "lastActiveTime": {
                      "type": "integer",
                      "format": "int64"
                    },
                    "walletCreateTime": {
                      "type": "integer",
                      "format": "int64"
                    },
                    "spotOpenTs": {
                      "type": "integer",
                      "format": "int64"
                    },
                    "spotClearanceTs": {
                      "type": "integer",
                      "format": "int64"
                    },
                    "tokenLogo": {
                      "type": "string"
                    },
                    "tokenSymbol": {
                      "type": "string"
                    },
                    "platformCryptoId": {
                      "type": "integer",
                      "format": "int32"
                    },
                    "dexerPlatformName": {
                      "type": "string"
                    },
                    "lowLiquidityFlag": {
                      "type": "integer",
                      "format": "int32"
                    },
                    "memePumpInnerFlag": {
                      "type": "integer",
                      "format": "int32"
                    },
                    "blackListFlag": {
                      "type": "integer",
                      "format": "int32"
                    },
                    "stableCoinFlag": {
                      "type": "integer",
                      "format": "int32"
                    },
                    "riskLevelFlag": {
                      "type": "integer",
                      "format": "int32"
                    }
                  },
                  "__$ref": "#/components/schemas/HolderDetailVO"
                }
              }
            },
            "__$ref": "#/components/schemas/HolderDexVO"
          }
        }
      ]
    }
  ]
}
```
