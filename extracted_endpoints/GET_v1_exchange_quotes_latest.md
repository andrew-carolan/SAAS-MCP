# GET /v1/exchange/quotes/latest

**Summary:** Quotes Latest

**Description:** Returns the latest aggregate market data for 1 or more exchanges. Use the "convert" option to return market values in multiple fiat and cryptocurrency conversions in the same call.

**This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
- ~~Basic~~
- ~~Hobbyist~~
- ~~Startup~~
- Standard
- Professional
- Enterprise

**Cache / Update frequency:** Every 60 seconds.
**Plan credit use:** 1 call credit per 100 exchanges returned (rounded up) and 1 call credit per `convert` option beyond the first.
**CMC equivalent pages:** Latest market data summary for specific exchanges like [coinmarketcap.com/rankings/exchanges/](https://coinmarketcap.com/rankings/exchanges/).

***NOTE:** “exchange_score" will be deprecated on 4 November 2024.*

*After this date, the "exchange_score" field return null from these endpoints. We encourage users to review and update their implementations accordingly to avoid any disruptions.*

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **id** (query) - *Optional*: One or more comma-separated CoinMarketCap exchange IDs. Example: "1,2"
- **slug** (query) - *Optional*: Alternatively, pass a comma-separated list of exchange "slugs" (URL friendly all lowercase shorthand version of name with spaces replaced with hyphens). Example: "binance,gdax". At least one "id" *or* "slug" is required.
- **convert** (query) - *Optional*: Optionally calculate market quotes in up to 120 currencies at once by passing a comma-separated list of cryptocurrency or fiat currency symbols. Each additional convert option beyond the first requires an additional call credit. A list of supported fiat options can be found [here](/guides/standards-and-conventions). Each conversion is returned in its own "quote" object.
- **convert_id** (query) - *Optional*: Optionally calculate market quotes by CoinMarketCap ID instead of symbol. This option is identical to `convert` outside of ID format. Ex: convert_id=1,2781 would replace convert=BTC,USD in your query. This parameter cannot be used when `convert` is used.
- **aux** (query) - *Optional*: Optionally specify a comma-separated list of supplemental data fields to return. Pass `num_market_pairs,traffic_score,rank,exchange_score,liquidity_score,effective_liquidity_24h` to include all auxiliary fields.

### Raw Data

```json
{
  "slug": "quotes-latest",
  "summary": "Quotes Latest",
  "method": "get",
  "description": "Returns the latest aggregate market data for 1 or more exchanges. Use the \"convert\" option to return market values in multiple fiat and cryptocurrency conversions in the same call.\n\n**This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**\n- ~~Basic~~\n- ~~Hobbyist~~\n- ~~Startup~~\n- Standard\n- Professional\n- Enterprise\n\n**Cache / Update frequency:** Every 60 seconds.\n**Plan credit use:** 1 call credit per 100 exchanges returned (rounded up) and 1 call credit per `convert` option beyond the first.\n**CMC equivalent pages:** Latest market data summary for specific exchanges like [coinmarketcap.com/rankings/exchanges/](https://coinmarketcap.com/rankings/exchanges/).\n\n***NOTE:** \u201cexchange_score\" will be deprecated on 4 November 2024.*\n\n*After this date, the \"exchange_score\" field return null from these endpoints. We encourage users to review and update their implementations accordingly to avoid any disruptions.*",
  "operationId": "getV1ExchangeQuotesLatest",
  "contentTypes": [],
  "path": "/v1/exchange/quotes/latest",
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
      "description": "One or more comma-separated CoinMarketCap exchange IDs. Example: \"1,2\"",
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
      "name": "slug",
      "in": "query",
      "description": "Alternatively, pass a comma-separated list of exchange \"slugs\" (URL friendly all lowercase shorthand version of name with spaces replaced with hyphens). Example: \"binance,gdax\". At least one \"id\" *or* \"slug\" is required.",
      "required": null,
      "schema": {
        "type": "string",
        "pattern": "^[0-9a-z-]+(?:,[0-9a-z-]+)*$"
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
    },
    {
      "name": "aux",
      "in": "query",
      "description": "Optionally specify a comma-separated list of supplemental data fields to return. Pass `num_market_pairs,traffic_score,rank,exchange_score,liquidity_score,effective_liquidity_24h` to include all auxiliary fields.",
      "required": null,
      "schema": {
        "type": "string",
        "pattern": "^(num_market_pairs|traffic_score|rank|exchange_score|liquidity_score|effective_liquidity_24h)+(?:,(num_market_pairs|traffic_score|rank|exchange_score|liquidity_score|effective_liquidity_24h)+)*$",
        "default": "num_market_pairs,traffic_score,rank,exchange_score,liquidity_score,effective_liquidity_24h"
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
                "description": "A map of exchange objects by ID or slugs (as used in query parameters).",
                "example": {
                  "1": {
                    "id": 270,
                    "name": "Binance",
                    "slug": "binance",
                    "num_coins": 132,
                    "num_market_pairs": 385,
                    "last_updated": "2018-11-08T22:11:00.000Z",
                    "traffic_score": 1000,
                    "rank": 1,
                    "exchange_score": 9.8,
                    "liquidity_score": 9.8028,
                    "quote": {
                      "USD": {
                        "volume_24h": 768478308.529847,
                        "volume_24h_adjusted": 768478308.529847,
                        "volume_7d": 3666423776,
                        "volume_30d": 21338299776,
                        "percent_change_volume_24h": -11.8232,
                        "percent_change_volume_7d": 67.0306,
                        "percent_change_volume_30d": -0.0821558,
                        "effective_liquidity_24h": 629.9774,
                        "last_updated": "2018-11-08T22:18:00.000Z"
                      }
                    }
                  }
                },
                "additionalProperties": {
                  "type": "object",
                  "description": "An exchange object for each requested.",
                  "properties": {
                    "id": {
                      "type": "integer",
                      "description": "The CoinMarketCap exchange ID.",
                      "example": 1
                    },
                    "name": {
                      "type": "string",
                      "description": "The exchange name.",
                      "example": "Binance"
                    },
                    "slug": {
                      "type": "string",
                      "description": "The exchange slug.",
                      "example": "binance"
                    },
                    "num_market_pairs": {
                      "type": "integer",
                      "description": "The number of active trading pairs available for this exchange.",
                      "example": 500
                    },
                    "exchange_score": {
                      "type": "number",
                      "description": "The exchange score.",
                      "example": 9.8
                    },
                    "liquidity_score": {
                      "type": "number",
                      "description": "The liquidity score.",
                      "example": 9.8
                    },
                    "rank": {
                      "type": "integer",
                      "description": "The exchange rank.",
                      "example": 5
                    },
                    "traffic_score": {
                      "type": "number",
                      "description": "The traffic score.",
                      "example": 1000
                    },
                    "last_updated": {
                      "type": "string",
                      "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                      "description": "Timestamp (ISO 8601) of the last time this exchange's market data was updated.",
                      "example": "2018-06-02T00:00:00.000Z"
                    },
                    "quote": {
                      "type": "object",
                      "description": "A map of market quotes in different currency conversions. The default map included is USD.",
                      "additionalProperties": {
                        "type": "object",
                        "description": "A market quote in the currency conversion option.",
                        "properties": {
                          "last_updated": {
                            "type": "string",
                            "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                            "description": "Timestamp (ISO 8601) of when the conversion currency's current value was referenced for this conversion.",
                            "example": "2018-06-02T22:51:28.209Z"
                          },
                          "volume_24h": {
                            "type": "number",
                            "description": "Reported 24 hour volume in the specified currency.",
                            "example": 768478308.529847
                          },
                          "volume_24h_adjusted": {
                            "type": "number",
                            "description": "Adjusted 24 hour volume in the specified currency for spot markets excluding markets with no fees and transaction mining.",
                            "example": 768478308.529847
                          },
                          "volume_7d": {
                            "type": "number",
                            "description": "7 day volume in the specified currency.",
                            "example": 3666423776
                          },
                          "volume_30d": {
                            "type": "number",
                            "description": "30 day volume in the specified currency.",
                            "example": 21338299776
                          },
                          "percent_change_volume_24h": {
                            "type": "number",
                            "description": "24 hour percent change in the specified currency.",
                            "example": 0.03
                          },
                          "percent_change_volume_7d": {
                            "type": "number",
                            "description": "7 day percent change in the specified currency.",
                            "example": 5.75
                          },
                          "percent_change_volume_30d": {
                            "type": "number",
                            "description": "30 day percent change in the specified currency.",
                            "example": -19.64
                          },
                          "effective_liquidity_24h": {
                            "type": "number",
                            "description": "24 hour liquidity in the specified currency.",
                            "example": -19.64
                          },
                          "derivative_volume": {
                            "type": "number",
                            "description": "Reported 24 hour derivative volume in the specified currency.",
                            "example": 768478308.529847
                          },
                          "spot_volume": {
                            "type": "number",
                            "description": "Reported 24 hour spot volume in the specified currency.",
                            "example": 768478308.529847
                          }
                        },
                        "required": [
                          "last_updated",
                          "volume_24h",
                          "volume_24h_adjusted",
                          "volume_7d",
                          "volume_30d",
                          "percent_change_volume_24h",
                          "percent_change_volume_7d",
                          "percent_change_volume_30d"
                        ],
                        "__$ref": "#/components/schemas/Exchange_Quotes_Latest_-_Quote_object"
                      },
                      "__$ref": "#/components/schemas/Exchange_Quotes_Latest_-_Quote_map"
                    }
                  },
                  "required": [
                    "id",
                    "name",
                    "slug",
                    "num_market_pairs",
                    "last_updated",
                    "quote"
                  ],
                  "__$ref": "#/components/schemas/Exchange_Quotes_Latest_-_Exchange_object"
                },
                "__$ref": "#/components/schemas/Exchange_Quotes_Latest_-_Exchange_Results_map"
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
            "__$ref": "#/components/schemas/Exchange_Quotes_Latest_-_Response_Model"
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
