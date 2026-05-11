# GET /v1/cryptocurrency/airdrop

**Summary:** Airdrop

**Description:** Returns information about a single airdrop available on CoinMarketCap. Includes the cryptocurrency metadata. 

  **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
  - Hobbyist
  - Startup
  - Standard
  - Professional
  - Enterprise

**Cache / Update frequency:** Data is updated only as needed, every 30 seconds.  
**Plan credit use:** 1 API call credit per request no matter query size.  
**CMC equivalent pages:** Our free airdrops page [coinmarketcap.com/airdrop/](https://coinmarketcap.com/airdrop/).

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **id** (query) - *Required*: Airdrop Unique ID. This can be found using the Airdrops API.

### Raw Data

```json
{
  "slug": "airdrop",
  "summary": "Airdrop",
  "method": "get",
  "description": "Returns information about a single airdrop available on CoinMarketCap. Includes the cryptocurrency metadata. \n\n  **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**\n  - Hobbyist\n  - Startup\n  - Standard\n  - Professional\n  - Enterprise\n\n**Cache / Update frequency:** Data is updated only as needed, every 30 seconds.  \n**Plan credit use:** 1 API call credit per request no matter query size.  \n**CMC equivalent pages:** Our free airdrops page [coinmarketcap.com/airdrop/](https://coinmarketcap.com/airdrop/).",
  "operationId": "getV1CryptocurrencyAirdrop",
  "contentTypes": [],
  "path": "/v1/cryptocurrency/airdrop",
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
      "description": "Airdrop Unique ID. This can be found using the Airdrops API.",
      "required": true,
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
                    "id": "60e59b99c8ca1d58514a2322",
                    "project_name": "DeRace Airdrop",
                    "description": "For 7 days starting from August 15, 2021, CoinMarketCap will host an Airdrop event...",
                    "status": "UPCOMING",
                    "coin": {
                      "id": 10744,
                      "name": "DeRace",
                      "slug": "derace",
                      "symbol": "DERC"
                    },
                    "start_date": "2021-06-01T22:11:00.000Z",
                    "end_date": "2021-07-01T22:11:00.000Z",
                    "total_prize": 20000000000,
                    "winner_count": 1000,
                    "link": "https://coinmarketcap.com/currencies/derace/airdrop/"
                  }
                },
                "additionalProperties": {
                  "type": "object",
                  "description": "A results object for the airdrop requested.",
                  "properties": {
                    "id": {
                      "type": "string",
                      "description": "The unique ID of the airdrop",
                      "example": "60e59b99c8ca1d58514a2322"
                    },
                    "project_name": {
                      "type": "string",
                      "description": "The project name",
                      "example": "DeRace Airdrop"
                    },
                    "description": {
                      "type": "string",
                      "description": "The description of the airdrop.",
                      "example": "For 7 days starting from August 15, 2021, CoinMarketCap will host an Airdrop event..."
                    },
                    "status": {
                      "type": "string",
                      "description": "The current status of the airdrop.",
                      "example": "UPCOMING"
                    },
                    "coin": {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "integer",
                          "description": "The unique CoinMarketCap ID for this asset.",
                          "example": 2781
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
                        }
                      },
                      "required": [
                        "id",
                        "name",
                        "symbol",
                        "slug"
                      ],
                      "__$ref": "#/components/schemas/coin"
                    },
                    "start_date": {
                      "type": "string",
                      "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                      "description": "Timestamp (ISO 8601) of when this cryptocurrency was added to CoinMarketCap.",
                      "example": "2013-04-28T00:00:00.000Z"
                    },
                    "end_date": {
                      "type": "string",
                      "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                      "description": "Timestamp (ISO 8601) of when this cryptocurrency was added to CoinMarketCap.",
                      "example": "2013-04-28T00:00:00.000Z"
                    },
                    "total_prize": {
                      "type": "integer",
                      "example": 10000
                    },
                    "winner_count": {
                      "type": "integer",
                      "example": 55
                    },
                    "link": {
                      "type": "string",
                      "description": "A link to the airdrop information.",
                      "example": "https://coinmarketcap.com/currencies/derace/airdrop"
                    }
                  },
                  "required": [
                    "id",
                    "start_date",
                    "end_date"
                  ],
                  "__$ref": "#/components/schemas/Airdrop_-_Airdrop_object"
                },
                "__$ref": "#/components/schemas/Airdrop_-_Results_map"
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
            "__$ref": "#/components/schemas/Airdrop_-_Response_Model"
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
