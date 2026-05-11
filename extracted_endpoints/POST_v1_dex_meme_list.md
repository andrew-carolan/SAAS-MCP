# POST /v1/dex/meme/list

**Summary:** Get meme tokens

**Description:** Get list of meme tokens

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key

### Raw Data

```json
{
  "slug": "get-meme-tokens",
  "summary": "Get meme tokens",
  "method": "post",
  "description": "Get list of meme tokens",
  "operationId": "getMemeList",
  "contentTypes": [
    "application/json"
  ],
  "path": "/v1/dex/meme/list",
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
            "protocol": {
              "type": "integer",
              "description": "Protocol code",
              "format": "int32"
            },
            "exclusive": {
              "type": "integer",
              "description": "Binance exclusive flag",
              "format": "int32"
            },
            "limit": {
              "type": "integer",
              "description": "Result limit",
              "format": "int32"
            },
            "newCreationFilter": {
              "type": "object",
              "properties": {
                "topHoldersLessThan": {
                  "type": "boolean",
                  "description": "Whether top holders collectively hold less than a certain threshold"
                },
                "devSoldAll": {
                  "type": "boolean",
                  "description": "Whether the developer has sold all of their tokens"
                },
                "devStillHolding": {
                  "type": "boolean",
                  "description": "dev still holding"
                },
                "social": {
                  "type": "boolean",
                  "description": "Whether the token has social media presence"
                },
                "minAge": {
                  "type": "integer",
                  "description": "Minimum token age in minutes (\u22650)",
                  "format": "int32"
                },
                "maxAge": {
                  "type": "integer",
                  "description": "Maximum token age in minutes (\u22650)",
                  "format": "int32"
                },
                "minMarketCap": {
                  "type": "number",
                  "description": "Minimum market cap in USD (\u22650)"
                },
                "maxMarketCap": {
                  "type": "number",
                  "description": "Maximum market cap in USD (\u22650)"
                },
                "minLiquidity": {
                  "type": "number",
                  "description": "Minimum liquidity value in USD (\u22650)"
                },
                "maxLiquidity": {
                  "type": "number",
                  "description": "Maximum liquidity value in USD (\u22650)"
                },
                "minBondingCurve": {
                  "type": "number",
                  "description": "Minimum bonding curve value (\u22650)"
                },
                "maxBondingCurve": {
                  "type": "number",
                  "description": "Maximum bonding curve value (\u22650)"
                },
                "minDevHolding": {
                  "type": "number",
                  "description": "Minimum DEX holding amount (\u22650)"
                },
                "maxDevHolding": {
                  "type": "number",
                  "description": "Maximum DEX holding amount (\u22650)"
                },
                "minHolders": {
                  "type": "integer",
                  "description": "Minimum number of token holders (\u22650)",
                  "format": "int32"
                },
                "maxHolders": {
                  "type": "integer",
                  "description": "Maximum number of token holders (\u22650)",
                  "format": "int32"
                },
                "minVolume": {
                  "type": "number",
                  "description": "Minimum trading volume (\u22650)"
                },
                "maxVolume": {
                  "type": "number",
                  "description": "Maximum trading volume (\u22650)"
                },
                "minTxns": {
                  "type": "integer",
                  "description": "Minimum 24h transaction count (\u22650)",
                  "format": "int64"
                },
                "maxTxns": {
                  "type": "integer",
                  "description": "Maximum 24h transaction count (\u22650)",
                  "format": "int64"
                },
                "minBuys": {
                  "type": "integer",
                  "description": "Minimum 24h buy transaction count (\u22650)",
                  "format": "int64"
                },
                "maxBuys": {
                  "type": "integer",
                  "description": "Maximum 24h buy transaction count (\u22650)",
                  "format": "int64"
                },
                "minSells": {
                  "type": "integer",
                  "description": "Minimum 24h sell transaction count (\u22650)",
                  "format": "int64"
                },
                "maxSells": {
                  "type": "integer",
                  "description": "Maximum 24h sell transaction count (\u22650)",
                  "format": "int64"
                },
                "minTop10Holding": {
                  "type": "number",
                  "description": "Minimum Top10Holding (\u22650)",
                  "format": "double"
                },
                "maxTop10Holding": {
                  "type": "number",
                  "description": "Maximum Top10Holding (\u22650)",
                  "format": "double"
                },
                "minSnipers": {
                  "type": "number",
                  "description": "Minimum Snipers (\u22650)",
                  "format": "double"
                },
                "maxSnipers": {
                  "type": "number",
                  "description": "Maximum Snipers (\u22650)",
                  "format": "double"
                },
                "minInsiders": {
                  "type": "number",
                  "description": "Minimum Insiders (\u22650)",
                  "format": "double"
                },
                "maxInsiders": {
                  "type": "number",
                  "description": "Maximum Insiders (\u22650)",
                  "format": "double"
                }
              },
              "description": "Filter criteria for meme coins",
              "__$ref": "#/components/schemas/MemeCoinFilterDTO"
            },
            "aboutGraduateFilter": {
              "type": "object",
              "properties": {
                "topHoldersLessThan": {
                  "type": "boolean",
                  "description": "Whether top holders collectively hold less than a certain threshold"
                },
                "devSoldAll": {
                  "type": "boolean",
                  "description": "Whether the developer has sold all of their tokens"
                },
                "devStillHolding": {
                  "type": "boolean",
                  "description": "dev still holding"
                },
                "social": {
                  "type": "boolean",
                  "description": "Whether the token has social media presence"
                },
                "minAge": {
                  "type": "integer",
                  "description": "Minimum token age in minutes (\u22650)",
                  "format": "int32"
                },
                "maxAge": {
                  "type": "integer",
                  "description": "Maximum token age in minutes (\u22650)",
                  "format": "int32"
                },
                "minMarketCap": {
                  "type": "number",
                  "description": "Minimum market cap in USD (\u22650)"
                },
                "maxMarketCap": {
                  "type": "number",
                  "description": "Maximum market cap in USD (\u22650)"
                },
                "minLiquidity": {
                  "type": "number",
                  "description": "Minimum liquidity value in USD (\u22650)"
                },
                "maxLiquidity": {
                  "type": "number",
                  "description": "Maximum liquidity value in USD (\u22650)"
                },
                "minBondingCurve": {
                  "type": "number",
                  "description": "Minimum bonding curve value (\u22650)"
                },
                "maxBondingCurve": {
                  "type": "number",
                  "description": "Maximum bonding curve value (\u22650)"
                },
                "minDevHolding": {
                  "type": "number",
                  "description": "Minimum DEX holding amount (\u22650)"
                },
                "maxDevHolding": {
                  "type": "number",
                  "description": "Maximum DEX holding amount (\u22650)"
                },
                "minHolders": {
                  "type": "integer",
                  "description": "Minimum number of token holders (\u22650)",
                  "format": "int32"
                },
                "maxHolders": {
                  "type": "integer",
                  "description": "Maximum number of token holders (\u22650)",
                  "format": "int32"
                },
                "minVolume": {
                  "type": "number",
                  "description": "Minimum trading volume (\u22650)"
                },
                "maxVolume": {
                  "type": "number",
                  "description": "Maximum trading volume (\u22650)"
                },
                "minTxns": {
                  "type": "integer",
                  "description": "Minimum 24h transaction count (\u22650)",
                  "format": "int64"
                },
                "maxTxns": {
                  "type": "integer",
                  "description": "Maximum 24h transaction count (\u22650)",
                  "format": "int64"
                },
                "minBuys": {
                  "type": "integer",
                  "description": "Minimum 24h buy transaction count (\u22650)",
                  "format": "int64"
                },
                "maxBuys": {
                  "type": "integer",
                  "description": "Maximum 24h buy transaction count (\u22650)",
                  "format": "int64"
                },
                "minSells": {
                  "type": "integer",
                  "description": "Minimum 24h sell transaction count (\u22650)",
                  "format": "int64"
                },
                "maxSells": {
                  "type": "integer",
                  "description": "Maximum 24h sell transaction count (\u22650)",
                  "format": "int64"
                },
                "minTop10Holding": {
                  "type": "number",
                  "description": "Minimum Top10Holding (\u22650)",
                  "format": "double"
                },
                "maxTop10Holding": {
                  "type": "number",
                  "description": "Maximum Top10Holding (\u22650)",
                  "format": "double"
                },
                "minSnipers": {
                  "type": "number",
                  "description": "Minimum Snipers (\u22650)",
                  "format": "double"
                },
                "maxSnipers": {
                  "type": "number",
                  "description": "Maximum Snipers (\u22650)",
                  "format": "double"
                },
                "minInsiders": {
                  "type": "number",
                  "description": "Minimum Insiders (\u22650)",
                  "format": "double"
                },
                "maxInsiders": {
                  "type": "number",
                  "description": "Maximum Insiders (\u22650)",
                  "format": "double"
                }
              },
              "description": "Filter criteria for meme coins",
              "__$ref": "#/components/schemas/MemeCoinFilterDTO"
            },
            "graduateFilter": {
              "type": "object",
              "properties": {
                "topHoldersLessThan": {
                  "type": "boolean",
                  "description": "Whether top holders collectively hold less than a certain threshold"
                },
                "devSoldAll": {
                  "type": "boolean",
                  "description": "Whether the developer has sold all of their tokens"
                },
                "devStillHolding": {
                  "type": "boolean",
                  "description": "dev still holding"
                },
                "social": {
                  "type": "boolean",
                  "description": "Whether the token has social media presence"
                },
                "minAge": {
                  "type": "integer",
                  "description": "Minimum token age in minutes (\u22650)",
                  "format": "int32"
                },
                "maxAge": {
                  "type": "integer",
                  "description": "Maximum token age in minutes (\u22650)",
                  "format": "int32"
                },
                "minMarketCap": {
                  "type": "number",
                  "description": "Minimum market cap in USD (\u22650)"
                },
                "maxMarketCap": {
                  "type": "number",
                  "description": "Maximum market cap in USD (\u22650)"
                },
                "minLiquidity": {
                  "type": "number",
                  "description": "Minimum liquidity value in USD (\u22650)"
                },
                "maxLiquidity": {
                  "type": "number",
                  "description": "Maximum liquidity value in USD (\u22650)"
                },
                "minBondingCurve": {
                  "type": "number",
                  "description": "Minimum bonding curve value (\u22650)"
                },
                "maxBondingCurve": {
                  "type": "number",
                  "description": "Maximum bonding curve value (\u22650)"
                },
                "minDevHolding": {
                  "type": "number",
                  "description": "Minimum DEX holding amount (\u22650)"
                },
                "maxDevHolding": {
                  "type": "number",
                  "description": "Maximum DEX holding amount (\u22650)"
                },
                "minHolders": {
                  "type": "integer",
                  "description": "Minimum number of token holders (\u22650)",
                  "format": "int32"
                },
                "maxHolders": {
                  "type": "integer",
                  "description": "Maximum number of token holders (\u22650)",
                  "format": "int32"
                },
                "minVolume": {
                  "type": "number",
                  "description": "Minimum trading volume (\u22650)"
                },
                "maxVolume": {
                  "type": "number",
                  "description": "Maximum trading volume (\u22650)"
                },
                "minTxns": {
                  "type": "integer",
                  "description": "Minimum 24h transaction count (\u22650)",
                  "format": "int64"
                },
                "maxTxns": {
                  "type": "integer",
                  "description": "Maximum 24h transaction count (\u22650)",
                  "format": "int64"
                },
                "minBuys": {
                  "type": "integer",
                  "description": "Minimum 24h buy transaction count (\u22650)",
                  "format": "int64"
                },
                "maxBuys": {
                  "type": "integer",
                  "description": "Maximum 24h buy transaction count (\u22650)",
                  "format": "int64"
                },
                "minSells": {
                  "type": "integer",
                  "description": "Minimum 24h sell transaction count (\u22650)",
                  "format": "int64"
                },
                "maxSells": {
                  "type": "integer",
                  "description": "Maximum 24h sell transaction count (\u22650)",
                  "format": "int64"
                },
                "minTop10Holding": {
                  "type": "number",
                  "description": "Minimum Top10Holding (\u22650)",
                  "format": "double"
                },
                "maxTop10Holding": {
                  "type": "number",
                  "description": "Maximum Top10Holding (\u22650)",
                  "format": "double"
                },
                "minSnipers": {
                  "type": "number",
                  "description": "Minimum Snipers (\u22650)",
                  "format": "double"
                },
                "maxSnipers": {
                  "type": "number",
                  "description": "Maximum Snipers (\u22650)",
                  "format": "double"
                },
                "minInsiders": {
                  "type": "number",
                  "description": "Minimum Insiders (\u22650)",
                  "format": "double"
                },
                "maxInsiders": {
                  "type": "number",
                  "description": "Maximum Insiders (\u22650)",
                  "format": "double"
                }
              },
              "description": "Filter criteria for meme coins",
              "__$ref": "#/components/schemas/MemeCoinFilterDTO"
            }
          },
          "description": "Meme coin request",
          "__$ref": "#/components/schemas/DqueryMemeRequestDTO"
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
              "newCreations": {
                "type": "object",
                "properties": {
                  "plt": {
                    "type": "integer",
                    "description": "Token platform ID",
                    "format": "int32"
                  },
                  "cid": {
                    "type": "string",
                    "description": "chain platform id"
                  },
                  "pr": {
                    "type": "integer",
                    "description": "Platform crypto id",
                    "format": "int32"
                  },
                  "pn": {
                    "type": "string",
                    "description": "Platform name"
                  },
                  "it": {
                    "type": "string",
                    "description": "Item link"
                  },
                  "addr": {
                    "type": "string",
                    "description": "Token address"
                  },
                  "n": {
                    "type": "string",
                    "description": "Name of the token"
                  },
                  "sym": {
                    "type": "string",
                    "description": "Symbol of the token"
                  },
                  "lg": {
                    "type": "string",
                    "description": "URL to the token's logo image"
                  },
                  "tw": {
                    "type": "string",
                    "description": "Twitter URL"
                  },
                  "web": {
                    "type": "string",
                    "description": "Official website URL"
                  },
                  "tg": {
                    "type": "string",
                    "description": "Telegram URL"
                  },
                  "pt": {
                    "type": "integer",
                    "description": "Token protocol type: 1001=Pump.fun, 1002=Moonshot, 2001=Four.meme",
                    "format": "int64"
                  },
                  "pubAt": {
                    "type": "integer",
                    "description": "Timestamp when the token was published, in milliseconds since epoch",
                    "format": "int64"
                  },
                  "dec": {
                    "type": "integer",
                    "description": "Number of decimals",
                    "format": "int32"
                  },
                  "tp": {
                    "type": "string",
                    "description": "Total supply of the token"
                  },
                  "bc": {
                    "type": "number",
                    "description": "Bonding curve progress percentage (0~1)"
                  },
                  "mcap": {
                    "type": "number",
                    "description": "Market capitalization in USD"
                  },
                  "liq": {
                    "type": "number",
                    "description": "Liquidity value in USD"
                  },
                  "vu": {
                    "type": "number",
                    "description": "Trading volume in USD over the last 24 hours"
                  },
                  "np": {
                    "type": "number",
                    "description": "Native price of the token (in native currency, e.g., SOL)"
                  },
                  "p": {
                    "type": "number",
                    "description": "Price of the token in USD"
                  },
                  "txs": {
                    "type": "integer",
                    "description": "Total number of transactions associated with this token",
                    "format": "int64"
                  },
                  "nb": {
                    "type": "integer",
                    "description": "Number of buy transactions in the last 24 hours",
                    "format": "int64"
                  },
                  "ns": {
                    "type": "integer",
                    "description": "Number of sell transactions in the last 24 hours",
                    "format": "int64"
                  },
                  "htp": {
                    "type": "number",
                    "description": "Percentage of tokens held by top 10 wallets",
                    "format": "double"
                  },
                  "hdp": {
                    "type": "number",
                    "description": "Percentage of tokens held by developer wallets",
                    "format": "double"
                  },
                  "hsp": {
                    "type": "number",
                    "description": "Percentage of tokens held by sniper wallets",
                    "format": "double"
                  },
                  "hip": {
                    "type": "number",
                    "description": "Percentage of tokens held by insider wallets",
                    "format": "double"
                  },
                  "dsp": {
                    "type": "number",
                    "description": "Percentage of tokens sold by DEX developers",
                    "format": "double"
                  },
                  "dmc": {
                    "type": "integer",
                    "description": "Number of times the token has migrated from a DEX",
                    "format": "int32"
                  },
                  "ms": {
                    "type": "integer",
                    "description": "Migration status",
                    "format": "int32"
                  },
                  "mt": {
                    "type": "integer",
                    "description": "Timestamp when the token was migrated, in milliseconds since epoch",
                    "format": "int64"
                  },
                  "md": {
                    "type": "string",
                    "description": "Name of the DEX where the token was migrated to"
                  },
                  "h": {
                    "type": "integer",
                    "description": "Total number of unique token holders",
                    "format": "int64"
                  },
                  "ecs": {
                    "type": "integer",
                    "description": "Binance exclusive code, 1 - exclusive",
                    "format": "int32"
                  }
                },
                "description": "List of meme coins that have graduated",
                "__$ref": "#/components/schemas/MemeCoinResultDTO"
              },
              "aboutGraduates": {
                "type": "object",
                "properties": {
                  "plt": {
                    "type": "integer",
                    "description": "Token platform ID",
                    "format": "int32"
                  },
                  "cid": {
                    "type": "string",
                    "description": "chain platform id"
                  },
                  "pr": {
                    "type": "integer",
                    "description": "Platform crypto id",
                    "format": "int32"
                  },
                  "pn": {
                    "type": "string",
                    "description": "Platform name"
                  },
                  "it": {
                    "type": "string",
                    "description": "Item link"
                  },
                  "addr": {
                    "type": "string",
                    "description": "Token address"
                  },
                  "n": {
                    "type": "string",
                    "description": "Name of the token"
                  },
                  "sym": {
                    "type": "string",
                    "description": "Symbol of the token"
                  },
                  "lg": {
                    "type": "string",
                    "description": "URL to the token's logo image"
                  },
                  "tw": {
                    "type": "string",
                    "description": "Twitter URL"
                  },
                  "web": {
                    "type": "string",
                    "description": "Official website URL"
                  },
                  "tg": {
                    "type": "string",
                    "description": "Telegram URL"
                  },
                  "pt": {
                    "type": "integer",
                    "description": "Token protocol type: 1001=Pump.fun, 1002=Moonshot, 2001=Four.meme",
                    "format": "int64"
                  },
                  "pubAt": {
                    "type": "integer",
                    "description": "Timestamp when the token was published, in milliseconds since epoch",
                    "format": "int64"
                  },
                  "dec": {
                    "type": "integer",
                    "description": "Number of decimals",
                    "format": "int32"
                  },
                  "tp": {
                    "type": "string",
                    "description": "Total supply of the token"
                  },
                  "bc": {
                    "type": "number",
                    "description": "Bonding curve progress percentage (0~1)"
                  },
                  "mcap": {
                    "type": "number",
                    "description": "Market capitalization in USD"
                  },
                  "liq": {
                    "type": "number",
                    "description": "Liquidity value in USD"
                  },
                  "vu": {
                    "type": "number",
                    "description": "Trading volume in USD over the last 24 hours"
                  },
                  "np": {
                    "type": "number",
                    "description": "Native price of the token (in native currency, e.g., SOL)"
                  },
                  "p": {
                    "type": "number",
                    "description": "Price of the token in USD"
                  },
                  "txs": {
                    "type": "integer",
                    "description": "Total number of transactions associated with this token",
                    "format": "int64"
                  },
                  "nb": {
                    "type": "integer",
                    "description": "Number of buy transactions in the last 24 hours",
                    "format": "int64"
                  },
                  "ns": {
                    "type": "integer",
                    "description": "Number of sell transactions in the last 24 hours",
                    "format": "int64"
                  },
                  "htp": {
                    "type": "number",
                    "description": "Percentage of tokens held by top 10 wallets",
                    "format": "double"
                  },
                  "hdp": {
                    "type": "number",
                    "description": "Percentage of tokens held by developer wallets",
                    "format": "double"
                  },
                  "hsp": {
                    "type": "number",
                    "description": "Percentage of tokens held by sniper wallets",
                    "format": "double"
                  },
                  "hip": {
                    "type": "number",
                    "description": "Percentage of tokens held by insider wallets",
                    "format": "double"
                  },
                  "dsp": {
                    "type": "number",
                    "description": "Percentage of tokens sold by DEX developers",
                    "format": "double"
                  },
                  "dmc": {
                    "type": "integer",
                    "description": "Number of times the token has migrated from a DEX",
                    "format": "int32"
                  },
                  "ms": {
                    "type": "integer",
                    "description": "Migration status",
                    "format": "int32"
                  },
                  "mt": {
                    "type": "integer",
                    "description": "Timestamp when the token was migrated, in milliseconds since epoch",
                    "format": "int64"
                  },
                  "md": {
                    "type": "string",
                    "description": "Name of the DEX where the token was migrated to"
                  },
                  "h": {
                    "type": "integer",
                    "description": "Total number of unique token holders",
                    "format": "int64"
                  },
                  "ecs": {
                    "type": "integer",
                    "description": "Binance exclusive code, 1 - exclusive",
                    "format": "int32"
                  }
                },
                "description": "List of meme coins that have graduated",
                "__$ref": "#/components/schemas/MemeCoinResultDTO"
              },
              "graduates": {
                "type": "object",
                "properties": {
                  "plt": {
                    "type": "integer",
                    "description": "Token platform ID",
                    "format": "int32"
                  },
                  "cid": {
                    "type": "string",
                    "description": "chain platform id"
                  },
                  "pr": {
                    "type": "integer",
                    "description": "Platform crypto id",
                    "format": "int32"
                  },
                  "pn": {
                    "type": "string",
                    "description": "Platform name"
                  },
                  "it": {
                    "type": "string",
                    "description": "Item link"
                  },
                  "addr": {
                    "type": "string",
                    "description": "Token address"
                  },
                  "n": {
                    "type": "string",
                    "description": "Name of the token"
                  },
                  "sym": {
                    "type": "string",
                    "description": "Symbol of the token"
                  },
                  "lg": {
                    "type": "string",
                    "description": "URL to the token's logo image"
                  },
                  "tw": {
                    "type": "string",
                    "description": "Twitter URL"
                  },
                  "web": {
                    "type": "string",
                    "description": "Official website URL"
                  },
                  "tg": {
                    "type": "string",
                    "description": "Telegram URL"
                  },
                  "pt": {
                    "type": "integer",
                    "description": "Token protocol type: 1001=Pump.fun, 1002=Moonshot, 2001=Four.meme",
                    "format": "int64"
                  },
                  "pubAt": {
                    "type": "integer",
                    "description": "Timestamp when the token was published, in milliseconds since epoch",
                    "format": "int64"
                  },
                  "dec": {
                    "type": "integer",
                    "description": "Number of decimals",
                    "format": "int32"
                  },
                  "tp": {
                    "type": "string",
                    "description": "Total supply of the token"
                  },
                  "bc": {
                    "type": "number",
                    "description": "Bonding curve progress percentage (0~1)"
                  },
                  "mcap": {
                    "type": "number",
                    "description": "Market capitalization in USD"
                  },
                  "liq": {
                    "type": "number",
                    "description": "Liquidity value in USD"
                  },
                  "vu": {
                    "type": "number",
                    "description": "Trading volume in USD over the last 24 hours"
                  },
                  "np": {
                    "type": "number",
                    "description": "Native price of the token (in native currency, e.g., SOL)"
                  },
                  "p": {
                    "type": "number",
                    "description": "Price of the token in USD"
                  },
                  "txs": {
                    "type": "integer",
                    "description": "Total number of transactions associated with this token",
                    "format": "int64"
                  },
                  "nb": {
                    "type": "integer",
                    "description": "Number of buy transactions in the last 24 hours",
                    "format": "int64"
                  },
                  "ns": {
                    "type": "integer",
                    "description": "Number of sell transactions in the last 24 hours",
                    "format": "int64"
                  },
                  "htp": {
                    "type": "number",
                    "description": "Percentage of tokens held by top 10 wallets",
                    "format": "double"
                  },
                  "hdp": {
                    "type": "number",
                    "description": "Percentage of tokens held by developer wallets",
                    "format": "double"
                  },
                  "hsp": {
                    "type": "number",
                    "description": "Percentage of tokens held by sniper wallets",
                    "format": "double"
                  },
                  "hip": {
                    "type": "number",
                    "description": "Percentage of tokens held by insider wallets",
                    "format": "double"
                  },
                  "dsp": {
                    "type": "number",
                    "description": "Percentage of tokens sold by DEX developers",
                    "format": "double"
                  },
                  "dmc": {
                    "type": "integer",
                    "description": "Number of times the token has migrated from a DEX",
                    "format": "int32"
                  },
                  "ms": {
                    "type": "integer",
                    "description": "Migration status",
                    "format": "int32"
                  },
                  "mt": {
                    "type": "integer",
                    "description": "Timestamp when the token was migrated, in milliseconds since epoch",
                    "format": "int64"
                  },
                  "md": {
                    "type": "string",
                    "description": "Name of the DEX where the token was migrated to"
                  },
                  "h": {
                    "type": "integer",
                    "description": "Total number of unique token holders",
                    "format": "int64"
                  },
                  "ecs": {
                    "type": "integer",
                    "description": "Binance exclusive code, 1 - exclusive",
                    "format": "int32"
                  }
                },
                "description": "List of meme coins that have graduated",
                "__$ref": "#/components/schemas/MemeCoinResultDTO"
              }
            },
            "description": "Response object containing categorized meme coin results",
            "__$ref": "#/components/schemas/MemeCoinResponseDTO"
          }
        }
      ]
    }
  ]
}
```
