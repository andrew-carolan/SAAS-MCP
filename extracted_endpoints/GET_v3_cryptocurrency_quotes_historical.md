# GET /v3/cryptocurrency/quotes/historical

**Summary:** Cryptocurrency Quotes Historical

**Description:** Returns an interval of historic market quotes for any cryptocurrency based on time and interval parameters.

**Please note**: This documentation relates to our updated V3 endpoint, which may be incompatible with our V1 versions. Documentation for deprecated endpoints can be found [the deprecated section](/pro-api-reference/deprecated).


**Technical Notes**  
- A historic quote for every "interval" period between your "time_start" and "time_end" will be returned.  
- If a "time_start" is not supplied, the "interval" will be applied in reverse from "time_end".  
- If "time_end" is not supplied, it defaults to the current time.  
- At each "interval" period, the historic quote that is closest in time to the requested time will be returned.  
- If no historic quotes are available in a given "interval" period up until the next interval period, it will be skipped.  

**Implementation Tips**
- Want to get the last quote of each UTC day? Don't use "interval=daily" as that returns the first quote. Instead use "interval=24h" to repeat a specific timestamp search every 24 hours and pass ex. "time_start=2019-01-04T23:59:00.000Z" to query for the last record of each UTC day.
- This endpoint supports requesting multiple cryptocurrencies in the same call. Please note the API response will be wrapped in an additional object in this case.  
  
**Interval Options**  
There are 2 types of time interval formats that may be used for "interval".

The first are calendar year and time constants in UTC time:  
**"hourly"** - Get the first quote available at the beginning of each calendar hour.  
**"daily"** - Get the first quote available at the beginning of each calendar day.  
**"weekly"** - Get the first quote available at the beginning of each calendar week.  
**"monthly"** - Get the first quote available at the beginning of each calendar month.  
**"yearly"** - Get the first quote available at the beginning of each calendar year.  

The second are relative time intervals.  
**"m"**: Get the first quote available every "m" minutes (60 second intervals). Supported minutes are: "5m", "10m", "15m", "30m", "45m".  
**"h"**: Get the first quote available every "h" hours (3600 second intervals). Supported hour intervals are: "1h", "2h", "3h", "4h", "6h", "12h".  
**"d"**: Get the first quote available every "d" days (86400 second intervals). Supported day intervals are: "1d", "2d", "3d", "7d", "14d", "15d", "30d", "60d", "90d", "365d".  

**This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
- ~~Basic~~
- Hobbyist (1 month)
- Startup (1 month)
- Standard (3 month)
- Professional (12 months)
- Enterprise (Up to 6 years)

