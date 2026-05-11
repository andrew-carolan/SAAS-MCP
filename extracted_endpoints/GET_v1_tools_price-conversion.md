# GET /v1/tools/price-conversion

**Summary:** Price Conversion v1 (deprecated)

**Description:** Convert an amount of one cryptocurrency or fiat currency into one or more different currencies utilizing the latest market rate for each currency. You may optionally pass a historical timestamp as `time` to convert values based on historical rates (as your API plan supports). 
  
  
**Technical Notes**
- Latest market rate conversions are accurate to 1 minute of specificity. Historical conversions are accurate to 1 minute of specificity outside of non-USD fiat conversions which have 5 minute specificity. 
- You may reference a current list of all supported cryptocurrencies via the [cryptocurrency/map](/pro-api-reference/cryptocurrency#coinmarketcap-id-map) endpoint. This endpoint also returns the supported date ranges for historical conversions via the `first_historical_data` and `last_historical_data` properties.   
- Conversions are supported in 93 different fiat currencies and 4 precious metals [as outlined here](/guides/standards-and-conventions). Historical fiat conversions are supported as far back as 2013-04-28.
- A `last_updated` timestamp is included for both your source currency and each conversion currency. This is the timestamp of the closest market rate record referenced for each currency during the conversion.  

**This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
- Basic (Latest market price conversions)
- Hobbyist (Latest market price conversions + 1 month historical)
- Startup (Latest market price conversions + 1 month historical)
- Standard (Latest market price conversions + 3 months historical)
- Professional (Latest market price conversions + 12 months historical)
- Enterprise (Latest market price conversions + up to 6 years historical)

**Cache / Update frequency:** Every 60 seconds for the lastest cryptocurrency and fiat currency rates.    
**Plan credit use:** 1 call credit per call and 1 call credit per `convert` option beyond the first.  
**CMC equivalent pages:** Our cryptocurrency conversion page at [coinmarketcap.com/converter/](https://coinmarketcap.com/converter/).  

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **amount** (query) - *Required*: An amount of currency to convert. Example: 10.43
- **id** (query) - *Optional*: The CoinMarketCap currency ID of the base cryptocurrency or fiat to convert from. Example: "1"
- **symbol** (query) - *Optional*: Alternatively the currency symbol of the base cryptocurrency or fiat to convert from. Example: "BTC". One "id" *or* "symbol" is required. Please note that starting in the v2 endpoint, due to the fact that a symbol is not unique, if you request by symbol each quote response will contain an array of objects containing all of the coins that use each requested symbol. The v1 endpoint will still return a single object, the highest ranked coin using that symbol.
- **time** (query) - *Optional*: Optional timestamp (Unix or ISO 8601) to reference historical pricing during conversion. If not passed, the current time will be used. If passed, we'll reference the closest historic values available for this conversion.
- **convert** (query) - *Optional*: Pass up to 120 comma-separated fiat or cryptocurrency symbols to convert the source amount to.
- **convert_id** (query) - *Optional*: Optionally calculate market quotes by CoinMarketCap ID instead of symbol. This option is identical to `convert` outside of ID format. Ex: convert_id=1,2781 would replace convert=BTC,USD in your query. This parameter cannot be used when `convert` is used.

### Raw Data

```json
{
  "slug": "price-conversion-v1-deprecated",
  "summary": "Price Conversion v1 (deprecated)",
  "method": "get",
  "description": "Convert an amount of one cryptocurrency or fiat currency into one or more different currencies utilizing the latest market rate for each currency. You may optionally pass a historical timestamp as `time` to convert values based on historical rates (as your API plan supports). \n  \n  \n**Technical Notes**\n- Latest market rate conversions are accurate to 1 minute of specificity. Historical conversions are accurate to 1 minute of specificity outside of non-USD fiat conversions which have 5 minute specificity. \n- You may reference a current list of all supported cryptocurrencies via the [cryptocurrency/map](/pro-api-reference/cryptocurrency#coinmarketcap-id-map) endpoint. This endpoint also returns the supported date ranges for historical conversions via the `first_historical_data` and `last_historical_data` properties.   \n- Conversions are supported in 93 different fiat currencies and 4 precious metals [as outlined here](/guides/standards-and-conventions). Historical fiat conversions are supported as far back as 2013-04-28.\n- A `last_updated` timestamp is included for both your source currency and each conversion currency. This is the timestamp of the closest market rate record referenced for each currency during the conversion.  \n\n**This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**\n- Basic (Latest market price conversions)\n- Hobbyist (Latest market price conversions + 1 month historical)\n- Startup (Latest market price conversions + 1 month historical)\n- Standard (Latest market price conversions + 3 months historical)\n- Professional (Latest market price conversions + 12 months historical)\n- Enterprise (Latest market price conversions + up to 6 years historical)\n\n**Cache / Update frequency:** Every 60 seconds for the lastest cryptocurrency and fiat currency rates.    \n**Plan credit use:** 1 call credit per call and 1 call credit per `convert` option beyond the first.  \n**CMC equivalent pages:** Our cryptocurrency conversion page at [coinmarketcap.com/converter/](https://coinmarketcap.com/converter/).  ",
  "operationId": "getV1ToolsPriceconversion",
  "contentTypes": [],
  "path": "/v1/tools/price-conversion",
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
      "name": "amount",
      "in": "query",
      "description": "An amount of currency to convert. Example: 10.43",
      "required": true,
      "schema": {
        "type": "number",
        "minimum": 1e-08,
        "maximum": 1000000000000
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "id",
      "in": "query",
      "description": "The CoinMarketCap currency ID of the base cryptocurrency or fiat to convert from. Example: \"1\"",
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
      "name": "symbol",
      "in": "query",
      "description": "Alternatively the currency symbol of the base cryptocurrency or fiat to convert from. Example: \"BTC\". One \"id\" *or* \"symbol\" is required. Please note that starting in the v2 endpoint, due to the fact that a symbol is not unique, if you request by symbol each quote response will contain an array of objects containing all of the coins that use each requested symbol. The v1 endpoint will still return a single object, the highest ranked coin using that symbol.",
      "required": null,
      "schema": {
        "type": "string",
        "pattern": "^[0-9A-Za-z$@\\-]*$"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "time",
      "in": "query",
      "description": "Optional timestamp (Unix or ISO 8601) to reference historical pricing during conversion. If not passed, the current time will be used. If passed, we'll reference the closest historic values available for this conversion.",
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
      "name": "convert",
      "in": "query",
      "description": "Pass up to 120 comma-separated fiat or cryptocurrency symbols to convert the source amount to.",
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
                "example": {
                  "symbol": "BTC",
                  "id": 1,
                  "name": "Bitcoin",
                  "amount": 50,
                  "last_updated": "2018-06-06T08:04:36.000Z",
                  "quote": {
                    "USD": {
                      "price": 284656.08465608465,
                      "last_updated": "2018-06-06T06:00:00.000Z"
                    }
                  }
                },
                "properties": {
                  "id": {
                    "type": "integer",
                    "description": "The unique CoinMarketCap ID for your base currency.",
                    "example": 1
                  },
                  "name": {
                    "type": "string",
                    "description": "The name of your base currency.",
                    "example": "Bitcoin"
                  },
                  "symbol": {
                    "type": "string",
                    "description": "The symbol for your base currency.",
                    "example": "BTC"
                  },
                  "amount": {
                    "type": "number",
                    "description": "Amount of base currency to convert from.",
                    "example": 50
                  },
                  "last_updated": {
                    "type": "string",
                    "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                    "description": "Timestamp (ISO 8601) of when the referenced market value of the base currency was recorded.",
                    "example": "2018-06-02T00:00:00.000Z"
                  },
                  "quote": {
                    "type": "object",
                    "description": "An object map of price conversions.",
                    "additionalProperties": {
                      "type": "object",
                      "description": "A quote object for each conversion requested. The map key being the id/symbol used in the request.",
                      "properties": {
                        "price": {
                          "type": "number",
                          "description": "Converted price in terms of the quoted currency and historic time (if supplied).",
                          "example": 1235000
                        },
                        "last_updated": {
                          "type": "string",
                          "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                          "description": "Timestamp (ISO 8601) of when the destination currency's market value was recorded.",
                          "example": "2018-06-02T00:00:00.000Z"
                        }
                      },
                      "required": [
                        "price",
                        "last_updated"
                      ],
                      "__$ref": "#/components/schemas/Tools_Price_Conversion_-_Quote_object"
                    },
                    "__$ref": "#/components/schemas/Tools_Price_Conversion_-_Quotes_map._Please_note_this_will_be_wrapped_in_an_array_if_you_request_by_symbol_using_the_v2_endpoint."
                  }
                },
                "required": [
                  "id",
                  "name",
                  "symbol",
                  "amount",
                  "last_updated",
                  "quote"
                ],
                "__$ref": "#/components/schemas/Tools_Price_Conversion_-_Results_Object"
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
            "__$ref": "#/components/schemas/Tools_Price_Conversion_-_Response_Model"
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
