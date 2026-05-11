# POST /v1/dex/tokens/batch-query

**Summary:** Batch query tokens

**Description:** Query multiple tokens in one request

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key

### Raw Data

```json
{
  "slug": "batch-query-tokens",
  "summary": "Batch query tokens",
  "method": "post",
  "description": "Query multiple tokens in one request",
  "operationId": "batchQueryTokens",
  "contentTypes": [
    "application/json"
  ],
  "path": "/v1/dex/tokens/batch-query",
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
            "platform": {
              "type": "string",
              "description": "Platform name"
            },
            "addresses": {
              "type": "array",
              "description": "List of token addresses",
              "items": {
                "type": "string",
                "description": "List of token addresses"
              }
            }
          },
          "description": "Batch token query request",
          "__$ref": "#/components/schemas/DqueryBatchTokenRequestDTO"
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
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "n": {
                  "type": "string",
                  "description": "Token name"
                },
                "sym": {
                  "type": "string",
                  "description": "Token symbol"
                },
                "addr": {
                  "type": "string",
                  "description": "Token address"
                },
                "plt": {
                  "type": "string",
                  "description": "Platform name"
                },
                "pdex": {
                  "type": "string",
                  "description": "Token platform dexer name (pdex)"
                },
                "pcid": {
                  "type": "integer",
                  "description": "Token platform crypto ID (pcid)",
                  "format": "int32"
                },
                "pid": {
                  "type": "integer",
                  "description": "Platform ID",
                  "format": "int32"
                },
                "dec": {
                  "type": "integer",
                  "description": "Token decimals",
                  "format": "int32"
                },
                "crt": {
                  "type": "string",
                  "description": "Token creator address"
                },
                "own": {
                  "type": "string",
                  "description": "Token owner address"
                },
                "rnc": {
                  "type": "string",
                  "description": "Renounced address"
                },
                "web": {
                  "type": "string",
                  "description": "Project website"
                },
                "tw": {
                  "type": "string",
                  "description": "Twitter URL"
                },
                "tg": {
                  "type": "string",
                  "description": "Telegram URL"
                },
                "lg": {
                  "type": "string",
                  "description": "Logo URL"
                },
                "pubAt": {
                  "type": "integer",
                  "description": "Token publish timestamp",
                  "format": "int64"
                },
                "lchAt": {
                  "type": "integer",
                  "description": "Token launched timestamp",
                  "format": "int64"
                },
                "fdv": {
                  "type": "string",
                  "description": "Fully Diluted Valuation"
                },
                "mcap": {
                  "type": "string",
                  "description": "Market capitalization"
                },
                "ts": {
                  "type": "string",
                  "description": "Total token supply"
                },
                "bs": {
                  "type": "string",
                  "description": "Burned supply"
                },
                "cs": {
                  "type": "string",
                  "description": "Circulating supply"
                },
                "liqUsd": {
                  "type": "string",
                  "description": "Liquidity (USD)"
                },
                "liq": {
                  "type": "string",
                  "description": "Liquidity (native)"
                },
                "hld": {
                  "type": "integer",
                  "description": "Holder count",
                  "format": "int64"
                },
                "p": {
                  "type": "string",
                  "description": "Token price in USD"
                },
                "ph24h": {
                  "type": "string",
                  "description": "24h price high"
                },
                "pl24h": {
                  "type": "string",
                  "description": "24h price low"
                },
                "pt": {
                  "type": "integer",
                  "description": "Price last updated timestamp",
                  "format": "int64"
                },
                "fpt": {
                  "type": "integer",
                  "description": "Timestamp of the first time this token had a price",
                  "format": "int64"
                },
                "fpct": {
                  "type": "integer",
                  "description": "Timestamp when the first pool for this token was created",
                  "format": "int64"
                },
                "bcr": {
                  "type": "number",
                  "description": "Bonding curve ratio",
                  "format": "double"
                },
                "sts": {
                  "type": "array",
                  "description": "Token statistics",
                  "items": {
                    "type": "object",
                    "properties": {
                      "tp": {
                        "type": "string",
                        "description": "Stat type, e.g., '1h', '24h', '7d'",
                        "example": "24h"
                      },
                      "vu": {
                        "type": "string",
                        "description": "Total volume (string formatted)",
                        "example": "123456.789"
                      },
                      "txs": {
                        "type": "integer",
                        "description": "Total number of transactions",
                        "format": "int64",
                        "example": 1024
                      },
                      "nb": {
                        "type": "integer",
                        "description": "Number of buy transactions",
                        "format": "int64",
                        "example": 678
                      },
                      "ns": {
                        "type": "integer",
                        "description": "Number of sell transactions",
                        "format": "int64",
                        "example": 346
                      },
                      "bvu": {
                        "type": "string",
                        "description": "Buy volume",
                        "example": "65432.12"
                      },
                      "svu": {
                        "type": "string",
                        "description": "Sell volume",
                        "example": "58024.67"
                      },
                      "but": {
                        "type": "integer",
                        "description": "Number of unique buyers",
                        "format": "int64",
                        "example": 431
                      },
                      "sut": {
                        "type": "integer",
                        "description": "Number of unique sellers",
                        "format": "int64",
                        "example": 398
                      },
                      "pc": {
                        "type": "number",
                        "description": "Price change rate (e.g. 5.23 means +5.23%)",
                        "format": "float",
                        "example": 3.51
                      },
                      "ut": {
                        "type": "integer",
                        "description": "Number of unique traders",
                        "format": "int64",
                        "example": 789
                      }
                    },
                    "description": "Statistics data for token in specific interval",
                    "__$ref": "#/components/schemas/TokenStatsDTO"
                  }
                },
                "pls": {
                  "type": "array",
                  "description": "Top liquidity pools",
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
                },
                "turl": {
                  "type": "string",
                  "description": "DEX trading URL"
                },
                "nps": {
                  "type": "integer",
                  "description": "Number of top pools",
                  "format": "int64"
                },
                "tsrc": {
                  "type": "string",
                  "description": "Pool source"
                },
                "rl": {
                  "type": "string",
                  "description": "Token risk level"
                },
                "lf": {
                  "type": "integer",
                  "description": "Listed flag (1 = listed, 0 = unlisted)",
                  "format": "int32"
                },
                "cid": {
                  "type": "integer",
                  "description": "Crypto currency ID",
                  "format": "int32"
                },
                "lmc": {
                  "type": "string",
                  "description": "Listing market capitalization"
                },
                "lsmc": {
                  "type": "string",
                  "description": "Listing self-reported market capitalization"
                },
                "lsrcs": {
                  "type": "string",
                  "description": "Listing self-reported circulating supply"
                },
                "ltcs": {
                  "type": "string",
                  "description": "Listing circulating supply"
                },
                "ltda": {
                  "type": "integer",
                  "description": "Listing token date added",
                  "format": "int64"
                },
                "cexs": {
                  "type": "array",
                  "description": "Centralized exchange listings",
                  "items": {
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "integer",
                        "description": "Exchange ID, e.g. 270",
                        "format": "int32"
                      },
                      "slug": {
                        "type": "string",
                        "description": "Exchange slug, e.g. binance"
                      },
                      "n": {
                        "type": "string",
                        "description": "Full exchange name, e.g. Binance"
                      },
                      "lg": {
                        "type": "string",
                        "description": "Logo URL, e.g. https://s2.coinmarketcap.com/static/img/exchanges/64x64/270.png"
                      },
                      "wst": {
                        "type": "string",
                        "description": "Exchange website URL"
                      },
                      "cat": {
                        "type": "array",
                        "description": "Exchange categories, e.g. SPOT, DERIVATIVES",
                        "items": {
                          "type": "string",
                          "description": "Exchange categories, e.g. SPOT, DERIVATIVES"
                        }
                      }
                    },
                    "description": "Centralized exchange information",
                    "__$ref": "#/components/schemas/CryptoCurrencyExchangeDTO"
                  }
                },
                "sig": {
                  "type": "object",
                  "properties": {
                    "mtp": {
                      "type": "number",
                      "description": "highestPrice / firstSignalPrice"
                    },
                    "psc": {
                      "type": "integer",
                      "description": "push count",
                      "format": "int64"
                    }
                  },
                  "description": "Token signal",
                  "__$ref": "#/components/schemas/DexTokenSignalDTO"
                },
                "ecs": {
                  "type": "integer",
                  "description": "Binance exclusive code, 1 - exclusive",
                  "format": "int32"
                },
                "la": {
                  "type": "integer",
                  "description": "show listed alert, 1-show,0-hide",
                  "format": "int32"
                }
              },
              "description": "Detailed token information",
              "__$ref": "#/components/schemas/TokenDetailDTO"
            }
          }
        }
      ]
    }
  ]
}
```
