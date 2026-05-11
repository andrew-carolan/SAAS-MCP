# GET /v3/index/cmc100-latest

**Summary:** CoinMarketCap 100 Index Latest

**Description:** Returns the lastest CoinMarketCap 100 Index value, constituents, and constituent weights. 		


 
 **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
 - Basic
 - Startup
 - Hobbyist
 - Standard
 - Professional
 - Enterprise

**Cache / Update frequency:** Every 5 minutes.     
**Plan credit use:** 1 call credit per API call.     
**CMC equivalent pages:** Our CoinMarketCap 100 Index on https://coinmarketcap.com/charts/cmc100/.

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key

### Raw Data

```json
{
  "slug": "coinmarketcap-100-index-latest",
  "summary": "CoinMarketCap 100 Index Latest",
  "method": "get",
  "description": "Returns the lastest CoinMarketCap 100 Index value, constituents, and constituent weights. \t\t\n\n\n \n **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**\n - Basic\n - Startup\n - Hobbyist\n - Standard\n - Professional\n - Enterprise\n\n**Cache / Update frequency:** Every 5 minutes.     \n**Plan credit use:** 1 call credit per API call.     \n**CMC equivalent pages:** Our CoinMarketCap 100 Index on https://coinmarketcap.com/charts/cmc100/.",
  "operationId": "getV3IndexCMC100Latest",
  "contentTypes": [],
  "path": "/v3/index/cmc100-latest",
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
                "description": "The latest CoinMarketCap 100 Index value is returned in this object.",
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
                        }
                      },
                      "type": "object",
                      "__$ref": "#/components/schemas/IndexDetailDTO"
                    },
                    "type": "array"
                  },
                  "last_update": {
                    "description": "Timestamp (ISO 8601) of the last time this record was updated.",
                    "type": "string",
                    "format": "date"
                  },
                  "next_update": {
                    "description": "Timestamp (ISO 8601) of the next time this record will be updated.",
                    "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                    "type": "string"
                  },
                  "value": {
                    "description": "Current value of CoinMarketCap 100 Index.",
                    "format": "bigdecimal",
                    "type": "number"
                  },
                  "value_24h_percentage_change": {
                    "description": "Percentage change of the CoinMarketCap 100 Index over the past 24h. ",
                    "format": "bigdecimal",
                    "type": "number"
                  }
                },
                "type": "object",
                "__$ref": "#/components/schemas/IndexLatestDTO"
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
            "required": [
              "data"
            ],
            "type": "object",
            "__$ref": "#/components/schemas/ApiResponseOfIndexLatestResponseDTO"
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
