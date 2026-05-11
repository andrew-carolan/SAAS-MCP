# GET /v1/exchange/market-pairs/latest

**Summary:** Market Pairs Latest

**Description:** Returns all active market pairs that CoinMarketCap tracks for a given exchange. The latest price and volume information is returned for each market. Use the "convert" option to return market values in multiple fiat and cryptocurrency conversions in the same call.'

  **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
  - ~~Basic~~
  - ~~Hobbyist~~
  - ~~Startup~~
  - Standard
  - Professional
  - Enterprise

**Cache / Update frequency:** Every 60 seconds.  
**Plan credit use:** 1 call credit per 100 market pairs returned (rounded up) and 1 call credit per `convert` option beyond the first.  
**CMC equivalent pages:** Our exchange level active markets pages like [coinmarketcap.com/exchanges/binance/](https://coinmarketcap.com/exchanges/binance/).  

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **id** (query) - *Optional*: A CoinMarketCap exchange ID. Example: "1"
- **slug** (query) - *Optional*: Alternatively pass an exchange "slug" (URL friendly all lowercase shorthand version of name with spaces replaced with hyphens). Example: "binance". One "id" *or* "slug" is required.
- **start** (query) - *Optional*: Optionally offset the start (1-based index) of the paginated list of items to return.
- **limit** (query) - *Optional*: Optionally specify the number of results to return. Use this parameter and the "start" parameter to determine your own pagination size.
- **aux** (query) - *Optional*: Optionally specify a comma-separated list of supplemental data fields to return. Pass `num_market_pairs,category,fee_type,market_url,currency_name,currency_slug,price_quote,effective_liquidity,market_score,market_reputation` to include all auxiliary fields.
- **matched_id** (query) - *Optional*: Optionally include one or more comma-delimited fiat or cryptocurrency IDs to filter market pairs by. For example `?matched_id=2781` would only return BTC markets that matched: "BTC/USD" or "USD/BTC" for the requested exchange. This parameter cannot be used when `matched_symbol` is used.
- **matched_symbol** (query) - *Optional*: Optionally include one or more comma-delimited fiat or cryptocurrency symbols to filter market pairs by. For example `?matched_symbol=USD` would only return BTC markets that matched: "BTC/USD" or "USD/BTC" for the requested exchange. This parameter cannot be used when `matched_id` is used.
- **category** (query) - *Optional*: The category of trading this market falls under. Spot markets are the most common but options include derivatives and OTC.
- **fee_type** (query) - *Optional*: The fee type the exchange enforces for this market.
- **convert** (query) - *Optional*: Optionally calculate market quotes in up to 120 currencies at once by passing a comma-separated list of cryptocurrency or fiat currency symbols. Each additional convert option beyond the first requires an additional call credit. A list of supported fiat options can be found [here](/guides/standards-and-conventions). Each conversion is returned in its own "quote" object.
- **convert_id** (query) - *Optional*: Optionally calculate market quotes by CoinMarketCap ID instead of symbol. This option is identical to `convert` outside of ID format. Ex: convert_id=1,2781 would replace convert=BTC,USD in your query. This parameter cannot be used when `convert` is used.

### Raw Data

```json
{
  "slug": "market-pairs-latest",
  "summary": "Market Pairs Latest",
  "method": "get",
  "description": "Returns all active market pairs that CoinMarketCap tracks for a given exchange. The latest price and volume information is returned for each market. Use the \"convert\" option to return market values in multiple fiat and cryptocurrency conversions in the same call.'\n\n  **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**\n  - ~~Basic~~\n  - ~~Hobbyist~~\n  - ~~Startup~~\n  - Standard\n  - Professional\n  - Enterprise\n\n**Cache / Update frequency:** Every 60 seconds.  \n**Plan credit use:** 1 call credit per 100 market pairs returned (rounded up) and 1 call credit per `convert` option beyond the first.  \n**CMC equivalent pages:** Our exchange level active markets pages like [coinmarketcap.com/exchanges/binance/](https://coinmarketcap.com/exchanges/binance/).  ",
  "operationId": "getV1ExchangeMarketpairsLatest",
  "contentTypes": [],
  "path": "/v1/exchange/market-pairs/latest",
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
      "name": "id",
      "in": "query",
      "description": "A CoinMarketCap exchange ID. Example: \"1\"",
      "required": null,
      "schema": {
        "type": "string",
        "pattern": "^\\d*$"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "slug",
      "in": "query",
      "description": "Alternatively pass an exchange \"slug\" (URL friendly all lowercase shorthand version of name with spaces replaced with hyphens). Example: \"binance\". One \"id\" *or* \"slug\" is required.",
      "required": null,
      "schema": {
        "type": "string",
        "pattern": "^[0-9a-z-]*$"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "start",
      "in": "query",
      "description": "Optionally offset the start (1-based index) of the paginated list of items to return.",
      "required": null,
      "schema": {
        "type": "integer",
        "minimum": 1,
        "default": 1
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "limit",
      "in": "query",
      "description": "Optionally specify the number of results to return. Use this parameter and the \"start\" parameter to determine your own pagination size.",
      "required": null,
      "schema": {
        "type": "integer",
        "minimum": 1,
        "maximum": 5000,
        "default": 100
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "aux",
      "in": "query",
      "description": "Optionally specify a comma-separated list of supplemental data fields to return. Pass `num_market_pairs,category,fee_type,market_url,currency_name,currency_slug,price_quote,effective_liquidity,market_score,market_reputation` to include all auxiliary fields.",
      "required": null,
      "schema": {
        "type": "string",
        "pattern": "^(num_market_pairs|category|fee_type|market_url|currency_name|currency_slug|price_quote|effective_liquidity|market_score|market_reputation)+(?:,(num_market_pairs|category|fee_type|market_url|currency_name|currency_slug|price_quote|effective_liquidity|market_score|market_reputation)+)*$",
        "default": "num_market_pairs,category,fee_type"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "matched_id",
      "in": "query",
      "description": "Optionally include one or more comma-delimited fiat or cryptocurrency IDs to filter market pairs by. For example `?matched_id=2781` would only return BTC markets that matched: \"BTC/USD\" or \"USD/BTC\" for the requested exchange. This parameter cannot be used when `matched_symbol` is used.",
      "required": null,
      "schema": {
        "type": "string",
        "pattern": "^\\d+(?:,\\d+)*$"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "matched_symbol",
      "in": "query",
      "description": "Optionally include one or more comma-delimited fiat or cryptocurrency symbols to filter market pairs by. For example `?matched_symbol=USD` would only return BTC markets that matched: \"BTC/USD\" or \"USD/BTC\" for the requested exchange. This parameter cannot be used when `matched_id` is used.",
      "required": null,
      "schema": {
        "type": "string",
        "pattern": "^[0-9A-Za-z$@\\-,]+(?:,[0-9A-Za-z$@\\-]+)*$"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "category",
      "in": "query",
      "description": "The category of trading this market falls under. Spot markets are the most common but options include derivatives and OTC.",
      "required": null,
      "schema": {
        "type": "string",
        "enum": [
          "all",
          "spot",
          "derivatives",
          "otc",
          "futures",
          "perpetual"
        ],
        "default": "all"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "fee_type",
      "in": "query",
      "description": "The fee type the exchange enforces for this market.",
      "required": null,
      "schema": {
        "type": "string",
        "enum": [
          "all",
          "percentage",
          "no-fees",
          "transactional-mining",
          "unknown"
        ],
        "default": "all"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "convert",
      "in": "query",
      "description": "Optionally calculate market quotes in up to 120 currencies at once by passing a comma-separated list of cryptocurrency or fiat currency symbols. Each additional convert option beyond the first requires an additional call credit. A list of supported fiat options can be found [here](/guides/standards-and-conventions). Each conversion is returned in its own \"quote\" object.",
      "required": null,
      "schema": {
        "type": "string",
        "pattern": "^[0-9A-Za-z$@\\-,]+(?:,[0-9A-Za-z$@\\-]+)*$"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "convert_id",
      "in": "query",
      "description": "Optionally calculate market quotes by CoinMarketCap ID instead of symbol. This option is identical to `convert` outside of ID format. Ex: convert_id=1,2781 would replace convert=BTC,USD in your query. This parameter cannot be used when `convert` is used.",
      "required": null,
      "schema": {
        "type": "string",
        "pattern": "^\\d+(?:,\\d+)*$"
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
      "description": "Successful",
      "content": [
        {
          "examples": [],
          "mediaType": "application/json",
          "encoding": null,
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "type": "object",
                "description": "Results of your query returned as an object.",
                "example": {
                  "id": 270,
                  "name": "Binance",
                  "slug": "binance",
                  "num_market_pairs": 473,
                  "volume_24h": 769291636.239632,
                  "market_pairs": [
                    {
                      "market_id": 9933,
                      "market_pair": "BTC/USDT",
                      "category": "spot",
                      "fee_type": "percentage",
                      "outlier_detected": 0,
                      "exclusions": null,
                      "market_pair_base": {
                        "currency_id": 1,
                        "currency_symbol": "BTC",
                        "exchange_symbol": "BTC",
                        "currency_type": "cryptocurrency"
                      },
                      "market_pair_quote": {
                        "currency_id": 825,
                        "currency_symbol": "USDT",
                        "exchange_symbol": "USDT",
                        "currency_type": "cryptocurrency"
                      },
                      "quote": {
                        "exchange_reported": {
                          "price": 7901.83,
                          "volume_24h_base": 47251.3345550653,
                          "volume_24h_quote": 373372012.927251,
                          "volume_percentage": 19.4346563602467,
                          "last_updated": "2019-05-24T01:40:10.000Z"
                        },
                        "USD": {
                          "price": 7933.66233493434,
                          "volume_24h": 374876133.234903,
                          "depth_negative_two": 40654.68019906,
                          "depth_positive_two": 17352.9964811,
                          "last_updated": "2019-05-24T01:40:10.000Z"
                        }
                      }
                    },
                    {
                      "market_id": 36329,
                      "market_pair": "MATIC/BTC",
                      "category": "spot",
                      "fee_type": "percentage",
                      "outlier_detected": 0,
                      "exclusions": null,
                      "market_pair_base": {
                        "currency_id": 3890,
                        "currency_symbol": "MATIC",
                        "exchange_symbol": "MATIC",
                        "currency_type": "cryptocurrency"
                      },
                      "market_pair_quote": {
                        "currency_id": 1,
                        "currency_symbol": "BTC",
                        "exchange_symbol": "BTC",
                        "currency_type": "cryptocurrency"
                      },
                      "quote": {
                        "exchange_reported": {
                          "price": 3.4e-06,
                          "volume_24h_base": 8773968381.05,
                          "volume_24h_quote": 29831.49249557,
                          "volume_percentage": 19.4346563602467,
                          "last_updated": "2019-05-24T01:41:16.000Z"
                        },
                        "USD": {
                          "price": 0.0269295015799739,
                          "volume_24h": 236278595.380127,
                          "depth_negative_two": 40654.68019906,
                          "depth_positive_two": 17352.9964811,
                          "last_updated": "2019-05-24T01:41:16.000Z"
                        }
                      }
                    }
                  ]
                },
                "properties": {
                  "id": {
                    "type": "integer",
                    "description": "The CoinMarketCap ID for this exchange.",
                    "example": 1
                  },
                  "name": {
                    "type": "string",
                    "description": "The name of this exchange.",
                    "example": "Binance"
                  },
                  "slug": {
                    "type": "string",
                    "description": "The slug for this exchange.",
                    "example": "binance"
                  },
                  "num_market_pairs": {
                    "type": "integer",
                    "description": "The number of market pairs that are open for trading on this exchange.",
                    "example": 303
                  },
                  "volume_24h": {
                    "type": "number",
                    "description": "Reported 24 hour volume in USD.",
                    "example": 768478308.529847
                  },
                  "market_pairs": {
                    "type": "array",
                    "description": "Array of all active market pairs for this exchange.",
                    "items": {
                      "type": "object",
                      "description": "Market Pair info object.",
                      "properties": {
                        "market_id": {
                          "type": "integer",
                          "description": "The CoinMarketCap ID for this market pair. This ID can reliably be used to identify this unique market as the ID never changes.",
                          "example": 9933
                        },
                        "market_pair": {
                          "type": "string",
                          "description": "The name of this market pair. Example: \"BTC/USD\"",
                          "example": "BTC/USD"
                        },
                        "category": {
                          "type": "string",
                          "description": "The category of trading this market falls under. Spot markets are the most common but options include derivatives and OTC.",
                          "example": "spot",
                          "enum": [
                            "spot",
                            "derivatives",
                            "otc"
                          ]
                        },
                        "fee_type": {
                          "type": "string",
                          "description": "The fee type the exchange enforces for this market.",
                          "example": "percentage",
                          "enum": [
                            "percentage",
                            "no-fees",
                            "transactional-mining",
                            "unknown"
                          ]
                        },
                        "market_url": {
                          "type": "string",
                          "description": "The URL to this market's trading page on the exchange if available. If not available the exchange's homepage URL is returned. *This field is only returned if requested through the `aux` request parameter.*",
                          "example": "https://www.binance.com/en/trade/BTC_USDT"
                        },
                        "quote": {
                          "type": "object",
                          "description": "Market Pair quotes object containing key->quote objects for each convert option requested. USD and \"exchange_reported\" are defaults.",
                          "properties": {
                            "exchange_reported": {
                              "type": "object",
                              "description": "A default exchange reported quote containing raw exchange reported values.",
                              "properties": {
                                "price": {
                                  "type": "number",
                                  "description": "The last exchange reported price for this market pair in quote currency units.",
                                  "example": 8000.23
                                },
                                "volume_24h_base": {
                                  "type": "number",
                                  "description": "The last exchange reported 24 hour volume for this market pair in base cryptocurrency units.",
                                  "example": 30768
                                },
                                "volume_24h_quote": {
                                  "type": "number",
                                  "description": "The last exchange reported 24 hour volume for this market pair in quote cryptocurrency units.",
                                  "example": 250448443.2
                                },
                                "volume_percentage": {
                                  "type": "number",
                                  "description": "Percentage of total exchange volume_24h",
                                  "example": 0.03
                                },
                                "last_updated": {
                                  "type": "string",
                                  "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                                  "description": "Timestamp (ISO 8601) of the last time this market data was updated.",
                                  "example": "2018-06-02T23:59:59.999Z"
                                }
                              },
                              "required": [
                                "price",
                                "volume_24h_base",
                                "volume_24h_quote",
                                "volume_percentage",
                                "last_updated"
                              ],
                              "__$ref": "#/components/schemas/Exchange_Market_Pairs_Latest_-_Market_Pair_Exchange_Reported_Quote"
                            }
                          },
                          "required": [
                            "exchange_reported"
                          ],
                          "additionalProperties": {
                            "type": "object",
                            "description": "One or more market quotes where $key is the conversion currency requested, ex. USD",
                            "properties": {
                              "price": {
                                "type": "number",
                                "description": "The last reported exchange price for this market pair converted into the requested convert currency.",
                                "example": 8000.23
                              },
                              "price_quote": {
                                "type": "number",
                                "description": "The latest exchange reported price in base units converted into the requested convert currency. *This field is only returned if requested through the `aux` request parameter.*",
                                "example": 8000.23
                              },
                              "volume_24h": {
                                "type": "number",
                                "description": "The last reported exchange volume for this market pair converted into the requested convert currency.",
                                "example": 1600000
                              },
                              "depth_negative_two": {
                                "type": "number",
                                "description": "-2% Depth in the specified currency.",
                                "example": 1600000
                              },
                              "depth_positive_two": {
                                "type": "number",
                                "description": "+2% Depth in the specified currency.",
                                "example": 1600000
                              },
                              "effective_liquidity": {
                                "type": "string",
                                "x-hidden": true
                              },
                              "market_score": {
                                "type": "string",
                                "x-hidden": true
                              },
                              "market_reputation": {
                                "type": "string",
                                "x-hidden": true
                              },
                              "last_updated": {
                                "type": "string",
                                "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                                "description": "Timestamp (ISO 8601) of when the conversion currency's current value was referenced for this conversion.",
                                "example": "2018-06-02T23:59:59.999Z"
                              }
                            },
                            "required": [
                              "price",
                              "volume_24h",
                              "last_updated"
                            ],
                            "__$ref": "#/components/schemas/Exchange_Market_Pairs_Latest_-_Market_Pair_Quote"
                          },
                          "__$ref": "#/components/schemas/Exchange_Market_Pairs_Latest_-_Market_Pair_Quote_object"
                        },
                        "market_pair_base": {
                          "type": "object",
                          "description": "Base currency details object for this market pair.",
                          "properties": {
                            "currency_id": {
                              "type": "integer",
                              "description": "The CoinMarketCap ID for the base currency in this market pair.",
                              "example": 1
                            },
                            "currency_name": {
                              "type": "string",
                              "description": "The name of this cryptocurrency. *This field is only returned if requested through the `aux` request parameter.*",
                              "example": "Bitcoin"
                            },
                            "currency_symbol": {
                              "type": "string",
                              "description": "The symbol for the base currency in this market pair.",
                              "example": "BTC"
                            },
                            "exchange_symbol": {
                              "type": "string",
                              "description": "The exchange reported symbol for the base currency in this market pair. In most cases this is identical to CoinMarketCap's symbol but it may differ if the exchange uses an outdated or contentious symbol that contrasts with the majority of other markets.",
                              "example": "BTC"
                            },
                            "currency_slug": {
                              "type": "string",
                              "description": "The web URL friendly shorthand version of this cryptocurrency name. *This field is only returned if requested through the `aux` request parameter.*",
                              "example": "bitcoin"
                            },
                            "currency_type": {
                              "type": "string",
                              "description": "The currency type for the base currency in this market pair.",
                              "example": "cryptocurrency",
                              "enum": [
                                "cryptocurrency",
                                "fiat"
                              ]
                            }
                          },
                          "required": [
                            "currency_id",
                            "currency_symbol",
                            "exchange_symbol",
                            "currency_type"
                          ],
                          "__$ref": "#/components/schemas/Exchange_Market_Pairs_Latest_-_Pair_Base_Currency_Info_object"
                        },
                        "market_pair_quote": {
                          "type": "object",
                          "description": "Quote (secondary) currency details object for this market pair",
                          "properties": {
                            "currency_id": {
                              "type": "integer",
                              "description": "The CoinMarketCap ID for the quote (secondary) currency in this market pair.",
                              "example": 2781
                            },
                            "currency_name": {
                              "type": "string",
                              "description": "The name of this cryptocurrency. *This field is only returned if requested through the `aux` request parameter.*",
                              "example": "Bitcoin"
                            },
                            "currency_symbol": {
                              "type": "string",
                              "description": "The symbol for the quote (secondary) currency in this market pair.",
                              "example": "USD"
                            },
                            "exchange_symbol": {
                              "type": "string",
                              "description": "The exchange reported symbol for the quote (secondary) currency in this market pair. In most cases this is identical to CoinMarketCap's symbol but it may differ if the exchange uses an outdated or contentious symbol that contrasts with the majority of other markets.",
                              "example": "USD"
                            },
                            "currency_slug": {
                              "type": "string",
                              "description": "The web URL friendly shorthand version of this cryptocurrency name. *This field is only returned if requested through the `aux` request parameter.*",
                              "example": "bitcoin"
                            },
                            "currency_type": {
                              "type": "string",
                              "description": "The currency type for the quote (secondary) currency in this market pair.",
                              "example": "fiat",
                              "enum": [
                                "cryptocurrency",
                                "fiat"
                              ]
                            }
                          },
                          "required": [
                            "currency_id",
                            "currency_symbol",
                            "exchange_symbol",
                            "currency_type"
                          ],
                          "__$ref": "#/components/schemas/Exchange_Market_Pairs_Latest_-_Pair_Base_Currency_Info_object_1"
                        }
                      },
                      "required": [
                        "market_id",
                        "market_pair",
                        "category",
                        "market_pair_base",
                        "market_pair_quote",
                        "quote"
                      ],
                      "__$ref": "#/components/schemas/Exchange_Market_Pairs_Latest_-_Market_Pair_Info_object"
                    },
                    "required": [
                      "Exchange Market Pairs Latest - Market Pair Info object"
                    ],
                    "__$ref": "#/components/schemas/Exchange_Market_Pairs_Latest_-_Market_Pairs_array"
                  }
                },
                "required": [
                  "id",
                  "name",
                  "slug",
                  "num_market_pairs",
                  "volume_24h",
                  "market_pairs"
                ],
                "__$ref": "#/components/schemas/Exchange_Market_Pairs_Latest_-_Results_object"
              },
              "status": {
                "type": "object",
                "description": "Standardized status object for API calls.",
                "properties": {
                  "timestamp": {
                    "type": "string",
                    "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                    "description": "Current timestamp (ISO 8601) on the server.",
                    "example": "2026-03-05T22:43:48.471Z"
                  },
                  "error_code": {
                    "type": "integer",
                    "description": "An internal error code for the current error. If a unique platform error code is not available the HTTP status code is returned. `null` is returned if there is no error."
                  },
                  "error_message": {
                    "type": [
                      "string",
                      "null"
                    ],
                    "description": "An error message to go along with the error code.",
                    "example": ""
                  },
                  "elapsed": {
                    "type": "integer",
                    "description": "Number of milliseconds taken to generate this response.",
                    "example": 10
                  },
                  "credit_count": {
                    "type": "integer",
                    "description": "Number of API call credits that were used for this call.",
                    "example": 1
                  },
                  "notice": {
                    "type": [
                      "string",
                      "null"
                    ],
                    "description": "Optional notice about API key information.",
                    "example": ""
                  }
                },
                "required": [
                  "timestamp",
                  "error_code",
                  "error_message",
                  "elapsed",
                  "credit_count"
                ],
                "__$ref": "#/components/schemas/API_Status_Object"
              }
            },
            "required": [
              "data"
            ],
            "__$ref": "#/components/schemas/Exchange_Market_Pairs_Latest_-_Response_Model"
          }
        }
      ]
    },
    {
      "statusCode": "400",
      "links": null,
      "description": "Bad Request",
      "content": [
        {
          "examples": [],
          "mediaType": "application/json",
          "encoding": null,
          "schema": {
            "type": "object",
            "description": "Bad Request",
            "properties": {
              "status": {
                "type": "object",
                "properties": {
                  "timestamp": {
                    "type": "string",
                    "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                    "description": "Current ISO 8601 timestamp on the server.",
                    "example": "2018-06-02T22:51:28.209Z"
                  },
                  "error_code": {
                    "type": "integer",
                    "description": "An internal error code for the current error. If a unique platform error code is not available the HTTP status code is returned.",
                    "example": 400,
                    "default": 400
                  },
                  "error_message": {
                    "type": "string",
                    "description": "An error message to go along with the error code.",
                    "example": "Invalid value for \\\"id\\\""
                  },
                  "elapsed": {
                    "type": "integer",
                    "description": "Number of milliseconds taken to generate this response",
                    "example": 10
                  },
                  "credit_count": {
                    "type": "integer",
                    "description": "Number of API call credits required for this call. Always 0 for errors.",
                    "example": 0
                  }
                },
                "required": [
                  "timestamp",
                  "error_code",
                  "error_message",
                  "elapsed",
                  "credit_count"
                ],
                "__$ref": "#/components/schemas/status"
              }
            },
            "__$ref": "#/components/schemas/HTTP_Status_400_Error_Object"
          }
        }
      ]
    },
    {
      "statusCode": "401",
      "links": null,
      "description": "Unauthorized",
      "content": [
        {
          "examples": [],
          "mediaType": "application/json",
          "encoding": null,
          "schema": {
            "type": "object",
            "description": "Unauthorized",
            "properties": {
              "status": {
                "type": "object",
                "properties": {
                  "timestamp": {
                    "type": "string",
                    "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                    "description": "Current ISO 8601 timestamp on the server.",
                    "example": "2018-06-02T22:51:28.209Z"
                  },
                  "error_code": {
                    "type": "integer",
                    "description": "An internal error code for the current error. If a unique platform error code is not available the HTTP status code is returned.",
                    "example": 1002,
                    "default": 401
                  },
                  "error_message": {
                    "type": "string",
                    "description": "An error message to go along with the error code.",
                    "example": "API key missing."
                  },
                  "elapsed": {
                    "type": "integer",
                    "description": "Number of milliseconds taken to generate this response",
                    "example": 10
                  },
                  "credit_count": {
                    "type": "integer",
                    "description": "Number of API call credits required for this call. Always 0 for errors.",
                    "example": 0
                  }
                },
                "required": [
                  "timestamp",
                  "error_code",
                  "error_message",
                  "elapsed",
                  "credit_count"
                ],
                "__$ref": "#/components/schemas/status_1"
              }
            },
            "__$ref": "#/components/schemas/HTTP_Status_401_Error_Object"
          }
        }
      ]
    },
    {
      "statusCode": "403",
      "links": null,
      "description": "Forbidden",
      "content": [
        {
          "examples": [],
          "mediaType": "application/json",
          "encoding": null,
          "schema": {
            "type": "object",
            "description": "Forbidden",
            "properties": {
              "status": {
                "type": "object",
                "properties": {
                  "timestamp": {
                    "type": "string",
                    "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                    "description": "Current ISO 8601 timestamp on the server.",
                    "example": "2018-06-02T22:51:28.209Z"
                  },
                  "error_code": {
                    "type": "integer",
                    "description": "An internal error code for the current error. If a unique platform error code is not available the HTTP status code is returned.",
                    "example": 1006,
                    "default": 403
                  },
                  "error_message": {
                    "type": "string",
                    "description": "An error message to go along with the error code.",
                    "example": "Your API Key subscription plan doesn't support this endpoint."
                  },
                  "elapsed": {
                    "type": "integer",
                    "description": "Number of milliseconds taken to generate this response",
                    "example": 10
                  },
                  "credit_count": {
                    "type": "integer",
                    "description": "Number of API call credits required for this call. Always 0 for errors.",
                    "example": 0
                  }
                },
                "required": [
                  "timestamp",
                  "error_code",
                  "error_message",
                  "elapsed",
                  "credit_count"
                ],
                "__$ref": "#/components/schemas/status_2"
              }
            },
            "__$ref": "#/components/schemas/HTTP_Status_403_Error_Object"
          }
        }
      ]
    },
    {
      "statusCode": "429",
      "links": null,
      "description": "Too Many Requests",
      "content": [
        {
          "examples": [],
          "mediaType": "application/json",
          "encoding": null,
          "schema": {
            "type": "object",
            "description": "Too Many Requests",
            "properties": {
              "status": {
                "type": "object",
                "properties": {
                  "timestamp": {
                    "type": "string",
                    "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                    "description": "Current ISO 8601 timestamp on the server.",
                    "example": "2018-06-02T22:51:28.209Z"
                  },
                  "error_code": {
                    "type": "integer",
                    "description": "An internal error code string for the current error. If a unique platform error code is not available the HTTP status code is returned.",
                    "example": 1008,
                    "default": 429
                  },
                  "error_message": {
                    "type": "string",
                    "description": "An error message to go along with the error code.",
                    "example": "You've exceeded your API Key's HTTP request rate limit. Rate limits reset every minute."
                  },
                  "elapsed": {
                    "type": "integer",
                    "description": "Number of milliseconds taken to generate this response",
                    "example": 10
                  },
                  "credit_count": {
                    "type": "integer",
                    "description": "Number of API call credits required for this call. Always 0 for errors.",
                    "example": 0
                  }
                },
                "required": [
                  "timestamp",
                  "error_code",
                  "error_message",
                  "elapsed",
                  "credit_count"
                ],
                "__$ref": "#/components/schemas/status_3"
              }
            },
            "__$ref": "#/components/schemas/HTTP_Status_429_Error_Object"
          }
        }
      ]
    },
    {
      "statusCode": "500",
      "links": null,
      "description": "Internal Server Error",
      "content": [
        {
          "examples": [],
          "mediaType": "application/json",
          "encoding": null,
          "schema": {
            "type": "object",
            "description": "Internal Server Error",
            "properties": {
              "status": {
                "type": "object",
                "properties": {
                  "timestamp": {
                    "type": "string",
                    "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                    "description": "Current ISO 8601 timestamp on the server.",
                    "example": "2018-06-02T22:51:28.209Z"
                  },
                  "error_code": {
                    "type": "integer",
                    "description": "An internal error code string for the current error. If a unique platform error code is not available the HTTP status code is returned.",
                    "default": 500,
                    "enum": [
                      500
                    ]
                  },
                  "error_message": {
                    "type": "string",
                    "description": "An error message to go along with the error code.",
                    "example": "An internal server error occurred"
                  },
                  "elapsed": {
                    "type": "integer",
                    "description": "Number of milliseconds taken to generate this response",
                    "example": 10
                  },
                  "credit_count": {
                    "type": "integer",
                    "description": "Number of API call credits required for this call. Always 0 for errors.",
                    "example": 0
                  }
                },
                "required": [
                  "timestamp",
                  "error_code",
                  "error_message",
                  "elapsed",
                  "credit_count"
                ],
                "__$ref": "#/components/schemas/status_4"
              }
            },
            "__$ref": "#/components/schemas/HTTP_Status_500_Error_Object"
          }
        }
      ]
    }
  ]
}
```
