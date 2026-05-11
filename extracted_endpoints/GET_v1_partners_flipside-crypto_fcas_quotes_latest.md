# GET /v1/partners/flipside-crypto/fcas/quotes/latest

**Summary:** FCAS Quotes Latest (deprecated)

**Description:** Returns the latest FCAS score for 1 or more cryptocurrencies. FCAS ratings are on a 0-1000 point scale with a corresponding letter grade and is updated once a day at UTC midnight.    


   
FCAS stands for Fundamental Crypto Asset Score, a single, consistently comparable value for measuring cryptocurrency project health. FCAS measures User Activity, Developer Behavior and Market Maturity and is provided by <a rel="noopener noreferrer" href="https://www.flipsidecrypto.com/" target="_blank">FlipSide Crypto</a>. Find out more about <a rel="noopener noreferrer" href="https://www.flipsidecrypto.com/fcas-explained" target="_blank">FCAS methodology</a>. Users interested in FCAS historical data including sub-component scoring may inquire through our <a rel="noopener noreferrer" href="https://pro.coinmarketcap.com/contact-data/" target="_blank">CSV Data Delivery</a> request form.  

*Disclaimer: Ratings that are calculated by third party organizations and are not influenced or endorsed by CoinMarketCap in any way.*  
  
  **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
  - Basic
  - Hobbyist
  - Startup
  - Standard
  - Professional
  - Enterprise

**Cache / Update frequency:** Once a day at UTC midnight.  
**Plan credit use:** 1 call credit per 100 FCAS scores returned (rounded up).  
**CMC equivalent pages:** The FCAS ratings available under our cryptocurrency ratings tab like [coinmarketcap.com/currencies/bitcoin/#ratings](https://coinmarketcap.com/currencies/bitcoin/#ratings).     
   
***NOTE:** Use this endpoint to request the latest FCAS score for specific cryptocurrencies. If you require FCAS for all supported cryptocurrencies use `/v1/partners/flipside-crypto/fcas/listings/latest` which is optimized for that purpose. The response data between these endpoints is otherwise the same.*

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **id** (query) - *Optional*: One or more comma-separated cryptocurrency CoinMarketCap IDs. Example: 1,2
- **slug** (query) - *Optional*: Alternatively pass a comma-separated list of cryptocurrency slugs. Example: "bitcoin,ethereum"
- **symbol** (query) - *Optional*: Alternatively pass one or more comma-separated cryptocurrency symbols. Example: "BTC,ETH". At least one "id" *or* "slug" *or* "symbol" is required for this request.
- **aux** (query) - *Optional*: Optionally specify a comma-separated list of supplemental data fields to return. Pass `point_change_24h,percent_change_24h` to include all auxiliary fields.

### Raw Data

```json
{
  "slug": "fcas-quotes-latest-deprecated",
  "summary": "FCAS Quotes Latest (deprecated)",
  "method": "get",
  "description": "Returns the latest FCAS score for 1 or more cryptocurrencies. FCAS ratings are on a 0-1000 point scale with a corresponding letter grade and is updated once a day at UTC midnight.    \n\n\n   \nFCAS stands for Fundamental Crypto Asset Score, a single, consistently comparable value for measuring cryptocurrency project health. FCAS measures User Activity, Developer Behavior and Market Maturity and is provided by <a rel=\"noopener noreferrer\" href=\"https://www.flipsidecrypto.com/\" target=\"_blank\">FlipSide Crypto</a>. Find out more about <a rel=\"noopener noreferrer\" href=\"https://www.flipsidecrypto.com/fcas-explained\" target=\"_blank\">FCAS methodology</a>. Users interested in FCAS historical data including sub-component scoring may inquire through our <a rel=\"noopener noreferrer\" href=\"https://pro.coinmarketcap.com/contact-data/\" target=\"_blank\">CSV Data Delivery</a> request form.  \n\n*Disclaimer: Ratings that are calculated by third party organizations and are not influenced or endorsed by CoinMarketCap in any way.*  \n  \n  **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**\n  - Basic\n  - Hobbyist\n  - Startup\n  - Standard\n  - Professional\n  - Enterprise\n\n**Cache / Update frequency:** Once a day at UTC midnight.  \n**Plan credit use:** 1 call credit per 100 FCAS scores returned (rounded up).  \n**CMC equivalent pages:** The FCAS ratings available under our cryptocurrency ratings tab like [coinmarketcap.com/currencies/bitcoin/#ratings](https://coinmarketcap.com/currencies/bitcoin/#ratings).     \n   \n***NOTE:** Use this endpoint to request the latest FCAS score for specific cryptocurrencies. If you require FCAS for all supported cryptocurrencies use `/v1/partners/flipside-crypto/fcas/listings/latest` which is optimized for that purpose. The response data between these endpoints is otherwise the same.*",
  "operationId": "getV1PartnersFlipsidecryptoFcasQuotesLatest",
  "contentTypes": [],
  "path": "/v1/partners/flipside-crypto/fcas/quotes/latest",
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
      "description": "One or more comma-separated cryptocurrency CoinMarketCap IDs. Example: 1,2",
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
      "name": "aux",
      "in": "query",
      "description": "Optionally specify a comma-separated list of supplemental data fields to return. Pass `point_change_24h,percent_change_24h` to include all auxiliary fields.",
      "required": null,
      "schema": {
        "type": "string",
        "pattern": "^(point_change_24h|percent_change_24h)+(?:,(point_change_24h|percent_change_24h)+)*$",
        "default": "point_change_24h,percent_change_24h"
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
                "description": "A map of cryptocurrency objects by ID or symbol (as used in query parameters).",
                "example": {
                  "1": {
                    "id": 1,
                    "name": "Bitcoin",
                    "symbol": "BTC",
                    "slug": "bitcoin",
                    "score": 894,
                    "grade": "A",
                    "percent_change_24h": 0.56,
                    "point_change_24h": 5,
                    "last_updated": "2019-08-08T00:00:00Z"
                  }
                },
                "additionalProperties": {
                  "type": "object",
                  "description": "A cryptocurrency object for each requested.",
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
                    "score": {
                      "type": "integer",
                      "description": "The cryptocurrency's current FCAS score out of 1000",
                      "example": 1000,
                      "minimum": 0,
                      "maximum": 1000
                    },
                    "grade": {
                      "type": "string",
                      "description": "The cryptocurrency's current FCAS letter grade",
                      "example": "A"
                    },
                    "percent_change_24h": {
                      "type": "number",
                      "description": "24 hour % FCAS score change",
                      "example": 0.03
                    },
                    "point_change_24h": {
                      "type": "number",
                      "description": "24 hour FCAS point change",
                      "example": 5,
                      "minimum": -1000,
                      "maximum": 1000
                    },
                    "last_updated": {
                      "type": "string",
                      "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                      "description": "Timestamp (ISO 8601) of the last time this cryptocurrency's FCAS value was updated.",
                      "example": "2018-06-02T23:59:59.999Z"
                    }
                  },
                  "required": [
                    "id",
                    "name",
                    "symbol",
                    "slug"
                  ],
                  "__$ref": "#/components/schemas/FCAS_Quote_Latest_-_Cryptocurrency_object"
                },
                "__$ref": "#/components/schemas/FCAS_Quote_Latest_-_Cryptocurrency_Results_map"
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
            "__$ref": "#/components/schemas/FCAS_Quote_Latest_-_Response_Model"
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
