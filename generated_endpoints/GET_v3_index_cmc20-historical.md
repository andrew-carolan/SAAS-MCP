# GET /v3/index/cmc20-historical

**Summary:** CoinMarketCap 20 Index Historical

**Description:** Returns an interval of historic CoinMarketCap 20 Index values based on the interval parameter. 		


 
 **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
 - Basic
 - Startup
 - Hobbyist
 - Standard
 - Professional
 - Enterprise

**Cache / Update frequency:** Every 5 minutes.     
**Plan credit use:** 1 API call credit per request no matter query size.     
**CMC equivalent pages:** Our CoinMarketCap 20 Index on https://coinmarketcap.com/charts/cmc20/.

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **time_start** (query) - *Optional*: Timestamp (Unix or ISO 8601) to start returning CoinMarketCap 20 Index data for. Optional, if not passed, we'll return quotes calculated in reverse from "time_end".
- **time_end** (query) - *Optional*: Timestamp (Unix or ISO 8601) to stop returning CoinMarketCap 20 Index data for (inclusive). Optional, if not passed, we'll default to the current time. If no "time_start" is passed, we return quotes in reverse order starting from this time.
- **count** (query) - *Optional*: The number of interval periods to return results for. Optional, required if both "time_start" and "time_end" aren't supplied. The default is 5 items. If "time_start" and "time_end" are supplied, the query limit is 10 and the count starts from "time_start".
- **interval** (query) - *Optional*: Optionally adjust the interval of data returned.Valid values:"5m","15m","daily".

### Raw Data

```json
{
  "slug": "coinmarketcap-20-index-historical",
  "summary": "CoinMarketCap 20 Index Historical",
  "method": "get",
  "description": "Returns an interval of historic CoinMarketCap 20 Index values based on the interval parameter. \t\t\n\n\n \n **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**\n - Basic\n - Startup\n - Hobbyist\n - Standard\n - Professional\n - Enterprise\n\n**Cache / Update frequency:** Every 5 minutes.     \n**Plan credit use:** 1 API call credit per request no matter query size.     \n**CMC equivalent pages:** Our CoinMarketCap 20 Index on https://coinmarketcap.com/charts/cmc20/.",
  "operationId": "getV3IndexCMC20Historical",
  "contentTypes": [],
  "path": "/v3/index/cmc20-historical",
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
      "name": "time_start",
      "in": "query",
      "description": "Timestamp (Unix or ISO 8601) to start returning CoinMarketCap 20 Index data for. Optional, if not passed, we'll return quotes calculated in reverse from \"time_end\".",
      "required": false,
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
      "description": "Timestamp (Unix or ISO 8601) to stop returning CoinMarketCap 20 Index data for (inclusive). Optional, if not passed, we'll default to the current time. If no \"time_start\" is passed, we return quotes in reverse order starting from this time.",
      "required": false,
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
      "description": "The number of interval periods to return results for. Optional, required if both \"time_start\" and \"time_end\" aren't supplied. The default is 5 items. If \"time_start\" and \"time_end\" are supplied, the query limit is 10 and the count starts from \"time_start\".",
      "required": false,
      "schema": {
        "type": "string"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "interval",
      "in": "query",
      "description": "Optionally adjust the interval of data returned.Valid values:\"5m\",\"15m\",\"daily\".",
      "required": false,
      "schema": {
        "type": "string"
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
      "description": "Succeeded response",
      "content": [
        {
          "examples": [],
          "mediaType": "application/json",
          "encoding": null,
          "schema": {
            "properties": {
              "data": {
                "items": {
                  "properties": {
                    "constituents": {
                      "description": "Array detailing the list of constituents and their weightage.",
                      "items": {
                        "properties": {
                          "id": {
                            "description": "The unique CoinMarketCap ID for this cryptocurrency.",
                            "format": "int32",
                            "type": "integer"
                          },
                          "name": {
                            "description": "The name of this cryptocurrency.",
                            "type": "string"
                          },
                          "symbol": {
                            "description": "The ticker symbol for this cryptocurrency.",
                            "type": "string"
                          },
                          "url": {
                            "description": "The URL of the detail page on CoinMarketCap for this cryptocurrency.",
                            "type": "string"
                          },
                          "weight": {
                            "description": "The relative proportion of this constituent within the index expressed as a percentage.",
                            "format": "bigdecimal",
                            "type": "number"
                          },
                          "priceUsd": {
                            "description": "The price of this cryptocurrency in USD.",
                            "format": "bigdecimal",
                            "type": "number"
                          },
                          "units": {
                            "description": "The units of this cryptocurrency.",
                            "format": "bigdecimal",
                            "type": "number"
                          }
                        },
                        "type": "object",
                        "__$ref": "#/components/schemas/CMC20IndexDetailDTO"
                      },
                      "type": "array"
                    },
                    "update_time": {
                      "description": "Timestamp (ISO 8601) of the time this record was updated.",
                      "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                      "type": "string"
                    },
                    "value": {
                      "description": "Value of CoinMarketCap 20 Index.",
                      "format": "bigdecimal",
                      "type": "number"
                    }
                  },
                  "type": "object",
                  "__$ref": "#/components/schemas/CMC20IndexHistoricalDTO"
                },
                "type": "array",
                "__$ref": "#/components/schemas/CMC20IndexHistoricalDpsDTO"
              },
              "status": {
                "properties": {
                  "credit_count": {
                    "description": "Number of credits used for the request",
                    "format": "int32",
                    "type": "integer"
                  },
                  "elapsed": {
                    "description": "Time taken to process the request",
                    "format": "int64",
                    "type": "integer"
                  },
                  "error_code": {
                    "description": "Error code of the response",
                    "type": "string"
                  },
                  "error_message": {
                    "description": "Error message of the response, if any",
                    "type": "string"
                  },
                  "notice": {
                    "description": "Api notice message of the response",
                    "type": "string"
                  },
                  "timestamp": {
                    "description": "Timestamp of the response",
                    "format": "date-time",
                    "type": "string"
                  },
                  "total_count": {
                    "description": "Number of data size",
                    "format": "int64",
                    "type": "integer"
                  }
                },
                "type": "object",
                "__$ref": "#/components/schemas/ProApiResponseStatus"
              }
            },
            "type": "object",
            "__$ref": "#/components/schemas/ApiResponseOfCMC20IndexHistoricalResponseDTO"
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