**Cache / Update frequency:** Every 5 minutes.    
**Plan credit use:** 1 call credit per 100 historical data points returned (rounded up) and 1 call credit per `convert` option beyond the first.  
**CMC equivalent pages:** Our historical cryptocurrency charts like [coinmarketcap.com/currencies/bitcoin/#charts](https://coinmarketcap.com/currencies/bitcoin/#charts).  

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **id** (query) - *Optional*: One or more comma-separated CoinMarketCap cryptocurrency IDs. Example: "1,2"
- **symbol** (query) - *Optional*: Alternatively pass one or more comma-separated cryptocurrency symbols. Example: "BTC,ETH". At least one "id" *or* "symbol" is required for this request.
- **time_start** (query) - *Optional*: Timestamp (Unix or ISO 8601) to start returning quotes for. Optional, if not passed, we'll return quotes calculated in reverse from "time_end".
- **time_end** (query) - *Optional*: Timestamp (Unix or ISO 8601) to stop returning quotes for (inclusive). Optional, if not passed, we'll default to the current time. If no "time_start" is passed, we return quotes in reverse order starting from this time.
- **count** (query) - *Optional*: The number of interval periods to return results for. Optional, required if both "time_start" and "time_end" aren't supplied. The default is 10 items. The current query limit is 10000.
- **interval** (query) - *Optional*: Interval of time to return data points for. See details in endpoint description.
- **convert** (query) - *Optional*: By default market quotes are returned in USD. Optionally calculate market quotes in up to 3 other fiat currencies or cryptocurrencies.
- **convert_id** (query) - *Optional*: Optionally calculate market quotes by CoinMarketCap ID instead of symbol. This option is identical to `convert` outside of ID format. Ex: convert_id=1,2781 would replace convert=BTC,USD in your query. This parameter cannot be used when `convert` is used.
- **aux** (query) - *Optional*: Optionally specify a comma-separated list of supplemental data fields to return. Pass `price,volume,market_cap,circulating_supply,total_supply,quote_timestamp,is_active,is_fiat,search_interval` to include all auxiliary fields.
- **skip_invalid** (query) - *Optional*: Pass `true` to relax request validation rules. When requesting records on multiple cryptocurrencies an error is returned if no match is found for 1 or more requested cryptocurrencies. If set to true, invalid lookups will be skipped allowing valid cryptocurrencies to still be returned.

### Raw Data

```json
{
  "slug": "cryptocurrency-quotes-historical",
  "summary": "Cryptocurrency Quotes Historical",
  "method": "get",
  "description": "Returns an interval of historic market quotes for any cryptocurrency based on time and interval parameters.\n\n**Please note**: This documentation relates to our updated V3 endpoint, which may be incompatible with our V1 versions. Documentation for deprecated endpoints can be found [the deprecated section](/pro-api-reference/deprecated).\n\n\n**Technical Notes**  \n- A historic quote for every \"interval\" period between your \"time_start\" and \"time_end\" will be returned.  \n- If a \"time_start\" is not supplied, the \"interval\" will be applied in reverse from \"time_end\".  \n- If \"time_end\" is not supplied, it defaults to the current time.  \n- At each \"interval\" period, the historic quote that is closest in time to the requested time will be returned.  \n- If no historic quotes are available in a given \"interval\" period up until the next interval period, it will be skipped.  \n\n**Implementation Tips**\n- Want to get the last quote of each UTC day? Don't use \"interval=daily\" as that returns the first quote. Instead use \"interval=24h\" to repeat a specific timestamp search every 24 hours and pass ex. \"time_start=2019-01-04T23:59:00.000Z\" to query for the last record of each UTC day.\n- This endpoint supports requesting multiple cryptocurrencies in the same call. Please note the API response will be wrapped in an additional object in this case.  \n  \n**Interval Options**  \nThere are 2 types of time interval formats that may be used for \"interval\".\n\nThe first are calendar year and time constants in UTC time:  \n**\"hourly\"** - Get the first quote available at the beginning of each calendar hour.  \n**\"daily\"** - Get the first quote available at the beginning of each calendar day.  \n**\"weekly\"** - Get the first quote available at the beginning of each calendar week.  \n**\"monthly\"** - Get the first quote available at the beginning of each calendar month.  \n**\"yearly\"** - Get the first quote available at the beginning of each calendar year.  \n\nThe second are relative time intervals.  \n**\"m\"**: Get the first quote available every \"m\" minutes (60 second intervals). Supported minutes are: \"5m\", \"10m\", \"15m\", \"30m\", \"45m\".  \n**\"h\"**: Get the first quote available every \"h\" hours (3600 second intervals). Supported hour intervals are: \"1h\", \"2h\", \"3h\", \"4h\", \"6h\", \"12h\".  \n**\"d\"**: Get the first quote available every \"d\" days (86400 second intervals). Supported day intervals are: \"1d\", \"2d\", \"3d\", \"7d\", \"14d\", \"15d\", \"30d\", \"60d\", \"90d\", \"365d\".  \n\n**This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**\n- ~~Basic~~\n- Hobbyist (1 month)\n- Startup (1 month)\n- Standard (3 month)\n- Professional (12 months)\n- Enterprise (Up to 6 years)\n\n**Cache / Update frequency:** Every 5 minutes.    \n**Plan credit use:** 1 call credit per 100 historical data points returned (rounded up) and 1 call credit per `convert` option beyond the first.  \n**CMC equivalent pages:** Our historical cryptocurrency charts like [coinmarketcap.com/currencies/bitcoin/#charts](https://coinmarketcap.com/currencies/bitcoin/#charts).  ",
  "operationId": "getV3CryptocurrencyQuotesHistorical",
  "contentTypes": [],
  "path": "/v3/cryptocurrency/quotes/historical",
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
      "description": "One or more comma-separated CoinMarketCap cryptocurrency IDs. Example: \"1,2\"",
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
      "name": "symbol",
      "in": "query",
      "description": "Alternatively pass one or more comma-separated cryptocurrency symbols. Example: \"BTC,ETH\". At least one \"id\" *or* \"symbol\" is required for this request.",
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
      "name": "time_start",
      "in": "query",
      "description": "Timestamp (Unix or ISO 8601) to start returning quotes for. Optional, if not passed, we'll return quotes calculated in reverse from \"time_end\".",
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
      "description": "Timestamp (Unix or ISO 8601) to stop returning quotes for (inclusive). Optional, if not passed, we'll default to the current time. If no \"time_start\" is passed, we return quotes in reverse order starting from this time.",
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
      "description": "The number of interval periods to return results for. Optional, required if both \"time_start\" and \"time_end\" aren't supplied. The default is 10 items. The current query limit is 10000.",
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
      "description": "Interval of time to return data points for. See details in endpoint description.",
      "required": null,
      "schema": {
        "type": "string",
        "enum": [
          "yearly",
          "monthly",
          "weekly",
          "daily",
          "hourly",
          "5m",
          "10m",
          "15m",
          "30m",
          "45m",
          "1h",
          "2h",
          "3h",
          "4h",
          "6h",
          "12h",
          "24h",
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
        "default": "5m"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "convert",
      "in": "query",
      "description": "By default market quotes are returned in USD. Optionally calculate market quotes in up to 3 other fiat currencies or cryptocurrencies.",
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
        "pattern": "(^\\d+(?:,\\d+)*$|(\\d,)*PLATFORM_ID+(?:,\\d+)*$)"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "aux",
      "in": "query",
      "description": "Optionally specify a comma-separated list of supplemental data fields to return. Pass `price,volume,market_cap,circulating_supply,total_supply,quote_timestamp,is_active,is_fiat,search_interval` to include all auxiliary fields.",
      "required": null,
      "schema": {
        "type": "string",
        "pattern": "^(price|volume|market_cap|circulating_supply|total_supply|quote_timestamp|is_active|is_fiat|search_interval)+(?:,(price|volume|market_cap|circulating_supply|total_supply|quote_timestamp|is_active|is_fiat|search_interval)+)*$",
        "default": "price,volume,market_cap,circulating_supply,total_supply,quote_timestamp,is_active,is_fiat"
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
                "description": "Results of your query returned as an object map.",
                "example": {
                  "1": {
                    "id": 1,
                    "name": "Bitcoin",
                    "symbol": "BTC",
                    "is_active": 1,
                    "is_fiat": 0,
                    "quotes": [
                      {
                        "timestamp": "2018-06-22T00:00:00.000Z",
                        "quote": {
                          "USD": {
                            "price": 6242.48,
                            "volume_24h": 4894120000,
                            "market_cap": 107057808682,
                            "last_updated": "2018-06-22T00:04:16.000Z",
                            "volume_24hr": 4894120000,
                            "timestamp": "2018-06-22T00:04:16.000Z"
                          }
                        }
                      }
                    ]
                  }
                },
                "additionalProperties": {
                  "type": "object",
                  "description": "A results object for each cryptocurrency requested. The map key being the id/symbol used in the request.",
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
                    "is_active": {
                      "type": "integer",
                      "description": "1 if this cryptocurrency has at least 1 active market currently being tracked by the platform, otherwise 0. A value of 1 is analogous with `listing_status=active`.",
                      "example": 1,
                      "minimum": 0,
                      "maximum": 1
                    },
                    "is_fiat": {
                      "type": "integer",
                      "description": "1 if this is a fiat",
                      "example": 1,
                      "minimum": 0,
                      "maximum": 1
                    },
                    "quotes": {
                      "type": "array",
                      "description": "An array of quotes for each interval for this cryptocurrency.",
                      "items": {
                        "type": "object",
                        "description": "An object containing details for the current interval quote.",
                        "properties": {
                          "timestamp": {
                            "type": "string",
                            "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                            "description": "Timestamp of when this historical quote was recorded.",
                            "example": "2018-06-02T23:59:59.999Z"
                          },
                          "search_interval": {
                            "type": "string",
                            "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                            "description": "The interval timestamp for the search period that this historical quote was located against. *This field is only returned if requested through the `aux` request parameter.*",
                            "example": "2018-06-02T00:00:00.000Z"
                          },
                          "quote": {
                            "type": "object",
                            "description": "A map of market details for this quote in different currency conversions. The default map included is USD.",
                            "additionalProperties": {
                              "type": "object",
                              "description": "The market details for the current interval and currency conversion option. The map key being the curency symbol.",
                              "properties": {
                                "price": {
                                  "type": "number",
                                  "description": "Price at this interval quote.",
                                  "example": 1235000
                                },
                                "volume_24hr": {
                                  "type": "number",
                                  "description": "Aggregate 24 hour adjusted volume for all market pairs tracked for this cryptocurrency at the current historical interval.",
                                  "example": 1235000
                                },
                                "market_cap": {
                                  "type": "number",
                                  "description": "Number of market pairs available at the current historical interval.",
                                  "example": 123456789
                                },
                                "timestamp": {
                                  "type": "string",
                                  "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                                  "description": "Timestamp (ISO 8601) of when the conversion currency's current value was referenced for this conversion.",
                                  "example": "2018-06-02T22:51:28.209Z"
                                }
                              },
                              "required": [
                                "price",
                                "volume_24hr",
                                "market_cap",
                                "timestamp"
                              ],
                              "__$ref": "#/components/schemas/Cryptocurrency_Quotes_Historical_-_Currency_Quote_object"
                            },
                            "__$ref": "#/components/schemas/Cryptocurrency_Quotes_Historical_-_Quote_currency_map"
                          }
                        },
                        "required": [
                          "timestamp",
                          "quote"
                        ],
                        "__$ref": "#/components/schemas/Cryptocurrency_Quotes_Historical_-_Interval_Quote_object"
                      },
                      "required": [
                        "Cryptocurrency Quotes Historical - Interval Quote object"
                      ],
                      "__$ref": "#/components/schemas/Cryptocurrency_Quotes_Historical_-_Interval_Quotes_array"
                    }
                  },
                  "required": [
                    "id",
                    "name",
                    "symbol",
                    "quotes"
                  ],
                  "__$ref": "#/components/schemas/Cryptocurrency_Quotes_Historical_-_Result_object"
                },
                "__$ref": "#/components/schemas/Cryptocurrency_Quotes_Historical_-_Results_map"
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
            "__$ref": "#/components/schemas/Cryptocurrency_Quotes_Historical_-_Response_Model"
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
