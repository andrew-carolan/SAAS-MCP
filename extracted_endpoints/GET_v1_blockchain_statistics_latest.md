# GET /v1/blockchain/statistics/latest

**Summary:** Statistics Latest

**Description:** Returns the latest blockchain statistics data for 1 or more blockchains. Bitcoin, Litecoin, and Ethereum are currently supported. Additional blockchains will be made available on a regular basis.  


 
  **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
  - ~~Basic~~
  - ~~Hobbyist~~
  - ~~Startup~~
  - ~~Standard~~
  - ~~Professional~~
  - Enterprise

**Cache / Update frequency:** Every 15 seconds.  
**Plan credit use:** 1 call credit per request.  
**CMC equivalent pages:** Our blockchain explorer pages like [blockchain.coinmarketcap.com/](https://blockchain.coinmarketcap.com/).

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **id** (query) - *Optional*: One or more comma-separated cryptocurrency CoinMarketCap IDs to return blockchain data for. Pass `1,2,1027` to request all currently supported blockchains.
- **symbol** (query) - *Optional*: Alternatively pass one or more comma-separated cryptocurrency symbols. Pass `BTC,LTC,ETH` to request all currently supported blockchains.
- **slug** (query) - *Optional*: Alternatively pass a comma-separated list of cryptocurrency slugs. Pass `bitcoin,litecoin,ethereum` to request all currently supported blockchains.

### Raw Data

```json
{
  "slug": "statistics-latest",
  "summary": "Statistics Latest",
  "method": "get",
  "description": "Returns the latest blockchain statistics data for 1 or more blockchains. Bitcoin, Litecoin, and Ethereum are currently supported. Additional blockchains will be made available on a regular basis.  \n\n\n \n  **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**\n  - ~~Basic~~\n  - ~~Hobbyist~~\n  - ~~Startup~~\n  - ~~Standard~~\n  - ~~Professional~~\n  - Enterprise\n\n**Cache / Update frequency:** Every 15 seconds.  \n**Plan credit use:** 1 call credit per request.  \n**CMC equivalent pages:** Our blockchain explorer pages like [blockchain.coinmarketcap.com/](https://blockchain.coinmarketcap.com/).",
  "operationId": "getV1BlockchainStatisticsLatest",
  "contentTypes": [],
  "path": "/v1/blockchain/statistics/latest",
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
      "description": "One or more comma-separated cryptocurrency CoinMarketCap IDs to return blockchain data for. Pass `1,2,1027` to request all currently supported blockchains.",
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
      "name": "symbol",
      "in": "query",
      "description": "Alternatively pass one or more comma-separated cryptocurrency symbols. Pass `BTC,LTC,ETH` to request all currently supported blockchains.",
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
      "name": "slug",
      "in": "query",
      "description": "Alternatively pass a comma-separated list of cryptocurrency slugs. Pass `bitcoin,litecoin,ethereum` to request all currently supported blockchains.",
      "required": null,
      "schema": {
        "type": "string",
        "pattern": "^[0-9a-z-]+(?:,[0-9a-z-]+)*$"
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
                "description": "A map of blockchain objects by ID, symbol, or slug (as used in query parameters).",
                "example": {
                  "1": {
                    "id": 1,
                    "slug": "bitcoin",
                    "symbol": "BTC",
                    "block_reward_static": 12.5,
                    "consensus_mechanism": "proof-of-work",
                    "difficulty": "11890594958796",
                    "hashrate_24h": "85116194130018810000",
                    "pending_transactions": 1177,
                    "reduction_rate": "50%",
                    "total_blocks": 595165,
                    "total_transactions": "455738994",
                    "tps_24h": 3.808090277777778,
                    "first_block_timestamp": "2009-01-09T02:54:25.000Z"
                  }
                },
                "additionalProperties": {
                  "type": "object",
                  "description": "A blockchain object for every blockchain that matched list options.",
                  "properties": {
                    "id": {
                      "type": "integer",
                      "description": "The unique CoinMarketCap ID for this blockchain's cryptocurrency.",
                      "example": 1
                    },
                    "slug": {
                      "type": "string",
                      "description": "The web URL friendly shorthand version of the cryptocurrency's name.",
                      "example": "bitcoin"
                    },
                    "symbol": {
                      "type": "string",
                      "description": "The ticker symbol for the cryptocurrency.",
                      "example": "BTC"
                    },
                    "block_reward_static": {
                      "type": "number",
                      "description": "The reward assigned to the miner of a block excluding fees.",
                      "example": 12.5
                    },
                    "consensus_mechanism": {
                      "type": "string",
                      "description": "The consensus mechanism used by the blockchain, for example, \"proof-of-work\" or \"proof-of-stake\".",
                      "example": "proof-of-work"
                    },
                    "difficulty": {
                      "type": "string",
                      "description": "The global block difficulty determining how hard to find a hash on this blockchain. *Note: This integer is returned as a string to use with BigInt libraries as it may exceed the max safe integer size for many programming languages.*",
                      "example": "2264398029247833"
                    },
                    "hashrate_24h": {
                      "type": "string",
                      "description": "The average hashrate over the past 24 hours. *Note: This integer is returned as a string to use with BigInt libraries as it may exceed the max safe integer size for many programming languages.*",
                      "example": "169267882822616"
                    },
                    "pending_transactions": {
                      "type": "integer",
                      "description": "The number of pending transactions.",
                      "example": 5120
                    },
                    "reduction_rate": {
                      "type": "string",
                      "description": "The rate the block reward is adjusted at a specified interval.",
                      "example": "50%"
                    },
                    "total_blocks": {
                      "type": "integer",
                      "description": "The total number of blocks.",
                      "example": 8385036
                    },
                    "total_transactions": {
                      "type": "string",
                      "description": "The total number of transactions. *Note: This integer is returned as a string to use with BigInt libraries as it may exceed the max safe integer size for many programming languages.*",
                      "example": "523059480"
                    },
                    "tps_24h": {
                      "type": "number",
                      "description": "The average transactions per second over the past 24 hours.",
                      "example": 8.463935185185186
                    },
                    "first_block_timestamp": {
                      "type": "string",
                      "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                      "description": "Timestamp (ISO 8601) of the time the first block was mined on this chain.",
                      "example": "2009-01-09T02:54:25.000Z"
                    }
                  },
                  "required": [
                    "id",
                    "slug",
                    "symbol",
                    "block_reward_static",
                    "consensus_mechanism",
                    "difficulty",
                    "hashrate_24h",
                    "pending_transactions",
                    "reduction_rate",
                    "total_blocks",
                    "total_transactions",
                    "tps_24h",
                    "first_block_timestamp"
                  ],
                  "__$ref": "#/components/schemas/Blockchain_Statistics_Latest_-_Blockchain_object"
                },
                "__$ref": "#/components/schemas/Blockchain_Statistics_Latest_-_Results_map"
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
            "__$ref": "#/components/schemas/Blockchain_Statistics_Latest_-_Response_Model"
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
