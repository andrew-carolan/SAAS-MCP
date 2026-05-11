# GET /v1/cryptocurrency/ohlcv/historical

**Summary:** OHLCV Historical v1 (deprecated)

**Description:** Returns historical OHLCV (Open, High, Low, Close, Volume) data along with market cap for any cryptocurrency using time interval parameters. Currently daily and hourly OHLCV periods are supported. Volume is not currently supported for hourly OHLCV intervals before 2020-09-22.

  
**Technical Notes**
- Only the date portion of the timestamp is used for daily OHLCV so it's recommended to send an ISO date format like "2018-09-19" without time for this "time_period". 
- One OHLCV quote will be returned for every "time_period" between your "time_start" (exclusive) and "time_end" (inclusive).  
- If a "time_start" is not supplied, the "time_period" will be calculated in reverse from "time_end" using the "count" parameter which defaults to 10 results.  
- If "time_end" is not supplied, it defaults to the current time.   
- If you don't need every "time_period" between your dates you may adjust the frequency that "time_period" is sampled using the "interval" parameter. For example with "time_period" set to "daily" you may set "interval" to "2d" to get the daily OHLCV for every other day. You could set "interval" to "monthly" to get the first daily OHLCV for each month, or set it to "yearly" to get the daily OHLCV value against the same date every year.  

**Implementation Tips**
- If querying for a specific OHLCV date your "time_start" should specify a timestamp of 1 interval prior as "time_start" is an exclusive time parameter (as opposed to "time_end" which is inclusive to the search). This means that when you pass a "time_start" results will be returned for the *next* complete "time_period". For example, if you are querying for a daily OHLCV datapoint for 2018-11-30 your "time_start" should be "2018-11-29".   
- If only specifying a "count" parameter to return latest OHLCV periods, your "count" should be 1 number higher than the number of results you expect to receive. "Count" defines the number of "time_period" intervals queried, *not* the number of results to return, and this includes the currently active time period which is incomplete when working backwards from current time. For example, if you want the last daily OHLCV value available simply pass "count=2" to skip the incomplete active time period.
- This endpoint supports requesting multiple cryptocurrencies in the same call. Please note the API response will be wrapped in an additional object in this case.  
  
**Interval Options**  
  
There are 2 types of time interval formats that may be used for "time_period" and "interval" parameters. For "time_period" these return aggregate OHLCV data from the beginning to end of each interval period. Apply these time intervals to "interval" to adjust how frequently "time_period" is sampled.  
  
The first are calendar year and time constants in UTC time:  
**"hourly"** - Hour intervals in UTC.  
**"daily"** - Calendar day intervals for each UTC day.  
**"weekly"** - Calendar week intervals for each calendar week.  
**"monthly"** - Calendar month intervals for each calendar month.    
**"yearly"** - Calendar year intervals for each calendar year.  
  
The second are relative time intervals.  
**"h"**: Get the first quote available every "h" hours (3600 second intervals). Supported hour intervals are: "1h", "2h", "3h", "4h", "6h", "12h".  
**"d"**: Time periods that repeat every "d" days (86400 second intervals). Supported day intervals are: "1d", "2d", "3d", "7d", "14d", "15d", "30d", "60d", "90d", "365d".  
  
Please note that "time_period" currently supports the "daily" and "hourly" options. "interval" supports all interval options.  
  
**This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**  
- ~~Basic~~
- ~~Hobbyist~~
- Startup (1 month)
- Standard (3 months)
- Professional (12 months)
- Enterprise (Up to 6 years)

