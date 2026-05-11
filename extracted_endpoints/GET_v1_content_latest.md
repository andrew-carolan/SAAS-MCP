# GET /v1/content/latest

**Summary:** Content Latest

**Description:** Returns a paginated list of content pulled from CMC News/Headlines and Alexandria articles.

  
  **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
  - Standard
  - Professional
  - Enterprise

**Cache / Update frequency:** Five Minutes
**Plan credit use:** 0 credit

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **start** (query) - *Optional*: Optionally offset the start (1-based index) of the paginated list of items to return.
- **limit** (query) - *Optional*: Optionally specify the number of results to return. Use this parameter and the "start" parameter to determine your own pagination size.
- **id** (query) - *Optional*: Optionally pass a comma-separated list of CoinMarketCap cryptocurrency IDs. Example: "1,1027"
- **slug** (query) - *Optional*: Optionally pass a comma-separated list of cryptocurrency slugs. Example: "bitcoin,ethereum"
- **symbol** (query) - *Optional*: Optionally pass a comma-separated list of cryptocurrency symbols. Example: "BTC,ETH". Optionally pass "id" *or* "slug" *or* "symbol" is required for this request.
- **news_type** (query) - *Optional*: Optionally specify a comma-separated list of supplemental data fields: `news`, `community`, or `alexandria` to filter news sources. Pass `all` or leave it blank to include all news types.
- **content_type** (query) - *Optional*: Optionally specify a comma-separated list of supplemental data fields: `news`, `video`, or `audio` to filter news's content. Pass `all` or leave it blank to include all content types.
- **category** (query) - *Optional*: Optionally pass a comma-separated list of categories. Example: "GameFi,NFT".
- **language** (query) - *Optional*: Optionally pass a language code. Example: "en". If not specified the default value is "en".

### Raw Data

```json
{
  "slug": "content-latest",
  "summary": "Content Latest",
  "method": "get",
  "description": "Returns a paginated list of content pulled from CMC News/Headlines and Alexandria articles.\n\n  \n  **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**\n  - Standard\n  - Professional\n  - Enterprise\n\n**Cache / Update frequency:** Five Minutes\n**Plan credit use:** 0 credit",
  "operationId": "getV1ContentLatest",
  "contentTypes": [],
  "path": "/v1/content/latest",
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
        "maximum": 200,
        "default": 100
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "id",
      "in": "query",
      "description": "Optionally pass a comma-separated list of CoinMarketCap cryptocurrency IDs. Example: \"1,1027\"",
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
      "description": "Optionally pass a comma-separated list of cryptocurrency slugs. Example: \"bitcoin,ethereum\"",
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
      "description": "Optionally pass a comma-separated list of cryptocurrency symbols. Example: \"BTC,ETH\". Optionally pass \"id\" *or* \"slug\" *or* \"symbol\" is required for this request.",
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
      "name": "news_type",
      "in": "query",
      "description": "Optionally specify a comma-separated list of supplemental data fields: `news`, `community`, or `alexandria` to filter news sources. Pass `all` or leave it blank to include all news types.",
      "required": null,
      "schema": {
        "type": "string",
        "pattern": "^(news|community|alexandria|all)+(?:,(news|community|alexandria|all)+)*$",
        "default": "all"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "content_type",
      "in": "query",
      "description": "Optionally specify a comma-separated list of supplemental data fields: `news`, `video`, or `audio` to filter news's content. Pass `all` or leave it blank to include all content types.",
      "required": null,
      "schema": {
        "type": "string",
        "pattern": "^(audio|news|video|all)+(?:,(audio|news|video|all)+)*$",
        "default": "all"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "category",
      "in": "query",
      "description": "Optionally pass a comma-separated list of categories. Example: \"GameFi,NFT\".",
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
      "name": "language",
      "in": "query",
      "description": "Optionally pass a language code. Example: \"en\". If not specified the default value is \"en\".",
      "required": null,
      "schema": {
        "type": "string",
        "enum": [
          "en",
          "zh",
          "zh-tw",
          "de",
          "id",
          "ja",
          "ko",
          "es",
          "th",
          "tr",
          "vi",
          "ru",
          "fr",
          "nl",
          "ar",
          "pt-br",
          "hi",
          "pl",
          "uk",
          "fil-rph",
          "it"
        ],
        "default": "en"
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
                  "cover": "https://academy-public.coinmarketcap.com/optimized-uploads/0aec0502868046419ceace229f92601f.gif",
                  "assets": [
                    {
                      "id": 1027,
                      "name": "Ethereum",
                      "symbol": "ETH",
                      "slug": "ethereum"
                    }
                  ],
                  "created_at": "2021-05-05T00:00:00Z",
                  "released_at": "2021-05-05T00:00:00Z",
                  "title": "Article Title",
                  "subtitle": "Article Subtitle",
                  "type": "alexandria",
                  "source_name": "Connor Sephton",
                  "source_url": "https://coinmarketcap.com/alexandria/article/coinmarketcap-news-august-9-u-s-comes-for-tornado-cash"
                }
              ],
              "status": {
                "timestamp": "2018-06-02T22:51:28.209Z",
                "error_code": 0,
                "error_message": "",
                "elapsed": 10,
                "credit_count": 1
              }
            },
            "properties": {
              "data": {
                "type": "array",
                "description": "Array of content objects.",
                "items": {
                  "type": "object",
                  "properties": {
                    "cover": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "subtitle": {
                      "type": "string"
                    },
                    "source_name": {
                      "type": "string"
                    },
                    "source_url": {
                      "type": "string"
                    },
                    "type": {
                      "type": "string"
                    },
                    "assets": {
                      "type": "array",
                      "items": {
                        "type": "object",
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
                          }
                        },
                        "required": [
                          "id",
                          "name",
                          "symbol",
                          "slug"
                        ],
                        "__$ref": "#/components/schemas/assets"
                      },
                      "__$ref": "#/components/schemas/assets_array"
                    },
                    "created_at": {
                      "type": "string",
                      "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                      "description": "Timestamp (ISO 8601) of the time this was created.",
                      "example": "2018-06-02T23:59:59.999Z"
                    },
                    "released_at": {
                      "type": "string",
                      "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                      "description": "Timestamp (ISO 8601) of the time this was released.",
                      "example": "2018-06-02T23:59:59.999Z"
                    }
                  },
                  "__$ref": "#/components/schemas/Model_1"
                },
                "__$ref": "#/components/schemas/Content_Latest_-_Results_array"
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
              "data",
              "status"
            ],
            "__$ref": "#/components/schemas/Content_Latest_-_Response_Model"
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
