# GET /v1/exchange/assets

**Summary:** Exchange Assets

**Description:** Returns the exchange assets in the form of token holdings. This information includes details like wallet address, cryptocurrency, blockchain platform, balance, and etc.


  * Only wallets containing at least 100,000 USD in balance are shown
  * Balances from wallets might be delayed
  
  ** Disclaimer:
  All information and data relating to the holdings in the third-party wallet addresses are provided by the third parties to CoinMarketCap, and CoinMarketCap does not confirm or verify the accuracy or timeliness of such information and data.
  The information and data are provided "as is" without warranty of any kind. CoinMarketCap shall have no responsibility or liability for these third parties’ information and data or have the duty to review, confirm, verify or otherwise perform any inquiry or investigation as to the completeness, accuracy, sufficiency, integrity, reliability or timeliness of any such information or data provided.
    
  **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
  - Free
  - Hobbyist
  - Startup
  - Standard
  - Professional
  - Enterprise
  
  **Cache / Update frequency:** Balance data is updated statically based on the source. Price data is updated every 5 minutes.  
  **Plan credit use:** 1 credit.  
  **CMC equivalent pages:** Exchange detail page like [coinmarketcap.com/exchanges/binance/](https://coinmarketcap.com/exchanges/binance/)

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **id** (query) - *Optional*: A CoinMarketCap exchange ID. Example: 270

### Raw Data

```json
{
  "slug": "exchange-assets",
  "summary": "Exchange Assets",
  "method": "get",
  "description": "Returns the exchange assets in the form of token holdings. This information includes details like wallet address, cryptocurrency, blockchain platform, balance, and etc.\n\n\n  * Only wallets containing at least 100,000 USD in balance are shown\n  * Balances from wallets might be delayed\n  \n  ** Disclaimer:\n  All information and data relating to the holdings in the third-party wallet addresses are provided by the third parties to CoinMarketCap, and CoinMarketCap does not confirm or verify the accuracy or timeliness of such information and data.\n  The information and data are provided \"as is\" without warranty of any kind. CoinMarketCap shall have no responsibility or liability for these third parties\u2019 information and data or have the duty to review, confirm, verify or otherwise perform any inquiry or investigation as to the completeness, accuracy, sufficiency, integrity, reliability or timeliness of any such information or data provided.\n    \n  **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**\n  - Free\n  - Hobbyist\n  - Startup\n  - Standard\n  - Professional\n  - Enterprise\n  \n  **Cache / Update frequency:** Balance data is updated statically based on the source. Price data is updated every 5 minutes.  \n  **Plan credit use:** 1 credit.  \n  **CMC equivalent pages:** Exchange detail page like [coinmarketcap.com/exchanges/binance/](https://coinmarketcap.com/exchanges/binance/)",
  "operationId": "getV1ExchangeAssets",
  "contentTypes": [],
  "path": "/v1/exchange/assets",
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
      "description": "A CoinMarketCap exchange ID. Example: 270",
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
            "example": {
              "status": {
                "timestamp": "2022-11-24T08:23:22.028Z",
                "error_code": 0,
                "error_message": null,
                "elapsed": 1828,
                "credit_count": 0,
                "notice": null
              },
              "data": [
                {
                  "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                  "balance": 45000000,
                  "platform": {
                    "crypto_id": 1027,
                    "symbol": "ETH",
                    "name": "Ethereum"
                  },
                  "currency": {
                    "crypto_id": 5117,
                    "price_usd": 0.10241799413549,
                    "symbol": "OGN",
                    "name": "Origin Protocol"
                  }
                },
                {
                  "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                  "balance": 400000000,
                  "platform": {
                    "crypto_id": 1027,
                    "symbol": "ETH",
                    "name": "Ethereum"
                  },
                  "currency": {
                    "crypto_id": 5824,
                    "price_usd": 0.00251174724338,
                    "symbol": "SLP",
                    "name": "Smooth Love Potion"
                  }
                },
                {
                  "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                  "balance": 5588175,
                  "platform": {
                    "crypto_id": 1027,
                    "symbol": "ETH",
                    "name": "Ethereum"
                  },
                  "currency": {
                    "crypto_id": 3928,
                    "price_usd": 0.04813245442357,
                    "symbol": "IDEX",
                    "name": "IDEX"
                  }
                },
                {
                  "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                  "balance": 125000,
                  "platform": {
                    "crypto_id": 1027,
                    "symbol": "ETH",
                    "name": "Ethereum"
                  },
                  "currency": {
                    "crypto_id": 1552,
                    "price_usd": 20.46545919550142,
                    "symbol": "MLN",
                    "name": "Enzyme"
                  }
                },
                {
                  "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                  "balance": 27241191.98,
                  "platform": {
                    "crypto_id": 1027,
                    "symbol": "ETH",
                    "name": "Ethereum"
                  },
                  "currency": {
                    "crypto_id": 14806,
                    "price_usd": 0.02390427295165,
                    "symbol": "PEOPLE",
                    "name": "ConstitutionDAO"
                  }
                }
              ]
            },
            "properties": {
              "data": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "wallet_address": {
                      "type": "string",
                      "description": "The address of the wallet",
                      "example": "0x5a52e96bacdabb82fd05763e25335261b270efcb"
                    },
                    "balance": {
                      "type": "number",
                      "description": "The amount of coins/tokens held in this wallet",
                      "example": 1000
                    },
                    "platform": {
                      "type": "object",
                      "properties": {
                        "crypto_id": {
                          "type": "integer",
                          "description": "The CoinMarketCap ID for the blockchain platform where the assets are held on",
                          "example": 1027
                        },
                        "symbol": {
                          "type": "string",
                          "description": "The symbol for the blockchain platform where the assets are held on",
                          "example": "ETH"
                        },
                        "name": {
                          "type": "string",
                          "description": "The name for the blockchain platform where the assets are held on",
                          "example": "Ethereum"
                        }
                      },
                      "__$ref": "#/components/schemas/The_blockchain_platform_where_the_assets_are_held_on."
                    },
                    "currency": {
                      "type": "object",
                      "properties": {
                        "crypto_id": {
                          "type": "integer",
                          "description": "The CoinMarketCap ID for the coin/token used for this wallet",
                          "example": 1027
                        },
                        "symbol": {
                          "type": "string",
                          "description": "The symbol for the coin/token used for this wallet",
                          "example": "ETH"
                        },
                        "name": {
                          "type": "string",
                          "description": "The name for the coin/token used for this wallet",
                          "example": "Ethereum"
                        },
                        "price_usd": {
                          "type": "number",
                          "description": "The price in USD for 1 coin/token",
                          "example": 1200.055
                        }
                      },
                      "__$ref": "#/components/schemas/The_cryptocurrency_of_the_holdings_in_the_wallet."
                    }
                  },
                  "required": [
                    "wallet_address",
                    "balance",
                    "platform",
                    "currency"
                  ],
                  "__$ref": "#/components/schemas/Exchange_Assets_Wallets_-_Response_Model"
                },
                "required": [
                  "Exchange Assets Wallets - Response Model"
                ],
                "__$ref": "#/components/schemas/data"
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
            "__$ref": "#/components/schemas/Exchange_Assets_-_Response_Model"
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
