# GET /v1/global-metrics/quotes/latest

**Summary:** Quotes Latest

**Description:** Returns the latest global cryptocurrency market metrics. Use the "convert" option to return market values in multiple fiat and cryptocurrency conversions in the same call.

**This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
- Basic
- Hobbyist
- Startup
- Standard
- Professional
- Enterprise

**Cache / Update frequency:** Every 5 minute.   
**Plan credit use:** 1 call credit per call and 1 call credit per `convert` option beyond the first.   
**CMC equivalent pages:** The latest aggregate global market stats ticker across all CMC pages like [coinmarketcap.com](https://coinmarketcap.com/).  

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **convert** (query) - *Optional*: Optionally calculate market quotes in up to 120 currencies at once by passing a comma-separated list of cryptocurrency or fiat currency symbols. Each additional convert option beyond the first requires an additional call credit. A list of supported fiat options can be found [here](/guides/standards-and-conventions). Each conversion is returned in its own "quote" object.
- **convert_id** (query) - *Optional*: Optionally calculate market quotes by CoinMarketCap ID instead of symbol. This option is identical to `convert` outside of ID format. Ex: convert_id=1,2781 would replace convert=BTC,USD in your query. This parameter cannot be used when `convert` is used.

### Raw Data

```json
{
  "slug": "quotes-latest-2",
  "summary": "Quotes Latest",
  "method": "get",
  "description": "Returns the latest global cryptocurrency market metrics. Use the \"convert\" option to return market values in multiple fiat and cryptocurrency conversions in the same call.\n\n**This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**\n- Basic\n- Hobbyist\n- Startup\n- Standard\n- Professional\n- Enterprise\n\n**Cache / Update frequency:** Every 5 minute.   \n**Plan credit use:** 1 call credit per call and 1 call credit per `convert` option beyond the first.   \n**CMC equivalent pages:** The latest aggregate global market stats ticker across all CMC pages like [coinmarketcap.com](https://coinmarketcap.com/).  ",
  "operationId": "getV1GlobalmetricsQuotesLatest",
  "contentTypes": [],
  "path": "/v1/global-metrics/quotes/latest",
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
                "description": "Results object for your API call.",
                "properties": {
                  "btc_dominance": {
                    "type": "number",
                    "description": "Bitcoin's market dominance percentage by market cap.",
                    "example": 67.0057
                  },
                  "eth_dominance": {
                    "type": "number",
                    "description": "Ethereum's market dominance percentage by market cap.",
                    "example": 9.02205
                  },
                  "active_cryptocurrencies": {
                    "type": "number",
                    "description": "Count of active cryptocurrencies tracked by CoinMarketCap. This includes all cryptocurrencies with a `listing_status` of \"active\" or \"listed\" as returned from our /cryptocurrency/map call.",
                    "example": 2941
                  },
                  "total_cryptocurrencies": {
                    "type": "number",
                    "description": "Count of all cryptocurrencies tracked by CoinMarketCap. This includes \"inactive\" `listing_status` cryptocurrencies.",
                    "example": 4637
                  },
                  "active_market_pairs": {
                    "type": "number",
                    "description": "Count of active market pairs tracked by CoinMarketCap across all exchanges.",
                    "example": 21209
                  },
                  "active_exchanges": {
                    "type": "number",
                    "description": "Count of active exchanges tracked by CoinMarketCap. This includes all exchanges with a `listing_status` of \"active\" or \"listed\" as returned by our /exchange/map call.",
                    "example": 445
                  },
                  "total_exchanges": {
                    "type": "number",
                    "description": "Count of all exchanges tracked by CoinMarketCap. This includes \"inactive\" `listing_status` exchanges.",
                    "example": 677
                  },
                  "last_updated": {
                    "type": "string",
                    "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                    "description": "Timestamp of when this record was last updated.",
                    "example": "2019-05-16T18:47:00.000Z"
                  },
                  "quote": {
                    "type": "object",
                    "description": "A map of market quotes in different currency conversions. The default map included is USD.",
                    "example": {
                      "USD": {
                        "total_market_cap": 250284668020.67,
                        "total_volume_24h": 16903498628.86,
                        "total_volume_24h_reported": 16903498628.86,
                        "altcoin_volume_24h": 11883384723.14,
                        "altcoin_volume_24h_reported": 11883384723.14,
                        "altcoin_market_cap": 119597549931.01,
                        "last_updated": "2018-06-02T23:46:14.000Z"
                      }
                    },
                    "additionalProperties": {
                      "type": "object",
                      "description": "A market quote in the currency conversion option.",
                      "properties": {
                        "total_market_cap": {
                          "type": "number",
                          "description": "The sum of all individual cryptocurrency market capitalizations in the requested currency.",
                          "example": 250385096532.124
                        },
                        "total_volume_24h": {
                          "type": "number",
                          "description": "The sum of rolling 24 hour adjusted volume (as outlined in our methodology) for all cryptocurrencies in the requested currency.",
                          "example": 119270642406.968
                        },
                        "total_volume_24h_reported": {
                          "type": "number",
                          "description": "The sum of rolling 24 hour reported volume for all cryptocurrencies in the requested currency.",
                          "example": 1514905418.39087
                        },
                        "altcoin_volume_24h": {
                          "type": "number",
                          "description": "The sum of rolling 24 hour adjusted volume (as outlined in our methodology) for all cryptocurrencies excluding Bitcoin in the requested currency.",
                          "example": 119270642406.968
                        },
                        "altcoin_volume_24h_reported": {
                          "type": "number",
                          "description": "The sum of rolling 24 hour reported volume for all cryptocurrencies excluding Bitcoin in the requested currency.",
                          "example": 1514905418.39087
                        },
                        "altcoin_market_cap": {
                          "type": "number",
                          "description": "The sum of all individual cryptocurrency market capitalizations excluding Bitcoin in the requested currency.",
                          "example": 250385096532.124
                        },
                        "last_updated": {
                          "type": "string",
                          "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                          "description": "Timestamp (ISO 8601) of when the conversion currency's current value was referenced.",
                          "example": "2019-05-16T18:47:00.000Z"
                        }
                      },
                      "required": [
                        "total_market_cap",
                        "total_volume_24h",
                        "total_volume_24h_reported",
                        "altcoin_volume_24h",
                        "altcoin_volume_24h_reported",
                        "altcoin_market_cap",
                        "last_updated"
                      ],
                      "__$ref": "#/components/schemas/Global_Metrics_Quotes_Latest_-_Quote_object"
                    },
                    "__$ref": "#/components/schemas/Global_Metrics_Quotes_Latest_-_Quote_map"
                  }
                },
                "required": [
                  "active_cryptocurrencies",
                  "total_cryptocurrencies",
                  "active_market_pairs",
                  "active_exchanges",
                  "total_exchanges",
                  "last_updated",
                  "quote"
                ],
                "__$ref": "#/components/schemas/Global_Metrics_Quotes_Latest_-_Results_Object"
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
            "__$ref": "#/components/schemas/Global_Metrics_Quotes_Latest_-_Response_Model"
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
