# GET /v1/exchange/listings/latest

**Summary:** Exchange Listings Latest

**Description:** Returns a paginated list of all cryptocurrency exchanges including the latest aggregate market data for each exchange. Use the "convert" option to return market values in multiple fiat and cryptocurrency conversions in the same call.

**This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
  - ~~Basic~~
  - ~~Hobbyist~~
  - ~~Startup~~
  - Standard
  - Professional
  - Enterprise

**Cache / Update frequency:** Every 1 minute.
**Plan credit use:** 1 call credit per 100 exchanges returned (rounded up) and 1 call credit per `convert` option beyond the first.
**CMC equivalent pages:** Our latest exchange listing and ranking pages like [coinmarketcap.com/rankings/exchanges/](https://coinmarketcap.com/rankings/exchanges/).

***NOTE:** Use this endpoint if you need a sorted and paginated list of exchanges. If you want to query for market data on a few specific exchanges use /v1/exchange/quotes/latest which is optimized for that purpose. The response data between these endpoints is otherwise the same.*

*“exchange_score" will be deprecated on 4 November 2024.*

*After this date, the "exchange_score" field return null from these endpoints. We encourage users to review and update their implementations accordingly to avoid any disruptions.*

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **start** (query) - *Optional*: Optionally offset the start (1-based index) of the paginated list of items to return.
- **limit** (query) - *Optional*: Optionally specify the number of results to return. Use this parameter and the "start" parameter to determine your own pagination size.
- **sort** (query) - *Optional*: What field to sort the list of exchanges by.
- **sort_dir** (query) - *Optional*: The direction in which to order exchanges against the specified sort.
- **market_type** (query) - *Optional*: The type of exchange markets to include in rankings. This field is deprecated. Please use "all" for accurate sorting.
- **category** (query) - *Optional*: The category for this exchange.
- **aux** (query) - *Optional*: Optionally specify a comma-separated list of supplemental data fields to return. Pass `num_market_pairs,traffic_score,rank,exchange_score,effective_liquidity_24h,date_launched,fiats` to include all auxiliary fields.
- **convert** (query) - *Optional*: Optionally calculate market quotes in up to 120 currencies at once by passing a comma-separated list of cryptocurrency or fiat currency symbols. Each additional convert option beyond the first requires an additional call credit. A list of supported fiat options can be found [here](/guides/standards-and-conventions). Each conversion is returned in its own "quote" object.
- **convert_id** (query) - *Optional*: Optionally calculate market quotes by CoinMarketCap ID instead of symbol. This option is identical to `convert` outside of ID format. Ex: convert_id=1,2781 would replace convert=BTC,USD in your query. This parameter cannot be used when `convert` is used.

### Raw Data

```json
{
  "slug": "exchange-listings-latest",
  "summary": "Exchange Listings Latest",
  "method": "get",
  "description": "Returns a paginated list of all cryptocurrency exchanges including the latest aggregate market data for each exchange. Use the \"convert\" option to return market values in multiple fiat and cryptocurrency conversions in the same call.\n\n**This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**\n  - ~~Basic~~\n  - ~~Hobbyist~~\n  - ~~Startup~~\n  - Standard\n  - Professional\n  - Enterprise\n\n**Cache / Update frequency:** Every 1 minute.\n**Plan credit use:** 1 call credit per 100 exchanges returned (rounded up) and 1 call credit per `convert` option beyond the first.\n**CMC equivalent pages:** Our latest exchange listing and ranking pages like [coinmarketcap.com/rankings/exchanges/](https://coinmarketcap.com/rankings/exchanges/).\n\n***NOTE:** Use this endpoint if you need a sorted and paginated list of exchanges. If you want to query for market data on a few specific exchanges use /v1/exchange/quotes/latest which is optimized for that purpose. The response data between these endpoints is otherwise the same.*\n\n*\u201cexchange_score\" will be deprecated on 4 November 2024.*\n\n*After this date, the \"exchange_score\" field return null from these endpoints. We encourage users to review and update their implementations accordingly to avoid any disruptions.*",
  "operationId": "getV1ExchangeListingsLatest",
  "contentTypes": [],
  "path": "/v1/exchange/listings/latest",
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
      "name": "sort",
      "in": "query",
      "description": "What field to sort the list of exchanges by.",
      "required": null,
      "schema": {
        "type": "string",
        "enum": [
          "name",
          "volume_24h",
          "volume_24h_adjusted",
          "exchange_score"
        ],
        "default": "volume_24h"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "sort_dir",
      "in": "query",
      "description": "The direction in which to order exchanges against the specified sort.",
      "required": null,
      "schema": {
        "type": "string",
        "enum": [
          "asc",
          "desc"
        ]
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "market_type",
      "in": "query",
      "description": "The type of exchange markets to include in rankings. This field is deprecated. Please use \"all\" for accurate sorting.",
      "required": null,
      "schema": {
        "type": "string",
        "enum": [
          "fees",
          "no_fees",
          "all"
        ],
        "default": "all"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "category",
      "in": "query",
      "description": "The category for this exchange.",
      "required": false,
      "schema": {
        "type": "string",
        "enum": [
          "all",
          "spot",
          "derivatives",
          "dex",
          "lending"
        ],
        "default": "all"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "aux",
      "in": "query",
      "description": "Optionally specify a comma-separated list of supplemental data fields to return. Pass `num_market_pairs,traffic_score,rank,exchange_score,effective_liquidity_24h,date_launched,fiats` to include all auxiliary fields.",
      "required": null,
      "schema": {
        "type": "string",
        "pattern": "^(num_market_pairs|traffic_score|rank|exchange_score|effective_liquidity_24h|date_launched|fiats)+(?:,(num_market_pairs|traffic_score|rank|exchange_score|effective_liquidity_24h|date_launched|fiats)+)*$",
        "default": "num_market_pairs,traffic_score,rank,exchange_score,effective_liquidity_24h"
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
                "type": "array",
                "description": "Array of exchange objects matching the list options.",
                "example": [
                  {
                    "id": 270,
                    "name": "Binance",
                    "slug": "binance",
                    "num_market_pairs": 1214,
                    "fiats": [
                      "AED",
                      "USD"
                    ],
                    "traffic_score": 1000,
                    "rank": 1,
                    "exchange_score": 9.8,
                    "liquidity_score": 9.8028,
                    "last_updated": "2018-11-08T22:18:00.000Z",
                    "quote": {
                      "USD": {
                        "volume_24h": 769291636.239632,
                        "volume_24h_adjusted": 769291636.239632,
                        "volume_7d": 3666423776,
                        "volume_30d": 21338299776,
                        "percent_change_volume_24h": -11.6153,
                        "percent_change_volume_7d": 67.2055,
                        "percent_change_volume_30d": 0.00169339,
                        "effective_liquidity_24h": 629.9774,
                        "derivative_volume_usd": 62828618628.85901,
                        "spot_volume_usd": 39682580614.8572,
                        "last_updated": "2018-11-08T22:18:00.000Z"
                      }
                    }
                  },
                  {
                    "id": 294,
                    "name": "OKEx",
                    "slug": "okex",
                    "num_market_pairs": 385,
                    "fiats": [
                      "AED",
                      "USD"
                    ],
                    "traffic_score": 845.1565,
                    "rank": 1,
                    "exchange_score": 8.5,
                    "liquidity_score": 9.8028,
                    "last_updated": "2018-11-08T22:18:00.000Z",
                    "quote": {
                      "USD": {
                        "volume_24h": 677439315.721563,
                        "volume_24h_adjusted": 677439315.721563,
                        "volume_7d": 3506137120,
                        "volume_30d": 14418225072,
                        "percent_change_volume_24h": -13.9256,
                        "percent_change_volume_7d": 60.0461,
                        "percent_change_volume_30d": 67.2225,
                        "effective_liquidity_24h": 629.9774,
                        "derivative_volume_usd": 62828618628.85901,
                        "spot_volume_usd": 39682580614.8572,
                        "last_updated": "2018-11-08T22:18:00.000Z"
                      }
                    }
                  }
                ],
                "items": {
                  "type": "object",
                  "description": "An exchange object for every exchange that matched list options.",
                  "properties": {
                    "id": {
                      "type": "integer",
                      "description": "The unique CoinMarketCap ID for this exchange.",
                      "example": 1
                    },
                    "name": {
                      "type": "string",
                      "description": "The name of this exchange.",
                      "example": "Binance"
                    },
                    "slug": {
                      "type": "string",
                      "description": "The web URL friendly shorthand version of this exchange name.",
                      "example": "Binance"
                    },
                    "num_market_pairs": {
                      "type": "integer",
                      "description": "The number of trading pairs actively tracked on this exchange.",
                      "example": 500
                    },
                    "date_launched": {
                      "type": "string",
                      "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                      "description": "Timestamp (ISO 8601) of the date this exchange launched. *This field is only returned if requested through the `aux` request parameter.*",
                      "example": "2018-06-02T00:00:00.000Z"
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
                      "description": "Timestamp (ISO 8601) of the last time this record was upated.",
                      "example": "2018-06-02T00:00:00.000Z"
                    },
                    "quote": {
                      "type": "object",
                      "description": "A map of market quotes in different currency conversions. The default map included is USD.",
                      "example": {
                        "USD": {
                          "volume_24h": 1418940000,
                          "last_updated": "2018-11-08T22:18:00.000Z",
                          "volume_24h_adjusted": 1418940000,
                          "volume_7d": 3666423776,
                          "volume_30d": 21338299776,
                          "percent_change_volume_24h": -11.62,
                          "percent_change_volume_7d": 67.21,
                          "percent_change_volume_30d": 0.0017,
                          "effective_liquidity_24h": 629.98
                        }
                      },
                      "additionalProperties": {
                        "type": "object",
                        "description": "A market quote in the currency conversion option.",
                        "properties": {
                          "last_updated": {
                            "type": "string",
                            "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                            "description": "Timestamp (ISO 8601) of when the conversion currency's current value was referenced for this conversion.",
                            "example": "2018-06-02T23:59:59.999Z"
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
                            "description": "24 hour volume change percentage in the specified currency.",
                            "example": 0.03
                          },
                          "percent_change_volume_7d": {
                            "type": "number",
                            "description": "7 day volume change percentage in the specified currency.",
                            "example": 5.75
                          },
                          "percent_change_volume_30d": {
                            "type": "number",
                            "description": "30 day volume change percentage in the specified currency.",
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
                          "open_interest": {
                            "type": "number",
                            "description": "Reported 24 hour derivative open interest in the specified currency.",
                            "example": 768478308.529847
                          },
                          "spot_volume_usd": {
                            "type": "number",
                            "description": "Reported all time spot volume in the specified currency.",
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
                        "__$ref": "#/components/schemas/Exchange_Listings_Latest_-_Quote_object"
                      },
                      "__$ref": "#/components/schemas/Exchange_Listings_Latest_-_Quote_map"
                    }
                  },
                  "required": [
                    "id",
                    "name",
                    "slug",
                    "last_updated",
                    "quote"
                  ],
                  "__$ref": "#/components/schemas/Exchange_Listings_Latest_-_Exchange_object"
                },
                "required": [
                  "Exchange Listings Latest - Exchange object"
                ],
                "__$ref": "#/components/schemas/Exchange_Listings_Latest_-_Results_array"
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
            "__$ref": "#/components/schemas/Exchange_Listings_Latest_-_Response_Model"
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
