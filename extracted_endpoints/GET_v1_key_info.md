# GET /v1/key/info

**Summary:** Key Info

**Description:** Returns API key details and usage stats. This endpoint can be used to programmatically monitor your key usage compared to the rate limit and daily/monthly credit limits available to your API plan. You may use the Developer Portal's account dashboard as an alternative to this endpoint.

  **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
  - Basic
  - Hobbyist
  - Startup
  - Standard
  - Professional
  - Enterprise

  **Cache / Update frequency:** No cache, this endpoint updates as requests are made with your key.  
  **Plan credit use:** No API credit cost. Requests to this endpoint do contribute to your minute based rate limit however.  
  **CMC equivalent pages:** Our Developer Portal dashboard for your API Key at [pro.coinmarketcap.com/account](https://pro.coinmarketcap.com/account).

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key

### Raw Data

```json
{
  "slug": "key-info",
  "summary": "Key Info",
  "method": "get",
  "description": "Returns API key details and usage stats. This endpoint can be used to programmatically monitor your key usage compared to the rate limit and daily/monthly credit limits available to your API plan. You may use the Developer Portal's account dashboard as an alternative to this endpoint.\n\n  **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**\n  - Basic\n  - Hobbyist\n  - Startup\n  - Standard\n  - Professional\n  - Enterprise\n\n  **Cache / Update frequency:** No cache, this endpoint updates as requests are made with your key.  \n  **Plan credit use:** No API credit cost. Requests to this endpoint do contribute to your minute based rate limit however.  \n  **CMC equivalent pages:** Our Developer Portal dashboard for your API Key at [pro.coinmarketcap.com/account](https://pro.coinmarketcap.com/account).",
  "operationId": "getV1KeyInfo",
  "contentTypes": [],
  "path": "/v1/key/info",
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
                "description": "Details about your API key are returned in this object.",
                "properties": {
                  "plan": {
                    "type": "object",
                    "description": "Object containing rate limit and daily/monthly credit limit details for your API Key.",
                    "properties": {
                      "credit_limit_monthly": {
                        "type": "number",
                        "description": "The number of API credits that can be used each monthly period before receiving a HTTP 429 rate limit error. This limit is based on the API plan tier.",
                        "example": 120000
                      },
                      "credit_limit_monthly_reset": {
                        "type": "string",
                        "description": "A human readable countdown of when the API key monthly credit limit will reset back to 0.",
                        "example": "In 3 days, 19 hours, 56 minutes"
                      },
                      "credit_limit_monthly_reset_timestamp": {
                        "type": "string",
                        "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                        "description": "Timestamp (ISO 8601) of when the monthly credit limit will reset. This is based on your billing plan activation date for premium subscription based keys or calendar month UTC midnight for free Basic plan keys.",
                        "example": "2019-09-01T00:00:00.000Z"
                      },
                      "rate_limit_minute": {
                        "type": "number",
                        "description": "The number of API calls that can be made within the same UTC minute before receiving a HTTP 429 rate limit error. This limit is based on the API plan tier.",
                        "example": 60
                      }
                    },
                    "required": [
                      "credit_limit_monthly",
                      "credit_limit_monthly_reset",
                      "credit_limit_monthly_reset_timestamp",
                      "rate_limit_minute"
                    ],
                    "__$ref": "#/components/schemas/plan"
                  },
                  "usage": {
                    "type": "object",
                    "description": "Object containing live usage details about your API Key.",
                    "properties": {
                      "current_minute": {
                        "type": "object",
                        "description": "Usage stats around the minute based rate limit.",
                        "properties": {
                          "requests_made": {
                            "type": "number",
                            "description": "The number of API calls that have been made in the current UTC minute.",
                            "example": 1
                          },
                          "requests_left": {
                            "type": "number",
                            "description": "The number of remaining API calls that can be made in the current UTC minute before receiving a HTTP 429 rate limit error. This limit resets each UTC minute.",
                            "example": 59
                          }
                        },
                        "required": [
                          "requests_made",
                          "requests_left"
                        ],
                        "__$ref": "#/components/schemas/current_minute"
                      },
                      "current_day": {
                        "type": "object",
                        "description": "Usage stats around the daily API credit limit.",
                        "properties": {
                          "credits_used": {
                            "type": "number",
                            "description": "The number of API credits used during the current daily period.",
                            "example": 1
                          },
                          "credits_left": {
                            "type": "number",
                            "description": "The number of remaining API credits that can be used during the current daily period before receiving a HTTP 429 rate limit error. This limit resets at the end of each daily period.",
                            "example": 3999
                          }
                        },
                        "required": [
                          "credits_used",
                          "credits_left"
                        ],
                        "__$ref": "#/components/schemas/current_day"
                      },
                      "current_month": {
                        "type": "object",
                        "description": "Usage stats around the monthly API credit limit.",
                        "properties": {
                          "credits_used": {
                            "type": "number",
                            "description": "The number of API credits used during the current monthly period.",
                            "example": 1
                          },
                          "credits_left": {
                            "type": "number",
                            "description": "The number of remaining API credits that can be used during the current monthly period before receiving a HTTP 429 rate limit error. This limit resets at the end of each monthly period.",
                            "example": 119999
                          }
                        },
                        "required": [
                          "credits_used",
                          "credits_left"
                        ],
                        "__$ref": "#/components/schemas/current_month"
                      }
                    },
                    "required": [
                      "current_minute",
                      "current_day",
                      "current_month"
                    ],
                    "__$ref": "#/components/schemas/usage"
                  }
                },
                "required": [
                  "plan",
                  "usage"
                ],
                "__$ref": "#/components/schemas/Account_Info_-_Response_Object"
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
            "__$ref": "#/components/schemas/Account_Info_-_Response_Model"
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
