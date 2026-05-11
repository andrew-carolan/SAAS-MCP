# GET /v1/content/posts/latest

**Summary:** Content Latest Posts

**Description:** Returns the latest crypto-related posts from the CMC Community.

  
  **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
  - Standard
  - Professional
  - Enterprise

**Cache / Update frequency:** Five Minutes
**Plan credit use:** 0 credit

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **id** (query) - *Optional*: Optional one cryptocurrency CoinMarketCap ID. Example: 1027
- **slug** (query) - *Optional*: Alternatively pass one cryptocurrency slug. Example: "ethereum"
- **symbol** (query) - *Optional*: Alternatively pass one cryptocurrency symbols. Example: "ETH"
- **last_score** (query) - *Optional*: Optional. The score is given in the response for finding next batch posts. Example: 1662903634322

### Raw Data

```json
{
  "slug": "content-latest-posts",
  "summary": "Content Latest Posts",
  "method": "get",
  "description": "Returns the latest crypto-related posts from the CMC Community.\n\n  \n  **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**\n  - Standard\n  - Professional\n  - Enterprise\n\n**Cache / Update frequency:** Five Minutes\n**Plan credit use:** 0 credit",
  "operationId": "getV1ContentPostsLatest",
  "contentTypes": [],
  "path": "/v1/content/posts/latest",
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
      "description": "Optional one cryptocurrency CoinMarketCap ID. Example: 1027",
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
      "name": "slug",
      "in": "query",
      "description": "Alternatively pass one cryptocurrency slug. Example: \"ethereum\"",
      "required": null,
      "schema": {
        "type": "string",
        "pattern": "^[0-9a-z-]*$"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "symbol",
      "in": "query",
      "description": "Alternatively pass one cryptocurrency symbols. Example: \"ETH\"",
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
      "name": "last_score",
      "in": "query",
      "description": "Optional. The score is given in the response for finding next batch posts. Example: 1662903634322",
      "required": null,
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
            "example": {
              "data": {
                "list": [
                  {
                    "post_id": "123456789",
                    "comments_url": "{{baseUrl}}/v1/content/posts/comments?post_id=123456789",
                    "owner": {
                      "nickname": "CoinMarketCap",
                      "avatar_url": "https://s3.coinmarketcap.com/static/img/portraits/621c22097aafe46422aa1161.png"
                    },
                    "text_content": "$ETH regardless of merging or not merging...",
                    "photos": [
                      "https://s3.coinmarketcap.com/static/img/portraits/621c22097aafe46422aa1161.png"
                    ],
                    "comment_count": "5",
                    "like_count": "5",
                    "post_time": "1662643031298",
                    "currencies": [
                      {
                        "id": 1027,
                        "symbol": "ETH",
                        "slug": "ethereum"
                      }
                    ],
                    "language_code": "en"
                  },
                  {
                    "post_id": "123456790",
                    "comments_url": "{{baseUrl}}/v1/content/posts/comments?post_id=123456790",
                    "owner": {
                      "nickname": "John",
                      "avatar_url": "https://s3.coinmarketcap.com/static/img/portraits/61b9aaca1d79d0637758fdeb.png"
                    },
                    "text_content": "$ETH The success and the failure are almost...",
                    "photos": [
                      "https://s3.coinmarketcap.com/static/img/portraits/621c22097aafe46422aa1161.png"
                    ],
                    "comment_count": "6",
                    "like_count": "60",
                    "post_time": "1662612816768",
                    "currencies": [
                      {
                        "id": 1027,
                        "symbol": "ETH",
                        "slug": "ethereum"
                      }
                    ],
                    "repost_count": "0",
                    "language_code": "en"
                  }
                ],
                "last_score": "1662903634322"
              }
            },
            "properties": {
              "data": {
                "type": "object",
                "description": "Cntent objects.",
                "properties": {
                  "list": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "post_id": {
                          "type": "string"
                        },
                        "owner": {
                          "type": "object",
                          "properties": {
                            "nickname": {
                              "type": "string"
                            },
                            "avatar_url": {
                              "type": "string"
                            }
                          },
                          "__$ref": "#/components/schemas/owner"
                        },
                        "text_content": {
                          "type": "string"
                        },
                        "photos": {
                          "type": "array",
                          "items": {
                            "type": "string"
                          },
                          "__$ref": "#/components/schemas/photos"
                        },
                        "comment_count": {
                          "type": "string"
                        },
                        "like_count": {
                          "type": "string"
                        },
                        "post_time": {
                          "type": "string"
                        },
                        "currencies": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "number"
                              },
                              "symbol": {
                                "type": "string"
                              },
                              "slug": {
                                "type": "string"
                              }
                            },
                            "__$ref": "#/components/schemas/Model_3"
                          },
                          "__$ref": "#/components/schemas/currencies"
                        },
                        "language_code": {
                          "type": "string"
                        },
                        "comments_url": {
                          "type": "string",
                          "description": "Returns comments of the current post/comment"
                        }
                      },
                      "required": [
                        "owner"
                      ],
                      "__$ref": "#/components/schemas/Model_4"
                    },
                    "__$ref": "#/components/schemas/list"
                  },
                  "last_score": {
                    "type": "string"
                  }
                },
                "__$ref": "#/components/schemas/Content_Top_Posts_-_Results"
              }
            },
            "required": [
              "data"
            ],
            "__$ref": "#/components/schemas/Content_Latest_Posts_-_Response_Model"
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
