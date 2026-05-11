# GET /v1/cryptocurrency/trending/gainers-losers

**Summary:** Trending Gainers & Losers

**Description:** Returns a paginated list of all trending cryptocurrencies, determined and sorted by the largest price gains or losses.


You may sort against any of the following:  
**percent_change_24h**: 24 hour trading price percentage change for each currency.

**This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
  - Startup
  - Standard
  - Professional
  - Enterprise

**Cache / Update frequency:** Every 10 minutes.  
**Plan credit use:** 1 call credit per 200 cryptocurrencies returned (rounded up) and 1 call credit per `convert` option beyond the first.  
**CMC equivalent pages:** Our cryptocurrency Gainers & Losers page [coinmarketcap.com/gainers-losers/](https://coinmarketcap.com/gainers-losers/).

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **start** (query) - *Optional*: Optionally offset the start (1-based index) of the paginated list of items to return.
- **limit** (query) - *Optional*: Optionally specify the number of results to return. Use this parameter and the "start" parameter to determine your own pagination size.
- **time_period** (query) - *Optional*: Adjusts the overall window of time for the biggest gainers and losers.
- **convert** (query) - *Optional*: Optionally calculate market quotes in up to 120 currencies at once by passing a comma-separated list of cryptocurrency or fiat currency symbols. Each additional convert option beyond the first requires an additional call credit. A list of supported fiat options can be found [here](/guides/standards-and-conventions). Each conversion is returned in its own "quote" object.
- **convert_id** (query) - *Optional*: Optionally calculate market quotes by CoinMarketCap ID instead of symbol. This option is identical to `convert` outside of ID format. Ex: convert_id=1,2781 would replace convert=BTC,USD in your query. This parameter cannot be used when `convert` is used.
- **sort** (query) - *Optional*: What field to sort the list of cryptocurrencies by.
- **sort_dir** (query) - *Optional*: The direction in which to order cryptocurrencies against the specified sort.

### Raw Data

```json
{
  "slug": "trending-gainers-losers",
  "summary": "Trending Gainers & Losers",
  "method": "get",
  "description": "Returns a paginated list of all trending cryptocurrencies, determined and sorted by the largest price gains or losses.\n\n\nYou may sort against any of the following:  \n**percent_change_24h**: 24 hour trading price percentage change for each currency.\n\n**This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**\n  - Startup\n  - Standard\n  - Professional\n  - Enterprise\n\n**Cache / Update frequency:** Every 10 minutes.  \n**Plan credit use:** 1 call credit per 200 cryptocurrencies returned (rounded up) and 1 call credit per `convert` option beyond the first.  \n**CMC equivalent pages:** Our cryptocurrency Gainers & Losers page [coinmarketcap.com/gainers-losers/](https://coinmarketcap.com/gainers-losers/).",
  "operationId": "getV1CryptocurrencyTrendingGainerslosers",
  "contentTypes": [],
  "path": "/v1/cryptocurrency/trending/gainers-losers",
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
        "maximum": 1000,
        "default": 100
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "time_period",
      "in": "query",
      "description": "Adjusts the overall window of time for the biggest gainers and losers.",
      "required": null,
      "schema": {
        "type": "string",
        "enum": [
          "1h",
          "24h",
          "30d",
          "7d"
        ],
        "default": "24h"
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
      "name": "sort",
      "in": "query",
      "description": "What field to sort the list of cryptocurrencies by.",
      "required": null,
      "schema": {
        "type": "string",
        "enum": [
          "percent_change_24h"
        ],
        "default": "percent_change_24h"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "sort_dir",
      "in": "query",
      "description": "The direction in which to order cryptocurrencies against the specified sort.",
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
            "example": {
              "data": [
                {
                  "id": 1,
                  "name": "Bitcoin",
                  "symbol": "BTC",
                  "slug": "bitcoin",
                  "cmc_rank": 5,
                  "num_market_pairs": 500,
                  "circulating_supply": 16950100,
                  "total_supply": 16950100,
                  "max_supply": 21000000,
                  "last_updated": "2018-06-02T22:51:28.209Z",
                  "date_added": "2013-04-28T00:00:00.000Z",
                  "tags": [
                    "mineable"
                  ],
                  "platform": null,
                  "quote": {
                    "USD": {
                      "price": 9283.92,
                      "volume_24h": 7155680000,
                      "percent_change_1h": -0.152774,
                      "percent_change_24h": 0.518894,
                      "percent_change_7d": 0.986573,
                      "market_cap": 158055024432,
                      "last_updated": "2018-08-09T22:53:32.000Z"
                    }
                  }
                },
                {
                  "id": 1027,
                  "name": "Ethereum",
                  "symbol": "ETH",
                  "slug": "ethereum",
                  "num_market_pairs": 6360,
                  "circulating_supply": 16950100,
                  "total_supply": 16950100,
                  "max_supply": 21000000,
                  "last_updated": "2018-06-02T22:51:28.209Z",
                  "date_added": "2013-04-28T00:00:00.000Z",
                  "tags": [
                    "mineable"
                  ],
                  "platform": null,
                  "quote": {
                    "USD": {
                      "price": 1283.92,
                      "volume_24h": 7155680000,
                      "percent_change_1h": -0.152774,
                      "percent_change_24h": 0.518894,
                      "percent_change_7d": 0.986573,
                      "market_cap": 158055024432,
                      "last_updated": "2018-08-09T22:53:32.000Z"
                    }
                  }
                }
              ],
              "status": {
                "timestamp": "2018-06-02T22:51:28.209Z",
                "error_code": 0,
                "error_message": "",
                "elapsed": 10,
                "credit_count": 1
              }
            },
            "properties": {
              "data": {
                "type": "array",
                "description": "Array of cryptocurrency objects matching the list options.",
                "items": {
                  "type": "object",
                  "description": "A cryptocurrency object for every cryptocurrency that matched list options.",
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
                    "cmc_rank": {
                      "type": "integer",
                      "description": "The cryptocurrency's CoinMarketCap rank by market cap.",
                      "example": 5
                    },
                    "num_market_pairs": {
                      "type": "integer",
                      "description": "The number of active trading pairs available for this cryptocurrency across supported exchanges.",
                      "example": 500
                    },
                    "circulating_supply": {
                      "type": "number",
                      "description": "The approximate number of coins circulating for this cryptocurrency.",
                      "example": 16950100
                    },
                    "total_supply": {
                      "type": "number",
                      "description": "The approximate total amount of coins in existence right now (minus any coins that have been verifiably burned).",
                      "example": 16950100
                    },
                    "market_cap_by_total_supply": {
                      "type": "number",
                      "description": "The market cap by total supply. *This field is only returned if requested through the `aux` request parameter.*",
                      "example": 158055024432
                    },
                    "max_supply": {
                      "type": "number",
                      "description": "The expected maximum limit of coins ever to be available for this cryptocurrency.",
                      "example": 21000000
                    },
                    "last_updated": {
                      "type": "string",
                      "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                      "description": "Timestamp (ISO 8601) of the last time this cryptocurrency's market data was updated.",
                      "example": "2018-06-02T22:51:28.209Z"
                    },
                    "date_added": {
                      "type": "string",
                      "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                      "description": "Timestamp (ISO 8601) of when this cryptocurrency was added to CoinMarketCap.",
                      "example": "2013-04-28T00:00:00.000Z"
                    },
                    "tags": {
                      "type": "array",
                      "description": "Array of tags associated with this cryptocurrency. Currently only a mineable tag will be returned if the cryptocurrency is mineable. Additional tags will be returned in the future.",
                      "example": [
                        "mineable"
                      ],
                      "items": {
                        "type": "string"
                      },
                      "__$ref": "#/components/schemas/tags"
                    },
                    "platform": {
                      "type": [
                        "object",
                        "null"
                      ],
                      "description": "Metadata about the parent cryptocurrency platform this cryptocurrency belongs to if it is a token, otherwise null.",
                      "properties": {
                        "id": {
                          "type": "integer",
                          "description": "The unique CoinMarketCap ID for the parent platform cryptocurrency.",
                          "example": 1
                        },
                        "name": {
                          "type": "string",
                          "description": "The name of the parent platform cryptocurrency.",
                          "example": "Ethereum"
                        },
                        "symbol": {
                          "type": "string",
                          "description": "The ticker symbol for the parent platform cryptocurrency.",
                          "example": "ETH"
                        },
                        "slug": {
                          "type": "string",
                          "description": "The web URL friendly shorthand version of the parent platform cryptocurrency name.",
                          "example": "ethereum"
                        },
                        "token_address": {
                          "type": "string",
                          "description": "The token address on the parent platform cryptocurrency.",
                          "example": "0xe41d2489571d322189246dafa5ebde1f4699f498"
                        }
                      },
                      "required": [
                        "id",
                        "name",
                        "symbol",
                        "slug",
                        "token_address"
                      ],
                      "__$ref": "#/components/schemas/platform"
                    },
                    "quote": {
                      "type": "object",
                      "description": "A map of market quotes in different currency conversions. The default map included is USD.",
                      "example": {
                        "USD": {
                          "price": 9283.92,
                          "volume_24h": 7155680000,
                          "percent_change_1h": -0.152774,
                          "percent_change_24h": 0.518894,
                          "percent_change_7d": 0.986573,
                          "market_cap": 158055024432,
                          "last_updated": "2018-08-09T22:53:32.000Z"
                        }
                      },
                      "additionalProperties": {
                        "type": "object",
                        "description": "A market quote in the currency conversion option.",
                        "properties": {
                          "price": {
                            "type": "number",
                            "description": "Price in the specified currency for this historical.",
                            "example": 7139.82
                          },
                          "volume_24h": {
                            "type": "number",
                            "description": "Rolling 24 hour adjusted volume in the specified currency.",
                            "example": 4885880000
                          },
                          "volume_24h_reported": {
                            "type": "number",
                            "description": "Rolling 24 hour reported volume in the specified currency. *This field is only returned if requested through the `aux` request parameter.*",
                            "example": 4885880000
                          },
                          "volume_7d": {
                            "type": "number",
                            "description": "Rolling 7 day adjusted volume in the specified currency. *This field is only returned if requested through the `aux` request parameter.*",
                            "example": 4885880000
                          },
                          "volume_7d_reported": {
                            "type": "number",
                            "description": "Rolling 7 day reported volume in the specified currency. *This field is only returned if requested through the `aux` request parameter.*",
                            "example": 4885880000
                          },
                          "volume_30d": {
                            "type": "number",
                            "description": "Rolling 30 day adjusted volume in the specified currency. *This field is only returned if requested through the `aux` request parameter.*",
                            "example": 4885880000
                          },
                          "volume_30d_reported": {
                            "type": "number",
                            "description": "Rolling 30 day reported volume in the specified currency. *This field is only returned if requested through the `aux` request parameter.*",
                            "example": 4885880000
                          },
                          "market_cap": {
                            "type": "number",
                            "description": "Market cap in the specified currency.",
                            "example": 121020662982
                          },
                          "percent_change_1h": {
                            "type": "number",
                            "description": "1 hour change in the specified currency.",
                            "example": 0.03
                          },
                          "percent_change_24h": {
                            "type": "number",
                            "description": "24 hour change in the specified currency.",
                            "example": 5.75
                          },
                          "percent_change_7d": {
                            "type": "number",
                            "description": "7 day change in the specified currency.",
                            "example": -19.64
                          },
                          "last_updated": {
                            "type": "string",
                            "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                            "description": "Timestamp (ISO 8601) of when the conversion currency's current value was referenced.",
                            "example": "2018-06-02T23:59:59.999Z"
                          }
                        },
                        "required": [
                          "price",
                          "volume_24h",
                          "market_cap",
                          "percent_change_1h",
                          "percent_change_24h",
                          "percent_change_7d",
                          "last_updated"
                        ],
                        "__$ref": "#/components/schemas/Cryptocurrency_-_Quote_object"
                      },
                      "__$ref": "#/components/schemas/Cryptocurrency_-_Quote_map"
                    }
                  },
                  "required": [
                    "id",
                    "name",
                    "symbol",
                    "slug",
                    "last_updated",
                    "quote"
                  ],
                  "__$ref": "#/components/schemas/Cryptocurrency_-_Cryptocurrency_object"
                },
                "required": [
                  "Cryptocurrency Trending Gainers & Losers - Cryptocurrency object"
                ],
                "__$ref": "#/components/schemas/Cryptocurrency_Trending_Gainers_Losers_-_Results_array"
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
            "__$ref": "#/components/schemas/Cryptocurrency_Trending_Gainers_Losers_-_Response_Model"
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
