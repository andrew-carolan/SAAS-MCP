# GET /v1/exchange/map

**Summary:** CoinMarketCap ID Map

**Description:** Returns a paginated list of all active cryptocurrency exchanges by CoinMarketCap ID. We recommend using this convenience endpoint to lookup and utilize our unique exchange `id` across all endpoints as typical exchange identifiers may change over time. As a convenience you may pass a comma-separated list of exchanges by `slug` to filter this list to only those you require or the `aux` parameter to slim down the payload.

By default this endpoint returns exchanges that have at least 1 actively tracked market. You may receive a map of all inactive cryptocurrencies by passing `listing_status=inactive`. You may also receive a map of registered exchanges that are listed but do not yet meet methodology requirements to have tracked markets available via `listing_status=untracked`. Please review **(3) Listing Tiers** in our <a target="_blank" href="https://coinmarketcap.com/methodology/">methodology documentation</a> for additional details on listing states. 

**This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
  - Basic
  - Hobbyist
  - Startup
  - Standard
  - Professional
  - Enterprise

**Cache / Update frequency:** Mapping data is updated only as needed, every 30 seconds.  
**Plan credit use:** 1 call credit per call.  
**CMC equivalent pages:** No equivalent, this data is only available via API.  

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **listing_status** (query) - *Optional*: Only active exchanges are returned by default. Pass `inactive` to get a list of exchanges that are no longer active. Pass `untracked` to get a list of exchanges that are registered but do not currently meet methodology requirements to have active markets tracked. You may pass one or more comma-separated values.
- **slug** (query) - *Optional*: Optionally pass a comma-separated list of exchange slugs (lowercase URL friendly shorthand name with spaces replaced with dashes) to return CoinMarketCap IDs for. If this option is passed, other options will be ignored.
- **start** (query) - *Optional*: Optionally offset the start (1-based index) of the paginated list of items to return.
- **limit** (query) - *Optional*: Optionally specify the number of results to return. Use this parameter and the "start" parameter to determine your own pagination size.
- **sort** (query) - *Optional*: What field to sort the list of exchanges by.
- **aux** (query) - *Optional*: Optionally specify a comma-separated list of supplemental data fields to return. Pass `first_historical_data,last_historical_data,is_active,status` to include all auxiliary fields.
- **crypto_id** (query) - *Optional*: Optionally include one fiat or cryptocurrency IDs to filter market pairs by. For example `?crypto_id=1` would only return exchanges that have BTC.

### Raw Data

```json
{
  "slug": "coinmarketcap-id-map-2",
  "summary": "CoinMarketCap ID Map",
  "method": "get",
  "description": "Returns a paginated list of all active cryptocurrency exchanges by CoinMarketCap ID. We recommend using this convenience endpoint to lookup and utilize our unique exchange `id` across all endpoints as typical exchange identifiers may change over time. As a convenience you may pass a comma-separated list of exchanges by `slug` to filter this list to only those you require or the `aux` parameter to slim down the payload.\n\nBy default this endpoint returns exchanges that have at least 1 actively tracked market. You may receive a map of all inactive cryptocurrencies by passing `listing_status=inactive`. You may also receive a map of registered exchanges that are listed but do not yet meet methodology requirements to have tracked markets available via `listing_status=untracked`. Please review **(3) Listing Tiers** in our <a target=\"_blank\" href=\"https://coinmarketcap.com/methodology/\">methodology documentation</a> for additional details on listing states. \n\n**This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**\n  - Basic\n  - Hobbyist\n  - Startup\n  - Standard\n  - Professional\n  - Enterprise\n\n**Cache / Update frequency:** Mapping data is updated only as needed, every 30 seconds.  \n**Plan credit use:** 1 call credit per call.  \n**CMC equivalent pages:** No equivalent, this data is only available via API.  ",
  "operationId": "getV1ExchangeMap",
  "contentTypes": [],
  "path": "/v1/exchange/map",
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
      "name": "listing_status",
      "in": "query",
      "description": "Only active exchanges are returned by default. Pass `inactive` to get a list of exchanges that are no longer active. Pass `untracked` to get a list of exchanges that are registered but do not currently meet methodology requirements to have active markets tracked. You may pass one or more comma-separated values.",
      "required": null,
      "schema": {
        "type": "string",
        "pattern": "^(active|inactive|untracked)+(?:,(active|inactive|untracked)+)*$",
        "default": "active"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "slug",
      "in": "query",
      "description": "Optionally pass a comma-separated list of exchange slugs (lowercase URL friendly shorthand name with spaces replaced with dashes) to return CoinMarketCap IDs for. If this option is passed, other options will be ignored.",
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
        "maximum": 5000
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
          "volume_24h",
          "id"
        ],
        "default": "id"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "aux",
      "in": "query",
      "description": "Optionally specify a comma-separated list of supplemental data fields to return. Pass `first_historical_data,last_historical_data,is_active,status` to include all auxiliary fields.",
      "required": null,
      "schema": {
        "type": "string",
        "pattern": "^(first_historical_data|last_historical_data|is_active|status)+(?:,(first_historical_data|last_historical_data|is_active|status)+)*$",
        "default": "first_historical_data,last_historical_data,is_active"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "crypto_id",
      "in": "query",
      "description": "Optionally include one fiat or cryptocurrency IDs to filter market pairs by. For example `?crypto_id=1` would only return exchanges that have BTC.",
      "required": null,
      "schema": {
        "type": "string",
        "pattern": "^\\d*$"
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
                "description": "Array of exchange object results.",
                "items": {
                  "type": "object",
                  "description": "Exchange object description",
                  "properties": {
                    "id": {
                      "type": "integer",
                      "description": "The unique CoinMarketCap ID for this exchange.",
                      "example": 270
                    },
                    "name": {
                      "type": "string",
                      "description": "The name of this exchange.",
                      "example": "Binance"
                    },
                    "slug": {
                      "type": "string",
                      "description": "The web URL friendly shorthand version of this exchange name.",
                      "example": "binance"
                    },
                    "is_active": {
                      "type": "integer",
                      "description": "1 if this exchange is still being actively tracked and updated, otherwise 0.",
                      "example": 1,
                      "minimum": 0,
                      "maximum": 1
                    },
                    "status": {
                      "type": "string",
                      "description": "The listing status of the exchange. *This field is only returned if requested through the `aux` request parameter.*",
                      "example": "active",
                      "enum": [
                        "active",
                        "inactive",
                        "untracked"
                      ]
                    },
                    "first_historical_data": {
                      "type": "string",
                      "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                      "description": "Timestamp (ISO 8601) of the earliest market data record available to query using our historical endpoints. `null` if there is no historical data currently available for this exchange.",
                      "example": "2018-04-26T00:45:00.000Z"
                    },
                    "last_historical_data": {
                      "type": "string",
                      "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                      "description": "Timestamp (ISO 8601) of the latest market data record available to query using our historical endpoints. `null` if there is no historical data currently available for this exchange.",
                      "example": "2019-06-02T21:25:00.000Z"
                    }
                  },
                  "required": [
                    "id",
                    "name",
                    "slug"
                  ],
                  "__$ref": "#/components/schemas/Exchange_Map_-_Exchange_Object"
                },
                "__$ref": "#/components/schemas/Exchange_Map_-_Exchanges_Array"
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
            "__$ref": "#/components/schemas/Exchange_Map_-_Response_Model"
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
