# GET /v1/exchange/info

**Summary:** Metadata

**Description:** Returns all static metadata for one or more exchanges. This information includes details like launch date, logo, official website URL, social links, and market fee documentation URL.

  **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
  - Basic
  - Hobbyist
  - Startup
  - Standard
  - Professional
  - Enterprise

**Cache / Update frequency:** Static data is updated only as needed, every 30 seconds.  
**Plan credit use:** 1 call credit per 100 exchanges returned (rounded up).  
**CMC equivalent pages:** Exchange detail page metadata like [coinmarketcap.com/exchanges/binance/](https://coinmarketcap.com/exchanges/binance/).  

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **id** (query) - *Optional*: One or more comma-separated CoinMarketCap cryptocurrency exchange ids. Example: "1,2"
- **slug** (query) - *Optional*: Alternatively, one or more comma-separated exchange names in URL friendly shorthand "slug" format (all lowercase, spaces replaced with hyphens). Example: "binance,gdax". At least one "id" *or* "slug" is required.
- **aux** (query) - *Optional*: Optionally specify a comma-separated list of supplemental data fields to return. Pass `urls,logo,description,date_launched,notice,status` to include all auxiliary fields.

### Raw Data

```json
{
  "slug": "metadata",
  "summary": "Metadata",
  "method": "get",
  "description": "Returns all static metadata for one or more exchanges. This information includes details like launch date, logo, official website URL, social links, and market fee documentation URL.\n\n  **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**\n  - Basic\n  - Hobbyist\n  - Startup\n  - Standard\n  - Professional\n  - Enterprise\n\n**Cache / Update frequency:** Static data is updated only as needed, every 30 seconds.  \n**Plan credit use:** 1 call credit per 100 exchanges returned (rounded up).  \n**CMC equivalent pages:** Exchange detail page metadata like [coinmarketcap.com/exchanges/binance/](https://coinmarketcap.com/exchanges/binance/).  ",
  "operationId": "getV1ExchangeInfo",
  "contentTypes": [],
  "path": "/v1/exchange/info",
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
      "description": "One or more comma-separated CoinMarketCap cryptocurrency exchange ids. Example: \"1,2\"",
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
      "description": "Alternatively, one or more comma-separated exchange names in URL friendly shorthand \"slug\" format (all lowercase, spaces replaced with hyphens). Example: \"binance,gdax\". At least one \"id\" *or* \"slug\" is required.",
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
      "name": "aux",
      "in": "query",
      "description": "Optionally specify a comma-separated list of supplemental data fields to return. Pass `urls,logo,description,date_launched,notice,status` to include all auxiliary fields.",
      "required": null,
      "schema": {
        "type": "string",
        "pattern": "^(urls|logo|description|date_launched|notice|status)+(?:,(urls|logo|description|date_launched|notice|status)+)*$",
        "default": "urls,logo,description,date_launched,notice"
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
                    "id": 270,
                    "name": "Binance",
                    "slug": "binance",
                    "logo": "https://s2.coinmarketcap.com/static/img/exchanges/64x64/270.png",
                    "description": "Launched in Jul-2017, Binance is a centralized exchange based in Malta.",
                    "date_launched": "2017-07-14T00:00:00.000Z",
                    "notice": "",
                    "countries": [],
                    "fiats": [
                      "AED",
                      "USD"
                    ],
                    "tags": null,
                    "type": "",
                    "maker_fee": 0.02,
                    "taker_fee": 0.04,
                    "weekly_visits": 5123451,
                    "spot_volume_usd": 66926283498.60113,
                    "spot_volume_last_updated": "2021-05-06T01:20:15.451Z",
                    "urls": {
                      "website": [
                        "https://www.binance.com/"
                      ],
                      "twitter": [
                        "https://twitter.com/binance"
                      ],
                      "blog": [],
                      "chat": [
                        "https://t.me/binanceexchange"
                      ],
                      "fee": [
                        "https://www.binance.com/fees.html"
                      ]
                    }
                  }
                },
                "additionalProperties": {
                  "type": "object",
                  "description": "A results object for each exchange requested. The map key being the id or slug used in the request.",
                  "properties": {
                    "id": {
                      "type": "integer",
                      "description": "The unique CoinMarketCap ID for this exchange.",
                      "example": 1
                    },
                    "name": {
                      "type": "string",
                      "description": "The name of this exchange.",
                      "example": "Binance"
                    },
                    "slug": {
                      "type": "string",
                      "description": "The web URL friendly shorthand version of the exchange name.",
                      "example": "binance"
                    },
                    "logo": {
                      "type": "string",
                      "description": "Link to a CoinMarketCap hosted logo png for this exchange. 64px is default size returned. Replace \"64x64\" in the image path with these alternative sizes: 16, 32, 64, 128, 200",
                      "example": "https://s2.coinmarketcap.com/static/img/exchanges/64x64/270.png",
                      "x-format": {
                        "uri": true
                      }
                    },
                    "description": {
                      "type": "string",
                      "description": "A CoinMarketCap supplied brief description of this cryptocurrency exchange. This field will return null if a description is not available.",
                      "example": "Launched in Jul-2017, Binance is a centralized exchange based in Malta."
                    },
                    "date_launched": {
                      "type": "string",
                      "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                      "description": "Timestamp (ISO 8601) of the launch date for this exchange.",
                      "example": "2017-07-14T00:00:00.000Z"
                    },
                    "notice": {
                      "type": "string",
                      "description": "A [Markdown](https://commonmark.org/help/) formatted message outlining a condition that is impacting the availability of the exchange's market data or the secure use of the exchange, otherwise null. This may include a maintenance event on the exchange's end or CoinMarketCap's end, an alert about reported issues with withdrawls from this exchange, or another condition that may be impacting the exchange and it's markets. If present, this notice is also displayed in an alert banner at the top of the exchange's page on coinmarketcap.com."
                    },
                    "weekly_visits": {
                      "type": "number",
                      "description": "The number of weekly visitors.",
                      "example": 1000
                    },
                    "spot_volume_usd": {
                      "type": "number",
                      "description": "Reported all time spot volume in the specified currency.",
                      "example": 768478308.529847
                    },
                    "urls": {
                      "type": "object",
                      "description": "An object containing various resource URLs for this exchange.",
                      "properties": {
                        "website": {
                          "type": "array",
                          "description": "Official website URLs.",
                          "example": [
                            "https://binance.com"
                          ],
                          "items": {
                            "type": "string",
                            "x-format": {
                              "uri": true
                            }
                          },
                          "__$ref": "#/components/schemas/website_1"
                        },
                        "blog": {
                          "type": "array",
                          "description": "Official blog URLs.",
                          "example": [
                            "https://blog.kraken.com/"
                          ],
                          "items": {
                            "type": "string",
                            "x-format": {
                              "uri": true
                            }
                          },
                          "__$ref": "#/components/schemas/blog"
                        },
                        "chat": {
                          "type": "array",
                          "description": "Official chat URLs.",
                          "example": [
                            "https://t.me/coinbene"
                          ],
                          "items": {
                            "type": "string",
                            "x-format": {
                              "uri": true
                            }
                          },
                          "__$ref": "#/components/schemas/chat_1"
                        },
                        "fee": {
                          "type": "array",
                          "description": "Official web URLs covering exchange fees.",
                          "example": [
                            "https://www.gdax.com/fees"
                          ],
                          "items": {
                            "type": "string",
                            "x-format": {
                              "uri": true
                            }
                          },
                          "__$ref": "#/components/schemas/fee"
                        },
                        "twitter": {
                          "type": "array",
                          "description": "Official twitter profile URLs.",
                          "example": [
                            "https://twitter.com/Bitcoin"
                          ],
                          "items": {
                            "type": "string",
                            "x-format": {
                              "uri": true
                            }
                          },
                          "__$ref": "#/components/schemas/twitter_1"
                        }
                      },
                      "required": [
                        "website",
                        "blog",
                        "chat",
                        "fee",
                        "twitter"
                      ],
                      "__$ref": "#/components/schemas/Exchanges_Info_-_URLs_object"
                    }
                  },
                  "required": [
                    "id",
                    "name",
                    "slug",
                    "logo",
                    "description",
                    "date_launched",
                    "notice",
                    "urls"
                  ],
                  "__$ref": "#/components/schemas/Exchanges_Info_-_Exchange_Info_object"
                },
                "__$ref": "#/components/schemas/Exchanges_Info_-_Results_map"
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
            "__$ref": "#/components/schemas/Exchanges_Info_-_Response_Model"
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
