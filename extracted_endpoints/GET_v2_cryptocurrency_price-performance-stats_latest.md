# GET /v2/cryptocurrency/price-performance-stats/latest

**Summary:** Price Performance Stats

**Description:** Returns price performance statistics for one or more cryptocurrencies including launch price ROI and all-time high / all-time low. Stats are returned for an `all_time` period by default. UTC `yesterday` and a number of *rolling time periods* may be requested using the `time_period` parameter. Utilize the `convert` parameter to translate values into multiple fiats or cryptocurrencies using historical rates.


**Please note**: This documentation relates to our updated V2 endpoint, which may be incompatible with our V1 versions. Documentation for deprecated endpoints can be found [the deprecated section](/pro-api-reference/deprecated).


  **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
  - ~~Basic~~
  - ~~Hobbyist~~
  - Startup
  - Standard
  - Professional
  - Enterprise

**Cache / Update frequency:** Every 60 seconds.  
**Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up) and 1 call credit per `convert` option beyond the first.  
**CMC equivalent pages:** The statistics module displayed on cryptocurrency pages like [Bitcoin](https://coinmarketcap.com/currencies/bitcoin/).     
  
***NOTE:** You may also use `/cryptocurrency/ohlcv/historical` for traditional OHLCV data at historical daily and hourly intervals. You may also use `/v1/cryptocurrency/ohlcv/latest` for OHLCV data for the current UTC day.* 

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **id** (query) - *Optional*: One or more comma-separated cryptocurrency CoinMarketCap IDs. Example: 1,2
- **slug** (query) - *Optional*: Alternatively pass a comma-separated list of cryptocurrency slugs. Example: "bitcoin,ethereum"
- **symbol** (query) - *Optional*: Alternatively pass one or more comma-separated cryptocurrency symbols. Example: "BTC,ETH". At least one "id" *or* "slug" *or* "symbol" is required for this request.
- **time_period** (query) - *Optional*: Specify one or more comma-delimited time periods to return stats for. `all_time` is the default. Pass `all_time,yesterday,24h,7d,30d,90d,365d` to return all supported time periods. All rolling periods have a rolling close time of the current request time. For example `24h` would have a close time of now and an open time of 24 hours before now. *Please note: `yesterday` is a UTC period and currently does not currently support `high` and `low` timestamps.*
- **convert** (query) - *Optional*: Optionally calculate quotes in up to 120 currencies at once by passing a comma-separated list of cryptocurrency or fiat currency symbols. Each additional convert option beyond the first requires an additional call credit. A list of supported fiat options can be found [here](/guides/standards-and-conventions). Each conversion is returned in its own "quote" object.
- **convert_id** (query) - *Optional*: Optionally calculate quotes by CoinMarketCap ID instead of symbol. This option is identical to `convert` outside of ID format. Ex: convert_id=1,2781 would replace convert=BTC,USD in your query. This parameter cannot be used when `convert` is used.
- **skip_invalid** (query) - *Optional*: Pass `true` to relax request validation rules. When requesting records on multiple cryptocurrencies an error is returned if no match is found for 1 or more requested cryptocurrencies. If set to true, invalid lookups will be skipped allowing valid cryptocurrencies to still be returned.

### Raw Data

```json
{
  "slug": "price-performance-stats",
  "summary": "Price Performance Stats",
  "method": "get",
  "description": "Returns price performance statistics for one or more cryptocurrencies including launch price ROI and all-time high / all-time low. Stats are returned for an `all_time` period by default. UTC `yesterday` and a number of *rolling time periods* may be requested using the `time_period` parameter. Utilize the `convert` parameter to translate values into multiple fiats or cryptocurrencies using historical rates.\n\n\n**Please note**: This documentation relates to our updated V2 endpoint, which may be incompatible with our V1 versions. Documentation for deprecated endpoints can be found [the deprecated section](/pro-api-reference/deprecated).\n\n\n  **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**\n  - ~~Basic~~\n  - ~~Hobbyist~~\n  - Startup\n  - Standard\n  - Professional\n  - Enterprise\n\n**Cache / Update frequency:** Every 60 seconds.  \n**Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up) and 1 call credit per `convert` option beyond the first.  \n**CMC equivalent pages:** The statistics module displayed on cryptocurrency pages like [Bitcoin](https://coinmarketcap.com/currencies/bitcoin/).     \n  \n***NOTE:** You may also use `/cryptocurrency/ohlcv/historical` for traditional OHLCV data at historical daily and hourly intervals. You may also use `/v1/cryptocurrency/ohlcv/latest` for OHLCV data for the current UTC day.* ",
  "operationId": "getV2CryptocurrencyPriceperformancestatsLatest",
  "contentTypes": [],
  "path": "/v2/cryptocurrency/price-performance-stats/latest",
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
      "description": "One or more comma-separated cryptocurrency CoinMarketCap IDs. Example: 1,2",
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
      "description": "Alternatively pass a comma-separated list of cryptocurrency slugs. Example: \"bitcoin,ethereum\"",
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
      "name": "symbol",
      "in": "query",
      "description": "Alternatively pass one or more comma-separated cryptocurrency symbols. Example: \"BTC,ETH\". At least one \"id\" *or* \"slug\" *or* \"symbol\" is required for this request.",
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
      "name": "time_period",
      "in": "query",
      "description": "Specify one or more comma-delimited time periods to return stats for. `all_time` is the default. Pass `all_time,yesterday,24h,7d,30d,90d,365d` to return all supported time periods. All rolling periods have a rolling close time of the current request time. For example `24h` would have a close time of now and an open time of 24 hours before now. *Please note: `yesterday` is a UTC period and currently does not currently support `high` and `low` timestamps.*",
      "required": null,
      "schema": {
        "type": "string",
        "pattern": "^(all_time|yesterday|24h|7d|30d|90d|365d)+(?:,(all_time|yesterday|24h|7d|30d|90d|365d)+)*$",
        "default": "all_time"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "convert",
      "in": "query",
      "description": "Optionally calculate quotes in up to 120 currencies at once by passing a comma-separated list of cryptocurrency or fiat currency symbols. Each additional convert option beyond the first requires an additional call credit. A list of supported fiat options can be found [here](/guides/standards-and-conventions). Each conversion is returned in its own \"quote\" object.",
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
      "description": "Optionally calculate quotes by CoinMarketCap ID instead of symbol. This option is identical to `convert` outside of ID format. Ex: convert_id=1,2781 would replace convert=BTC,USD in your query. This parameter cannot be used when `convert` is used.",
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
      "name": "skip_invalid",
      "in": "query",
      "description": "Pass `true` to relax request validation rules. When requesting records on multiple cryptocurrencies an error is returned if no match is found for 1 or more requested cryptocurrencies. If set to true, invalid lookups will be skipped allowing valid cryptocurrencies to still be returned.",
      "required": null,
      "schema": {
        "type": "boolean",
        "default": true
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
                "description": "An object map of cryptocurrency objects by ID, slug, or symbol (as used in query parameters).",
                "example": {
                  "1": {
                    "id": 1,
                    "name": "Bitcoin",
                    "symbol": "BTC",
                    "slug": "bitcoin",
                    "last_updated": "2019-08-22T01:51:32.000Z",
                    "periods": {
                      "USD": {
                        "open_timestamp": "2013-04-28T00:00:00.000Z",
                        "high_timestamp": "2017-12-17T12:19:14.000Z",
                        "low_timestamp": "2013-07-05T18:56:01.000Z",
                        "close_timestamp": "2019-08-22T01:52:18.613Z",
                        "quote": {
                          "USD": {
                            "open": 135.3000030517578,
                            "open_timestamp": "2013-04-28T00:00:00.000Z",
                            "high": 20088.99609375,
                            "high_timestamp": "2017-12-17T12:19:14.000Z",
                            "low": 65.5260009765625,
                            "low_timestamp": "2013-07-05T18:56:01.000Z",
                            "close": 65.5260009765625,
                            "close_timestamp": "2019-08-22T01:52:18.618Z",
                            "percent_change": 7223.718930042746,
                            "price_change": 9773.691932798241
                          }
                        }
                      }
                    }
                  }
                },
                "additionalProperties": {
                  "type": "object",
                  "description": "A cryptocurrency object for each requested.",
                  "properties": {
                    "id": {
                      "type": "integer",
                      "description": "The unique CoinMarketCap ID for this cryptocurrency.",
                      "example": 1
                    },
                    "name": {
                      "type": "string",
                      "description": "The name of this cryptocurrency.",
                      "example": "Bitcoin"
                    },
                    "symbol": {
                      "type": "string",
                      "description": "The ticker symbol for this cryptocurrency.",
                      "example": "BTC"
                    },
                    "slug": {
                      "type": "string",
                      "description": "The web URL friendly shorthand version of this cryptocurrency name.",
                      "example": "bitcoin"
                    },
                    "last_updated": {
                      "type": "string",
                      "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                      "description": "Timestamp (ISO 8601) of the last time this cryptocurrency's market data was updated.",
                      "example": "2019-08-22T01:51:32.000Z"
                    },
                    "periods": {
                      "type": "object",
                      "description": "An object map of time periods by period requested.",
                      "additionalProperties": {
                        "type": "object",
                        "description": "A time period data object. `all_time` is the default.",
                        "properties": {
                          "open_timestamp": {
                            "type": "string",
                            "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                            "description": "Timestamp (ISO 8601) of the start of this time period. Please note that this is a rolling period back from current time for time periods outside of `yesterday`.",
                            "example": "2013-04-28T00:00:00.000Z"
                          },
                          "high_timestamp": {
                            "type": "string",
                            "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                            "description": "Timestamp (ISO 8601) of when this cryptocurrency achieved it's highest USD price during the requested time period. *Note: The `yesterday` period currently doesn't support this field and will return `null`.*",
                            "example": "2017-12-17T12:19:14.000Z"
                          },
                          "low_timestamp": {
                            "type": "string",
                            "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                            "description": "Timestamp (ISO 8601) of when this cryptocurrency achieved it's lowest USD price during the requested time period. *Note: The `yesterday` period currently doesn't support this field and will return `null`.*",
                            "example": "2013-07-05T18:56:01.000Z"
                          },
                          "close_timestamp": {
                            "type": "string",
                            "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                            "description": "Timestamp (ISO 8601) of the end of this time period. Please note that this is a rolling period back from current time for time periods outside of `yesterday`.",
                            "example": "2019-08-22T01:52:18.613Z"
                          },
                          "quote": {
                            "type": "object",
                            "description": "An object map of time period quotes for each convert option requested. The default map included is USD.",
                            "additionalProperties": {
                              "type": "object",
                              "description": "A time period quote in the currency conversion option.",
                              "properties": {
                                "open": {
                                  "type": "number",
                                  "description": "Cryptocurrency price at the start of the requested time period historically converted into units of the convert currency.",
                                  "example": 135.3000030517578
                                },
                                "open_timestamp": {
                                  "type": "string",
                                  "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                                  "description": "Timestamp (ISO 8601) of the closest convert currency reference price used during `open` price conversion.",
                                  "example": "2013-04-28T00:00:00.000Z"
                                },
                                "high": {
                                  "type": "number",
                                  "description": "Highest USD price achieved within the requested time period historically converted into units of the convert currency.",
                                  "example": 20088.99609375
                                },
                                "high_timestamp": {
                                  "type": "string",
                                  "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                                  "description": "Timestamp (ISO 8601) of the closest convert currency reference price used during `high` price conversion. *For `yesterday` UTC close will be used.*",
                                  "example": "2017-12-17T12:19:14.000Z"
                                },
                                "low": {
                                  "type": "number",
                                  "description": "Lowest USD price achieved within the requested time period historically converted into units of the convert currency.",
                                  "example": 65.5260009765625
                                },
                                "low_timestamp": {
                                  "type": "string",
                                  "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                                  "description": "Timestamp (ISO 8601) of the closest convert currency reference price used during `low` price conversion. *For `yesterday` UTC close will be used.*",
                                  "example": "2013-07-05T18:56:01.000Z"
                                },
                                "close": {
                                  "type": "number",
                                  "description": "Cryptocurrency price at the end of the requested time period historically converted into units of the convert currency.",
                                  "example": 9908.99193585
                                },
                                "close_timestamp": {
                                  "type": "string",
                                  "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                                  "description": "Timestamp (ISO 8601) of the closest convert currency reference price used during `close` price conversion.",
                                  "example": "2019-08-22T01:52:18.618Z"
                                },
                                "percent_change": {
                                  "type": "number",
                                  "description": "The approximate percentage change (ROI) if purchased at the start of the time period. This is the time of launch or earliest known price for the `all_time` period. This value includes historical change in market rate for the specified convert currency.",
                                  "example": 7223.718930042746
                                },
                                "price_change": {
                                  "type": "number",
                                  "description": "The actual price change between the start of the time period and end. This is the time of launch or earliest known price for the `all_time` period. This value includes historical change in market rate for the specified convert currency.",
                                  "example": 9773.691932798241
                                }
                              },
                              "required": [
                                "open",
                                "open_timestamp",
                                "high",
                                "high_timestamp",
                                "low",
                                "low_timestamp",
                                "close",
                                "close_timestamp",
                                "percent_change",
                                "price_change"
                              ],
                              "__$ref": "#/components/schemas/Cryptocurrency_Price_Performance_Stats_Latest_-_Quote_object"
                            },
                            "__$ref": "#/components/schemas/Cryptocurrency_Price_Performance_Stats_Latest_-_Quote_map"
                          }
                        },
                        "required": [
                          "open_timestamp",
                          "high_timestamp",
                          "low_timestamp",
                          "close_timestamp",
                          "quote"
                        ],
                        "__$ref": "#/components/schemas/Cryptocurrency_Price_Performance_Stats_Latest_-_Period_object"
                      },
                      "__$ref": "#/components/schemas/Cryptocurrency_Price_Performance_Stats_Latest_-_Period_object_map"
                    }
                  },
                  "required": [
                    "id",
                    "name",
                    "symbol",
                    "slug",
                    "last_updated",
                    "periods"
                  ],
                  "__$ref": "#/components/schemas/Cryptocurrency_Price_Performance_Stats_Latest_-_Cryptocurrency_object"
                },
                "__$ref": "#/components/schemas/Cryptocurrency_Price_Performance_Stats_Latest_-_Cryptocurrency_Results_map"
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
            "__$ref": "#/components/schemas/Cryptocurrency_Price_Performance_Stats_Latest_-_Response_Model"
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