**Cache / Update frequency:** Latest Daily OHLCV record is available ~5 to ~10 minutes after each midnight UTC. The latest hourly OHLCV record is available 5 minutes after each UTC hour.  
**Plan credit use:** 1 call credit per 100 OHLCV data points returned (rounded up) and 1 call credit per `convert` option beyond the first.  
**CMC equivalent pages:** Our historical cryptocurrency data pages like [coinmarketcap.com/currencies/bitcoin/historical-data/](https://coinmarketcap.com/currencies/bitcoin/historical-data/).

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **id** (query) - *Optional*: One or more comma-separated CoinMarketCap cryptocurrency IDs. Example: "1,1027"
- **slug** (query) - *Optional*: Alternatively pass a comma-separated list of cryptocurrency slugs. Example: "bitcoin,ethereum"
- **symbol** (query) - *Optional*: Alternatively pass one or more comma-separated cryptocurrency symbols. Example: "BTC,ETH". At least one "id" *or* "slug" *or* "symbol" is required for this request.
- **time_period** (query) - *Optional*: Time period to return OHLCV data for. The default is "daily". If hourly, the open will be 01:00 and the close will be 01:59. If daily, the open will be 00:00:00 for the day and close will be 23:59:99 for the same day. See the main endpoint description for details.
- **time_start** (query) - *Optional*: Timestamp (Unix or ISO 8601) to start returning OHLCV time periods for. Only the date portion of the timestamp is used for daily OHLCV so it's recommended to send an ISO date format like "2018-09-19" without time.
- **time_end** (query) - *Optional*: Timestamp (Unix or ISO 8601) to stop returning OHLCV time periods for (inclusive). Optional, if not passed we'll default to the current time. Only the date portion of the timestamp is used for daily OHLCV so it's recommended to send an ISO date format like "2018-09-19" without time.
- **count** (query) - *Optional*: Optionally limit the number of time periods to return results for. The default is 10 items. The current query limit is 10000 items.
- **interval** (query) - *Optional*: Optionally adjust the interval that "time_period" is sampled. For example with interval=monthly&time_period=daily you will see a daily OHLCV record for January, February, March and so on. See main endpoint description for available options.
- **convert** (query) - *Optional*: By default market quotes are returned in USD. Optionally calculate market quotes in up to 3 fiat currencies or cryptocurrencies.
- **convert_id** (query) - *Optional*: Optionally calculate market quotes by CoinMarketCap ID instead of symbol. This option is identical to `convert` outside of ID format. Ex: convert_id=1,2781 would replace convert=BTC,USD in your query. This parameter cannot be used when `convert` is used.
- **skip_invalid** (query) - *Optional*: Pass `true` to relax request validation rules. When requesting records on multiple cryptocurrencies an error is returned if any invalid cryptocurrencies are requested or a cryptocurrency does not have matching records in the requested timeframe. If set to true, invalid lookups will be skipped allowing valid cryptocurrencies to still be returned.

### Raw Data

```json
{
  "slug": "ohlcv-historical-v1-deprecated",
  "summary": "OHLCV Historical v1 (deprecated)",
  "method": "get",
  "description": "Returns historical OHLCV (Open, High, Low, Close, Volume) data along with market cap for any cryptocurrency using time interval parameters. Currently daily and hourly OHLCV periods are supported. Volume is not currently supported for hourly OHLCV intervals before 2020-09-22.\n\n  \n**Technical Notes**\n- Only the date portion of the timestamp is used for daily OHLCV so it's recommended to send an ISO date format like \"2018-09-19\" without time for this \"time_period\". \n- One OHLCV quote will be returned for every \"time_period\" between your \"time_start\" (exclusive) and \"time_end\" (inclusive).  \n- If a \"time_start\" is not supplied, the \"time_period\" will be calculated in reverse from \"time_end\" using the \"count\" parameter which defaults to 10 results.  \n- If \"time_end\" is not supplied, it defaults to the current time.   \n- If you don't need every \"time_period\" between your dates you may adjust the frequency that \"time_period\" is sampled using the \"interval\" parameter. For example with \"time_period\" set to \"daily\" you may set \"interval\" to \"2d\" to get the daily OHLCV for every other day. You could set \"interval\" to \"monthly\" to get the first daily OHLCV for each month, or set it to \"yearly\" to get the daily OHLCV value against the same date every year.  \n\n**Implementation Tips**\n- If querying for a specific OHLCV date your \"time_start\" should specify a timestamp of 1 interval prior as \"time_start\" is an exclusive time parameter (as opposed to \"time_end\" which is inclusive to the search). This means that when you pass a \"time_start\" results will be returned for the *next* complete \"time_period\". For example, if you are querying for a daily OHLCV datapoint for 2018-11-30 your \"time_start\" should be \"2018-11-29\".   \n- If only specifying a \"count\" parameter to return latest OHLCV periods, your \"count\" should be 1 number higher than the number of results you expect to receive. \"Count\" defines the number of \"time_period\" intervals queried, *not* the number of results to return, and this includes the currently active time period which is incomplete when working backwards from current time. For example, if you want the last daily OHLCV value available simply pass \"count=2\" to skip the incomplete active time period.\n- This endpoint supports requesting multiple cryptocurrencies in the same call. Please note the API response will be wrapped in an additional object in this case.  \n  \n**Interval Options**  \n  \nThere are 2 types of time interval formats that may be used for \"time_period\" and \"interval\" parameters. For \"time_period\" these return aggregate OHLCV data from the beginning to end of each interval period. Apply these time intervals to \"interval\" to adjust how frequently \"time_period\" is sampled.  \n  \nThe first are calendar year and time constants in UTC time:  \n**\"hourly\"** - Hour intervals in UTC.  \n**\"daily\"** - Calendar day intervals for each UTC day.  \n**\"weekly\"** - Calendar week intervals for each calendar week.  \n**\"monthly\"** - Calendar month intervals for each calendar month.    \n**\"yearly\"** - Calendar year intervals for each calendar year.  \n  \nThe second are relative time intervals.  \n**\"h\"**: Get the first quote available every \"h\" hours (3600 second intervals). Supported hour intervals are: \"1h\", \"2h\", \"3h\", \"4h\", \"6h\", \"12h\".  \n**\"d\"**: Time periods that repeat every \"d\" days (86400 second intervals). Supported day intervals are: \"1d\", \"2d\", \"3d\", \"7d\", \"14d\", \"15d\", \"30d\", \"60d\", \"90d\", \"365d\".  \n  \nPlease note that \"time_period\" currently supports the \"daily\" and \"hourly\" options. \"interval\" supports all interval options.  \n  \n**This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**  \n- ~~Basic~~\n- ~~Hobbyist~~\n- Startup (1 month)\n- Standard (3 months)\n- Professional (12 months)\n- Enterprise (Up to 6 years)\n\n**Cache / Update frequency:** Latest Daily OHLCV record is available ~5 to ~10 minutes after each midnight UTC. The latest hourly OHLCV record is available 5 minutes after each UTC hour.  \n**Plan credit use:** 1 call credit per 100 OHLCV data points returned (rounded up) and 1 call credit per `convert` option beyond the first.  \n**CMC equivalent pages:** Our historical cryptocurrency data pages like [coinmarketcap.com/currencies/bitcoin/historical-data/](https://coinmarketcap.com/currencies/bitcoin/historical-data/).",
  "operationId": "getV1CryptocurrencyOhlcvHistorical",
  "contentTypes": [],
  "path": "/v1/cryptocurrency/ohlcv/historical",
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
      "description": "One or more comma-separated CoinMarketCap cryptocurrency IDs. Example: \"1,1027\"",
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
      "description": "Time period to return OHLCV data for. The default is \"daily\". If hourly, the open will be 01:00 and the close will be 01:59. If daily, the open will be 00:00:00 for the day and close will be 23:59:99 for the same day. See the main endpoint description for details.",
      "required": null,
      "schema": {
        "type": "string",
        "enum": [
          "daily",
          "hourly"
        ],
        "default": "daily"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "time_start",
      "in": "query",
      "description": "Timestamp (Unix or ISO 8601) to start returning OHLCV time periods for. Only the date portion of the timestamp is used for daily OHLCV so it's recommended to send an ISO date format like \"2018-09-19\" without time.",
      "required": null,
      "schema": {
        "type": "string"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "time_end",
      "in": "query",
      "description": "Timestamp (Unix or ISO 8601) to stop returning OHLCV time periods for (inclusive). Optional, if not passed we'll default to the current time. Only the date portion of the timestamp is used for daily OHLCV so it's recommended to send an ISO date format like \"2018-09-19\" without time.",
      "required": null,
      "schema": {
        "type": "string"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "count",
      "in": "query",
      "description": "Optionally limit the number of time periods to return results for. The default is 10 items. The current query limit is 10000 items.",
      "required": null,
      "schema": {
        "type": "number",
        "minimum": 1,
        "maximum": 10000,
        "default": 10
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "interval",
      "in": "query",
      "description": "Optionally adjust the interval that \"time_period\" is sampled. For example with interval=monthly&time_period=daily you will see a daily OHLCV record for January, February, March and so on. See main endpoint description for available options.",
      "required": null,
      "schema": {
        "type": "string",
        "enum": [
          "hourly",
          "daily",
          "weekly",
          "monthly",
          "yearly",
          "1h",
          "2h",
          "3h",
          "4h",
          "6h",
          "12h",
          "1d",
          "2d",
          "3d",
          "7d",
          "14d",
          "15d",
          "30d",
          "60d",
          "90d",
          "365d"
        ],
        "default": "daily"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "convert",
      "in": "query",
      "description": "By default market quotes are returned in USD. Optionally calculate market quotes in up to 3 fiat currencies or cryptocurrencies.",
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
      "name": "skip_invalid",
      "in": "query",
      "description": "Pass `true` to relax request validation rules. When requesting records on multiple cryptocurrencies an error is returned if any invalid cryptocurrencies are requested or a cryptocurrency does not have matching records in the requested timeframe. If set to true, invalid lookups will be skipped allowing valid cryptocurrencies to still be returned.",
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
                "description": "Results of your query returned as an object.",
                "example": {
                  "id": 1,
                  "name": "Bitcoin",
                  "symbol": "BTC",
                  "quotes": [
                    {
                      "time_open": "2019-01-02T00:00:00.000Z",
                      "time_close": "2019-01-02T23:59:59.999Z",
                      "time_high": "2019-01-02T03:53:00.000Z",
                      "time_low": "2019-01-02T02:43:00.000Z",
                      "quote": {
                        "USD": {
                          "open": 3849.21640853,
                          "high": 3947.9812729,
                          "low": 3817.40949569,
                          "close": 3943.40933686,
                          "volume": 5244856835.70851,
                          "market_cap": 68849856731.6738,
                          "timestamp": "2019-01-02T23:59:59.999Z"
                        }
                      }
                    },
                    {
                      "time_open": "2019-01-03T00:00:00.000Z",
                      "time_close": "2019-01-03T23:59:59.999Z",
                      "time_high": "2019-01-02T03:53:00.000Z",
                      "time_low": "2019-01-02T02:43:00.000Z",
                      "quote": {
                        "USD": {
                          "open": 3931.04863841,
                          "high": 3935.68513083,
                          "low": 3826.22287069,
                          "close": 3836.74131867,
                          "volume": 4530215218.84018,
                          "market_cap": 66994920902.7202,
                          "timestamp": "2019-01-03T23:59:59.999Z"
                        }
                      }
                    }
                  ]
                },
                "properties": {
                  "id": {
                    "type": "integer",
                    "description": "The CoinMarketCap cryptocurrency ID.",
                    "example": 1
                  },
                  "name": {
                    "type": "string",
                    "description": "The cryptocurrency name.",
                    "example": "Bitcoin"
                  },
                  "symbol": {
                    "type": "string",
                    "description": "The cryptocurrency symbol.",
                    "example": "BTC"
                  },
                  "quotes": {
                    "type": "array",
                    "description": "An array of OHLCV quotes for the supplied interval.",
                    "items": {
                      "type": "object",
                      "description": "An OHLCV quote for the supplied interval.",
                      "properties": {
                        "time_open": {
                          "type": "string",
                          "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                          "description": "Timestamp (ISO 8601) of the start of this time series interval.",
                          "example": "2018-06-02T00:00:00.000Z"
                        },
                        "time_close": {
                          "type": "string",
                          "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                          "description": "Timestamp (ISO 8601) of the end of this time series interval.",
                          "example": "2018-06-02T23:59:59.999Z"
                        },
                        "time_high": {
                          "type": "string",
                          "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                          "description": "Timestamp (ISO 8601) of the high of this time series interval.",
                          "example": "2018-06-02T22:59:59.999Z"
                        },
                        "time_low": {
                          "type": "string",
                          "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                          "description": "Timestamp (ISO 8601) of the low of this time series interval.",
                          "example": "2018-06-02T21:59:59.999Z"
                        },
                        "quote": {
                          "type": "object",
                          "description": "A map of market quotes in different currency conversions. The default map included is USD.",
                          "additionalProperties": {
                            "type": "object",
                            "description": "A market quote in each currency conversion option.",
                            "properties": {
                              "open": {
                                "type": "number",
                                "description": "Opening price for time series interval.",
                                "example": 3849.21640853
                              },
                              "high": {
                                "type": "number",
                                "description": "Highest price during this time series interval.",
                                "example": 3947.9812729
                              },
                              "low": {
                                "type": "number",
                                "description": "Lowest price during this time series interval.",
                                "example": 3817.40949569
                              },
                              "close": {
                                "type": "number",
                                "description": "Closing price for this time series interval.",
                                "example": 3943.40933686
                              },
                              "volume": {
                                "type": "number",
                                "description": "Adjusted volume for this time series interval. Volume is not currently supported for hourly OHLCV intervals before 2020-09-22.",
                                "example": 5244856835.70851
                              },
                              "market_cap": {
                                "type": "number",
                                "description": "Market cap by circulating supply for this time series interval.",
                                "example": 68849856731.6738
                              },
                              "timestamp": {
                                "type": "string",
                                "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                                "description": "Timestamp (ISO 8601) of when the conversion currency's current value was referenced for this conversion.",
                                "example": "2019-01-02T23:59:59.999Z"
                              }
                            },
                            "required": [
                              "open",
                              "high",
                              "low",
                              "close",
                              "volume",
                              "market_cap",
                              "timestamp"
                            ],
                            "__$ref": "#/components/schemas/Cryptocurrency_OHLCV_Historical_-_Quote_object"
                          },
                          "__$ref": "#/components/schemas/Cryptocurrency_OHLCV_Historical_-_Quote_map"
                        }
                      },
                      "required": [
                        "time_open",
                        "time_close",
                        "time_high",
                        "time_low",
                        "quote"
                      ],
                      "__$ref": "#/components/schemas/Cryptocurrency_OHLCV_Historical_-_Interval_Quote_object"
                    },
                    "required": [
                      "Cryptocurrency OHLCV Historical - Interval Quote object"
                    ],
                    "__$ref": "#/components/schemas/Cryptocurrency_OHLCV_Historical_-_Interval_Quotes_array"
                  }
                },
                "required": [
                  "id",
                  "name",
                  "symbol",
                  "quotes"
                ],
                "__$ref": "#/components/schemas/Cryptocurrency_OHLCV_Historical_-_Results_object"
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
            "__$ref": "#/components/schemas/Cryptocurrency_OHLCV_Historical_-_Response_Model"
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
