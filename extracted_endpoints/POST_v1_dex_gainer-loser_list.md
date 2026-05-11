# POST /v1/dex/gainer-loser/list

**Summary:** Get top gainers and losers

**Description:** Get list of top gainer and loser tokens

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key

### Raw Data

```json
{
  "slug": "get-top-gainers-and-losers",
  "summary": "Get top gainers and losers",
  "method": "post",
  "description": "Get list of top gainer and loser tokens",
  "operationId": "getGainerLoserList",
  "contentTypes": [
    "application/json"
  ],
  "path": "/v1/dex/gainer-loser/list",
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
            "platformIds": {
              "type": "string",
              "description": "Platform IDs, comma separated"
            },
            "interval": {
              "type": "string",
              "description": "Time interval"
            },
            "nextPageIndex": {
              "type": "string",
              "description": "Next page cursor"
            },
            "pageSize": {
              "type": "integer",
              "description": "Page size",
              "format": "int32"
            },
            "filter": {
              "type": "object",
              "properties": {
                "hideFourMeme": {
                  "type": "boolean",
                  "description": "Whether to hide four.meme tokens"
                },
                "hidePumpFun": {
                  "type": "boolean",
                  "description": "Whether to hide PumpFun tokens"
                },
                "hideMoonshot": {
                  "type": "boolean",
                  "description": "Whether to hide Moonshot tokens"
                },
                "auditPassed": {
                  "type": "boolean",
                  "description": "Only include tokens that passed audit"
                },
                "social": {
                  "type": "boolean",
                  "description": "Only include tokens with social media presence"
                },
                "minAge": {
                  "type": "integer",
                  "description": "Minimum token age in minutes",
                  "format": "int32"
                },
                "maxAge": {
                  "type": "integer",
                  "description": "Maximum token age in minutes",
                  "format": "int32"
                },
                "minMarketCap": {
                  "type": "number",
                  "description": "Minimum market cap (USD)"
                },
                "maxMarketCap": {
                  "type": "number",
                  "description": "Maximum market cap (USD)"
                },
                "minLiquidity": {
                  "type": "number",
                  "description": "Minimum liquidity (USD)"
                },
                "maxLiquidity": {
                  "type": "number",
                  "description": "Maximum liquidity (USD)"
                },
                "volume": {
                  "type": "array",
                  "description": "Volume filter ranges (e.g. 1000~5000)",
                  "items": {
                    "type": "object",
                    "properties": {
                      "min": {
                        "type": "string",
                        "description": "Minimum value as string, e.g., 1000"
                      },
                      "max": {
                        "type": "string",
                        "description": "Maximum value as string, e.g., 5000"
                      },
                      "type": {
                        "type": "string",
                        "description": "Metric type, e.g. Refer to RangeFilterStatType for valid values. 5m, 1h, 4h, 24h"
                      }
                    },
                    "description": "Generic range filter structure",
                    "__$ref": "#/components/schemas/RangeFilterDto"
                  }
                },
                "txns": {
                  "type": "array",
                  "description": "Transaction count filter ranges",
                  "items": {
                    "type": "object",
                    "properties": {
                      "min": {
                        "type": "string",
                        "description": "Minimum value as string, e.g., 1000"
                      },
                      "max": {
                        "type": "string",
                        "description": "Maximum value as string, e.g., 5000"
                      },
                      "type": {
                        "type": "string",
                        "description": "Metric type, e.g. Refer to RangeFilterStatType for valid values. 5m, 1h, 4h, 24h"
                      }
                    },
                    "description": "Generic range filter structure",
                    "__$ref": "#/components/schemas/RangeFilterDto"
                  }
                },
                "buys": {
                  "type": "array",
                  "description": "Buy count filter ranges",
                  "items": {
                    "type": "object",
                    "properties": {
                      "min": {
                        "type": "string",
                        "description": "Minimum value as string, e.g., 1000"
                      },
                      "max": {
                        "type": "string",
                        "description": "Maximum value as string, e.g., 5000"
                      },
                      "type": {
                        "type": "string",
                        "description": "Metric type, e.g. Refer to RangeFilterStatType for valid values. 5m, 1h, 4h, 24h"
                      }
                    },
                    "description": "Generic range filter structure",
                    "__$ref": "#/components/schemas/RangeFilterDto"
                  }
                },
                "sells": {
                  "type": "array",
                  "description": "Sell count filter ranges",
                  "items": {
                    "type": "object",
                    "properties": {
                      "min": {
                        "type": "string",
                        "description": "Minimum value as string, e.g., 1000"
                      },
                      "max": {
                        "type": "string",
                        "description": "Maximum value as string, e.g., 5000"
                      },
                      "type": {
                        "type": "string",
                        "description": "Metric type, e.g. Refer to RangeFilterStatType for valid values. 5m, 1h, 4h, 24h"
                      }
                    },
                    "description": "Generic range filter structure",
                    "__$ref": "#/components/schemas/RangeFilterDto"
                  }
                },
                "priceChange": {
                  "type": "array",
                  "description": "Price range filter ranges",
                  "items": {
                    "type": "object",
                    "properties": {
                      "min": {
                        "type": "string",
                        "description": "Minimum value as string, e.g., 1000"
                      },
                      "max": {
                        "type": "string",
                        "description": "Maximum value as string, e.g., 5000"
                      },
                      "type": {
                        "type": "string",
                        "description": "Metric type, e.g. Refer to RangeFilterStatType for valid values. 5m, 1h, 4h, 24h"
                      }
                    },
                    "description": "Generic range filter structure",
                    "__$ref": "#/components/schemas/RangeFilterDto"
                  }
                },
                "boostType": {
                  "type": "string",
                  "description": "Boost filter type",
                  "enum": [
                    "all, onlyBoost, hideBoost"
                  ]
                },
                "allFieldsEmpty": {
                  "type": "boolean"
                }
              },
              "description": "The request parameters for querying the token leaderboard",
              "__$ref": "#/components/schemas/LeaderboardFilterDTO"
            },
            "sortBy": {
              "type": "string",
              "description": "Sort field"
            },
            "sortType": {
              "type": "string",
              "description": "Sort type: asc or desc"
            }
          },
          "description": "Market list request",
          "__$ref": "#/components/schemas/DqueryMarketRequestDTO"
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
              "leaderboardList": {
                "type": "array",
                "description": "List of token leaderboard entries",
                "items": {
                  "type": "object",
                  "properties": {
                    "n": {
                      "type": "string",
                      "description": "Token name (n)"
                    },
                    "sym": {
                      "type": "string",
                      "description": "Token symbol (sym)"
                    },
                    "addr": {
                      "type": "string",
                      "description": "Token address (addr)"
                    },
                    "plt": {
                      "type": "string",
                      "description": "Token platform name (plt)"
                    },
                    "pid": {
                      "type": "integer",
                      "description": "Token platform ID (pid)",
                      "format": "int32"
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
                    "web": {
                      "type": "string",
                      "description": "Token website (web)"
                    },
                    "tw": {
                      "type": "string",
                      "description": "Twitter (tw)"
                    },
                    "tg": {
                      "type": "string",
                      "description": "Telegram (tg)"
                    },
                    "lg": {
                      "type": "string",
                      "description": "Logo URL (lg)"
                    },
                    "pubAt": {
                      "type": "integer",
                      "description": "Publish timestamp in ms (pubAt)",
                      "format": "int64"
                    },
                    "lchAt": {
                      "type": "integer",
                      "description": "Launch timestamp in ms (lchAt)",
                      "format": "int64"
                    },
                    "fdv": {
                      "type": "string",
                      "description": "Fully Diluted Valuation (fdv)"
                    },
                    "mcap": {
                      "type": "string",
                      "description": "Market Cap (mcap)"
                    },
                    "liqUsd": {
                      "type": "string",
                      "description": "Liquidity USD (liqUsd)"
                    },
                    "liq": {
                      "type": "string",
                      "description": "Liquidity (liq)"
                    },
                    "hld": {
                      "type": "integer",
                      "description": "Holder count (hld)",
                      "format": "int32"
                    },
                    "p": {
                      "type": "string",
                      "description": "Price USD (p)"
                    },
                    "np": {
                      "type": "string",
                      "description": "native Price (np)"
                    },
                    "pt": {
                      "type": "integer",
                      "description": "Price timestamp (pt)",
                      "format": "int64"
                    },
                    "v24h": {
                      "type": "string",
                      "description": "24h Volume USD (v24h)"
                    },
                    "t24h": {
                      "type": "string",
                      "description": "24h Transactions (t24h)"
                    },
                    "ch24h": {
                      "type": "string",
                      "description": "24h Price Change (ch24h)"
                    },
                    "thr": {
                      "type": "string",
                      "description": "Top Holder Rate (thr)"
                    },
                    "dhr": {
                      "type": "string",
                      "description": "Developer Holder Rate (dhr)"
                    },
                    "bcr": {
                      "type": "string",
                      "description": "Bonding Curve Ratio (bcr)"
                    },
                    "hcnt": {
                      "type": "integer",
                      "description": "Holder Count (hcnt)",
                      "format": "int32"
                    },
                    "tsrc": {
                      "type": "string",
                      "description": "token Source (src) \u2014 e.g. four.meme, pump.fun, moonshot"
                    },
                    "sts": {
                      "type": "array",
                      "description": "Token statistics (sts)",
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
                    "rl": {
                      "type": "string",
                      "description": "Token security status"
                    },
                    "ts": {
                      "type": "string",
                      "description": "total supply (ts)"
                    },
                    "bs": {
                      "type": "string",
                      "description": "burn supply (bs)"
                    },
                    "dec": {
                      "type": "integer",
                      "description": "decimals",
                      "format": "int32"
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
                    "beScore": {
                      "type": "number",
                      "description": "Meme binance exclusive Score",
                      "format": "double"
                    },
                    "beRank": {
                      "type": "integer",
                      "description": "Meme binance exclusive rank",
                      "format": "int32"
                    },
                    "pltA": {
                      "type": "string",
                      "description": "Token platform acronym name"
                    },
                    "ecs": {
                      "type": "integer",
                      "description": "Binance exclusive code, 1 - exclusive",
                      "format": "int32"
                    },
                    "tags": {
                      "type": "array",
                      "description": "Token tags",
                      "items": {
                        "type": "string",
                        "description": "Token tags"
                      }
                    }
                  },
                  "description": "Token leaderboard response DTO",
                  "__$ref": "#/components/schemas/TokenLeaderboardDTO"
                }
              },
              "pageNum": {
                "type": "integer",
                "description": "Current page number",
                "format": "int32"
              },
              "pageSize": {
                "type": "integer",
                "description": "Number of entries per page",
                "format": "int32"
              },
              "total": {
                "type": "integer",
                "description": "Total number of matching entries",
                "format": "int64"
              },
              "hasNextPage": {
                "type": "boolean",
                "description": "Whether there is another page after the current one"
              },
              "lastUpdateTime": {
                "type": "integer",
                "description": "Timestamp (in milliseconds) when the data was last updated",
                "format": "int64"
              },
              "nextPageIndex": {
                "type": "string",
                "description": "Cursor to be used for fetching the next page"
              }
            },
            "description": "Response object for the Gainer Leaderboard API",
            "__$ref": "#/components/schemas/GainerLeaderBoardResponseDTO"
          }
        }
      ]
    }
  ]
}
```
