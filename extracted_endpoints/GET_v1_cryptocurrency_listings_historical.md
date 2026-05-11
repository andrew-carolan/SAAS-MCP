# GET /v1/cryptocurrency/listings/historical

**Summary:** Listings Historical

**Description:** Returns a ranked and sorted list of all cryptocurrencies for a historical UTC date.  


**Technical Notes**
- This endpoint is identical in format to our `/cryptocurrency/listings/latest` endpoint but is used to retrieve historical daily ranking snapshots from the end of each UTC day.  
- Daily snapshots reflect market data at the end of each UTC day and may be requested as far back as 2013-04-28 (as supported by your plan's historical limits).  
- The required "date" parameter can be passed as a Unix timestamp or ISO 8601 date but only the date portion of the timestamp will be referenced. It is recommended to send an ISO date format like "2019-10-10" without time.
- This endpoint is for retrieving paginated and sorted lists of all currencies. If you require historical market data on specific cryptocurrencies you should use `/cryptocurrency/quotes/historical`.
   


Cryptocurrencies are listed by cmc_rank by default. You may optionally sort against any of the following:  
**cmc_rank**: CoinMarketCap's market cap rank as outlined in [our methodology](https://coinmarketcap.com/methodology/).  
**name**: The cryptocurrency name.  
**symbol**: The cryptocurrency symbol.  
**market_cap**: market cap (latest trade price x circulating supply).  
**price**: latest average trade price across markets.  
**circulating_supply**: approximate number of coins currently in circulation.  
**total_supply**: approximate total amount of coins in existence right now (minus any coins that have been verifiably burned).  
**max_supply**: our best approximation of the maximum amount of coins that will ever exist in the lifetime of the currency.  
**num_market_pairs**: number of market pairs across all exchanges trading each currency.  
**volume_24h**: 24 hour trading volume for each currency.  
**percent_change_1h**: 1 hour trading price percentage change for each currency.  
**percent_change_24h**: 24 hour trading price percentage change for each currency.  
**percent_change_7d**: 7 day trading price percentage change for each currency.  
 
  **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
  - ~~Basic~~
  - Hobbyist (1 month)
  - Startup (1 month)
  - Standard (3 month)
  - Professional (12 months)
  - Enterprise (Up to 6 years)

**Cache / Update frequency:** The last completed UTC day is available 30 minutes after midnight on the next UTC day.  
**Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up) and 1 call credit per `convert` option beyond the first.  
**CMC equivalent pages:** Our historical daily crypto ranking snapshot pages like this one on [February 02, 2014](https://coinmarketcap.com/historical/20140202/).

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **date** (query) - *Required*: date (Unix or ISO 8601) to reference day of snapshot.
- **start** (query) - *Optional*: Optionally offset the start (1-based index) of the paginated list of items to return.
- **limit** (query) - *Optional*: Optionally specify the number of results to return. Use this parameter and the "start" parameter to determine your own pagination size.
- **convert** (query) - *Optional*: Optionally calculate market quotes in up to 120 currencies at once by passing a comma-separated list of cryptocurrency or fiat currency symbols. Each additional convert option beyond the first requires an additional call credit. A list of supported fiat options can be found [here](/guides/standards-and-conventions). Each conversion is returned in its own "quote" object.
- **convert_id** (query) - *Optional*: Optionally calculate market quotes by CoinMarketCap ID instead of symbol. This option is identical to `convert` outside of ID format. Ex: convert_id=1,2781 would replace convert=BTC,USD in your query. This parameter cannot be used when `convert` is used.
- **sort** (query) - *Optional*: What field to sort the list of cryptocurrencies by.
- **sort_dir** (query) - *Optional*: The direction in which to order cryptocurrencies against the specified sort.
- **cryptocurrency_type** (query) - *Optional*: The type of cryptocurrency to include.
- **aux** (query) - *Optional*: Optionally specify a comma-separated list of supplemental data fields to return. Pass `platform,tags,date_added,circulating_supply,total_supply,max_supply,cmc_rank,num_market_pairs` to include all auxiliary fields.

### Raw Data

```json
{
  "slug": "listings-historical",
  "summary": "Listings Historical",
  "method": "get",
  "description": "Returns a ranked and sorted list of all cryptocurrencies for a historical UTC date.  \n\n\n**Technical Notes**\n- This endpoint is identical in format to our `/cryptocurrency/listings/latest` endpoint but is used to retrieve historical daily ranking snapshots from the end of each UTC day.  \n- Daily snapshots reflect market data at the end of each UTC day and may be requested as far back as 2013-04-28 (as supported by your plan's historical limits).  \n- The required \"date\" parameter can be passed as a Unix timestamp or ISO 8601 date but only the date portion of the timestamp will be referenced. It is recommended to send an ISO date format like \"2019-10-10\" without time.\n- This endpoint is for retrieving paginated and sorted lists of all currencies. If you require historical market data on specific cryptocurrencies you should use `/cryptocurrency/quotes/historical`.\n   \n\n\nCryptocurrencies are listed by cmc_rank by default. You may optionally sort against any of the following:  \n**cmc_rank**: CoinMarketCap's market cap rank as outlined in [our methodology](https://coinmarketcap.com/methodology/).  \n**name**: The cryptocurrency name.  \n**symbol**: The cryptocurrency symbol.  \n**market_cap**: market cap (latest trade price x circulating supply).  \n**price**: latest average trade price across markets.  \n**circulating_supply**: approximate number of coins currently in circulation.  \n**total_supply**: approximate total amount of coins in existence right now (minus any coins that have been verifiably burned).  \n**max_supply**: our best approximation of the maximum amount of coins that will ever exist in the lifetime of the currency.  \n**num_market_pairs**: number of market pairs across all exchanges trading each currency.  \n**volume_24h**: 24 hour trading volume for each currency.  \n**percent_change_1h**: 1 hour trading price percentage change for each currency.  \n**percent_change_24h**: 24 hour trading price percentage change for each currency.  \n**percent_change_7d**: 7 day trading price percentage change for each currency.  \n \n  **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**\n  - ~~Basic~~\n  - Hobbyist (1 month)\n  - Startup (1 month)\n  - Standard (3 month)\n  - Professional (12 months)\n  - Enterprise (Up to 6 years)\n\n**Cache / Update frequency:** The last completed UTC day is available 30 minutes after midnight on the next UTC day.  \n**Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up) and 1 call credit per `convert` option beyond the first.  \n**CMC equivalent pages:** Our historical daily crypto ranking snapshot pages like this one on [February 02, 2014](https://coinmarketcap.com/historical/20140202/).",
  "operationId": "getV1CryptocurrencyListingsHistorical",
  "contentTypes": [],
  "path": "/v1/cryptocurrency/listings/historical",
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
      "name": "date",
      "in": "query",
      "description": "date (Unix or ISO 8601) to reference day of snapshot.",
      "required": true,
      "schema": {
        "type": "string"
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
          "cmc_rank",
          "name",
          "symbol",
          "market_cap",
          "price",
          "circulating_supply",
          "total_supply",
          "max_supply",
          "num_market_pairs",
          "volume_24h",
          "percent_change_1h",
          "percent_change_24h",
          "percent_change_7d"
        ],
        "default": "cmc_rank"
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
    },
    {
      "name": "cryptocurrency_type",
      "in": "query",
      "description": "The type of cryptocurrency to include.",
      "required": null,
      "schema": {
        "type": "string",
        "enum": [
          "all",
          "coins",
          "tokens"
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
      "description": "Optionally specify a comma-separated list of supplemental data fields to return. Pass `platform,tags,date_added,circulating_supply,total_supply,max_supply,cmc_rank,num_market_pairs` to include all auxiliary fields.",
      "required": null,
      "schema": {
        "type": "string",
        "pattern": "^(platform|tags|date_added|circulating_supply|total_supply|max_supply|cmc_rank|num_market_pairs)+(?:,(platform|tags|date_added|circulating_supply|total_supply|max_supply|cmc_rank|num_market_pairs)+)*$",
        "default": "platform,tags,date_added,circulating_supply,total_supply,max_supply,cmc_rank,num_market_pairs"
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
                  "cmc_rank": 1,
                  "num_market_pairs": 500,
                  "circulating_supply": 17200062,
                  "total_supply": 17200062,
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
                  "num_market_pairs": 6089,
                  "circulating_supply": 17200062,
                  "total_supply": 17200062,
                  "max_supply": 21000000,
                  "last_updated": "2018-06-02T22:51:28.209Z",
                  "date_added": "2013-04-28T00:00:00.000Z",
                  "tags": [
                    "mineable"
                  ],
                  "platform": null,
                  "quote": {
                    "USD": {
                      "price": 1678.6501384942708,
                      "volume_24h": 7155680000,
                      "percent_change_1h": -0.152774,
                      "percent_change_24h": 0.518894,
                      "percent_change_7d": 0.986573,
                      "market_cap": 158055024432,
                      "last_updated": "2018-08-09T22:53:32.000Z"
                    }
                  },
                  "cmc_rank": 2
                }
              ],
              "status": {
                "timestamp": "2019-04-02T22:44:24.200Z",
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
                      "description": "The cryptocurrency's historic CoinMarketCap rank at the end of the requested UTC day.",
                      "example": 5
                    },
                    "num_market_pairs": {
                      "type": "integer",
                      "description": "The number of active trading pairs available for this cryptocurrency across supported exchanges.",
                      "example": 500
                    },
                    "circulating_supply": {
                      "type": "number",
                      "description": "The approximate number of coins circulating for this cryptocurrency at the end of the requested UTC day.",
                      "example": 16950100
                    },
                    "total_supply": {
                      "type": "number",
                      "description": "The approximate total amount of coins in existence right now (minus any coins that have been verifiably burned) at the end of the requested UTC day.",
                      "example": 16950100
                    },
                    "max_supply": {
                      "type": "number",
                      "description": "The expected maximum limit of coins ever to be available for this cryptocurrency.",
                      "example": 21000000
                    },
                    "last_updated": {
                      "type": "string",
                      "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                      "description": "Timestamp (ISO 8601) of when this cryptocurrency's market data was referenced for this UTC date snapshot. This is always the last update available during the UTC date requested.",
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
                            "description": "Price in the specified currency at the end of the requested UTC day.",
                            "example": 7139.82
                          },
                          "volume_24h": {
                            "type": "number",
                            "description": "24 hour adjusted volume in the specified currency at the end of the requested UTC day.",
                            "example": 4885880000
                          },
                          "market_cap": {
                            "type": "number",
                            "description": "Market cap in the specified currency at the end of the requested UTC day.",
                            "example": 121020662982
                          },
                          "percent_change_1h": {
                            "type": "number",
                            "description": "1 hour change in the specified currency at the end of the requested UTC day.",
                            "example": 0.03
                          },
                          "percent_change_24h": {
                            "type": "number",
                            "description": "24 hour change in the specified currency at the end of the requested UTC day.",
                            "example": 5.75
                          },
                          "percent_change_7d": {
                            "type": "number",
                            "description": "7 day change in the specified currency at the end of the requested UTC day.",
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
                        "__$ref": "#/components/schemas/Cryptocurrency_Listings_Latest_-_Quote_object"
                      },
                      "__$ref": "#/components/schemas/Cryptocurrency_Listings_Latest_-_Quote_map"
                    }
                  },
                  "required": [
                    "id",
                    "name",
                    "symbol",
                    "slug",
                    "cmc_rank",
                    "circulating_supply",
                    "total_supply",
                    "max_supply",
                    "last_updated",
                    "date_added",
                    "tags",
                    "platform",
                    "quote"
                  ],
                  "__$ref": "#/components/schemas/Cryptocurrency_Listings_Latest_-_Cryptocurrency_object"
                },
                "required": [
                  "Cryptocurrency Listings Latest - Cryptocurrency object"
                ],
                "__$ref": "#/components/schemas/Cryptocurrency_Listings_Latest_-_Results_array"
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
            "__$ref": "#/components/schemas/Cryptocurrency_Listings_Latest_-_Response_Model"
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
