# GET /v1/cryptocurrency/info

**Summary:** Metadata v1 (deprecated)

**Description:** Returns all static metadata available for one or more cryptocurrencies. This information includes details like logo, description, official website URL, social links, and links to a cryptocurrency's technical documentation.


**This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
- Basic
- Startup
- Hobbyist
- Standard
- Professional
- Enterprise

**Cache / Update frequency:** Static data is updated only as needed, every 30 seconds.  
**Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up).  
**CMC equivalent pages:** Cryptocurrency detail page metadata like [coinmarketcap.com/currencies/bitcoin/](https://coinmarketcap.com/currencies/bitcoin/).  

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **id** (query) - *Optional*: One or more comma-separated CoinMarketCap cryptocurrency IDs. Example: "1,2"
- **slug** (query) - *Optional*: Alternatively pass a comma-separated list of cryptocurrency slugs. Example: "bitcoin,ethereum"
- **symbol** (query) - *Optional*: Alternatively pass one or more comma-separated cryptocurrency symbols. Example: "BTC,ETH". At least one "id" *or* "slug" *or* "symbol" is required for this request. Please note that starting in the v2 endpoint, due to the fact that a symbol is not unique, if you request by symbol each data response will contain an array of objects containing all of the coins that use each requested symbol. The v1 endpoint will still return a single object, the highest ranked coin using that symbol.
- **address** (query) - *Optional*: Alternatively pass in a contract address. Example: "0xc40af1e4fecfa05ce6bab79dcd8b373d2e436c4e"
- **skip_invalid** (query) - *Optional*: Pass `true` to relax request validation rules. When requesting records on multiple cryptocurrencies an error is returned if any invalid cryptocurrencies are requested or a cryptocurrency does not have matching records in the requested timeframe. If set to true, invalid lookups will be skipped allowing valid cryptocurrencies to still be returned.
- **aux** (query) - *Optional*: Optionally specify a comma-separated list of supplemental data fields to return. Pass `urls,logo,description,tags,platform,date_added,notice,status` to include all auxiliary fields.

### Raw Data

```json
{
  "slug": "metadata-v1-deprecated",
  "summary": "Metadata v1 (deprecated)",
  "method": "get",
  "description": "Returns all static metadata available for one or more cryptocurrencies. This information includes details like logo, description, official website URL, social links, and links to a cryptocurrency's technical documentation.\n\n\n**This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**\n- Basic\n- Startup\n- Hobbyist\n- Standard\n- Professional\n- Enterprise\n\n**Cache / Update frequency:** Static data is updated only as needed, every 30 seconds.  \n**Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up).  \n**CMC equivalent pages:** Cryptocurrency detail page metadata like [coinmarketcap.com/currencies/bitcoin/](https://coinmarketcap.com/currencies/bitcoin/).  ",
  "operationId": "getV1CryptocurrencyInfo",
  "contentTypes": [],
  "path": "/v1/cryptocurrency/info",
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
      "description": "One or more comma-separated CoinMarketCap cryptocurrency IDs. Example: \"1,2\"",
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
      "description": "Alternatively pass one or more comma-separated cryptocurrency symbols. Example: \"BTC,ETH\". At least one \"id\" *or* \"slug\" *or* \"symbol\" is required for this request. Please note that starting in the v2 endpoint, due to the fact that a symbol is not unique, if you request by symbol each data response will contain an array of objects containing all of the coins that use each requested symbol. The v1 endpoint will still return a single object, the highest ranked coin using that symbol.",
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
      "name": "address",
      "in": "query",
      "description": "Alternatively pass in a contract address. Example: \"0xc40af1e4fecfa05ce6bab79dcd8b373d2e436c4e\"",
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
      "name": "skip_invalid",
      "in": "query",
      "description": "Pass `true` to relax request validation rules. When requesting records on multiple cryptocurrencies an error is returned if any invalid cryptocurrencies are requested or a cryptocurrency does not have matching records in the requested timeframe. If set to true, invalid lookups will be skipped allowing valid cryptocurrencies to still be returned.",
      "required": null,
      "schema": {
        "type": "boolean",
        "default": false
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "aux",
      "in": "query",
      "description": "Optionally specify a comma-separated list of supplemental data fields to return. Pass `urls,logo,description,tags,platform,date_added,notice,status` to include all auxiliary fields.",
      "required": null,
      "schema": {
        "type": "string",
        "pattern": "^(urls|logo|description|tags|platform|date_added|notice|status)+(?:,(urls|logo|description|tags|platform|date_added|notice|status)+)*$",
        "default": "urls,logo,description,tags,platform,date_added,notice"
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
                    "urls": {
                      "website": [
                        "https://bitcoin.org/"
                      ],
                      "technical_doc": [
                        "https://bitcoin.org/bitcoin.pdf"
                      ],
                      "twitter": [],
                      "reddit": [
                        "https://reddit.com/r/bitcoin"
                      ],
                      "message_board": [
                        "https://bitcointalk.org"
                      ],
                      "announcement": [],
                      "chat": [],
                      "explorer": [
                        "https://blockchain.coinmarketcap.com/chain/bitcoin",
                        "https://blockchain.info/",
                        "https://live.blockcypher.com/btc/"
                      ],
                      "source_code": [
                        "https://github.com/bitcoin/"
                      ]
                    },
                    "logo": "https://s2.coinmarketcap.com/static/img/coins/64x64/1.png",
                    "id": 1,
                    "name": "Bitcoin",
                    "symbol": "BTC",
                    "slug": "bitcoin",
                    "description": "Bitcoin (BTC) is a consensus network that enables a new payment system and a completely digital currency. Powered by its users, it is a peer to peer payment network that requires no central authority to operate. On October 31st, 2008, an individual or group of individuals operating under the pseudonym \"Satoshi Nakamoto\" published the Bitcoin Whitepaper and described it as: \"a purely peer-to-peer version of electronic cash would allow online payments to be sent directly from one party to another without going through a financial institution.\"",
                    "date_added": "2013-04-28T00:00:00.000Z",
                    "date_launched": "2013-04-28T00:00:00.000Z",
                    "tags": [
                      "mineable"
                    ],
                    "platform": null,
                    "category": "coin"
                  }
                },
                "additionalProperties": {
                  "type": "object",
                  "description": "A results object for each cryptocurrency requested. The map key being the id/symbol used in the request.",
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
                    "category": {
                      "type": "string",
                      "description": "The category for this cryptocurrency.",
                      "example": "coin",
                      "enum": [
                        "coin",
                        "token"
                      ]
                    },
                    "slug": {
                      "type": "string",
                      "description": "The web URL friendly shorthand version of this cryptocurrency name.",
                      "example": "bitcoin"
                    },
                    "logo": {
                      "type": "string",
                      "description": "Link to a CoinMarketCap hosted logo png for this cryptocurrency. 64px is default size returned. Replace \"64x64\" in the image path with these alternative sizes: 16, 32, 64, 128, 200",
                      "example": "https://s2.coinmarketcap.com/static/img/coins/64x64/1.png"
                    },
                    "description": {
                      "type": "string",
                      "description": "A CoinMarketCap supplied brief description of this cryptocurrency. This field will return null if a description is not available.",
                      "example": "Bitcoin (BTC) is a consensus network that enables a new payment system and a completely digital currency. Powered by its users, it is a peer to peer payment network that requires no central authority to operate."
                    },
                    "date_added": {
                      "type": "string",
                      "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                      "description": "Timestamp (ISO 8601) of when this cryptocurrency was added to CoinMarketCap.",
                      "example": "2013-04-28T00:00:00.000Z"
                    },
                    "date_launched": {
                      "type": "string",
                      "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                      "description": "Timestamp (ISO 8601) of when this cryptocurrency was launched.",
                      "example": "2013-04-28T00:00:00.000Z"
                    },
                    "notice": {
                      "type": "string",
                      "description": "A [Markdown](https://commonmark.org/help/) formatted notice that may highlight a significant event or condition that is impacting the cryptocurrency or how it is displayed, otherwise null. A notice may highlight a recent or upcoming mainnet swap, symbol change, exploit event, or known issue with a particular exchange or market, for example. If present, this notice is also displayed in an alert banner at the top of the cryptocurrency's page on coinmarketcap.com."
                    },
                    "tags": {
                      "type": "array",
                      "description": "Tags associated with this cryptocurrency.",
                      "example": [
                        "mineable"
                      ],
                      "items": {
                        "type": "string"
                      },
                      "__$ref": "#/components/schemas/tags_1"
                    },
                    "platform": {
                      "type": [
                        "object",
                        "null"
                      ],
                      "description": "Metadata about the parent cryptocurrency platform this cryptocurrency belongs to if it is a token, otherwise null.",
                      "properties": {
                        "id": {
                          "type": "integer",
                          "description": "The unique CoinMarketCap ID for the parent platform cryptocurrency.",
                          "example": 1
                        },
                        "name": {
                          "type": "string",
                          "description": "The name of the parent platform cryptocurrency.",
                          "example": "Ethereum"
                        },
                        "symbol": {
                          "type": "string",
                          "description": "The ticker symbol for the parent platform cryptocurrency.",
                          "example": "ETH"
                        },
                        "slug": {
                          "type": "string",
                          "description": "The web URL friendly shorthand version of the parent platform cryptocurrency name.",
                          "example": "ethereum"
                        },
                        "token_address": {
                          "type": "string",
                          "description": "The token address on the parent platform cryptocurrency.",
                          "example": "0xe41d2489571d322189246dafa5ebde1f4699f498"
                        }
                      },
                      "required": [
                        "id",
                        "name",
                        "symbol",
                        "slug",
                        "token_address"
                      ],
                      "__$ref": "#/components/schemas/platform"
                    },
                    "self_reported_circulating_supply": {
                      "type": [
                        "number",
                        "null"
                      ],
                      "description": "The self reported number of coins circulating for this cryptocurrency.",
                      "example": 16950100
                    },
                    "self_reported_market_cap": {
                      "type": [
                        "number",
                        "null"
                      ],
                      "description": "The self reported market cap for this cryptocurrency.",
                      "example": 16950100
                    },
                    "self_reported_tags": {
                      "type": "array",
                      "description": "Array of self reported tags associated with this cryptocurrency.",
                      "example": [
                        "Store Of Value",
                        "Play To Earn"
                      ],
                      "items": {
                        "type": "string"
                      },
                      "__$ref": "#/components/schemas/self_reported_tags"
                    },
                    "infinite_supply": {
                      "type": "boolean",
                      "description": "The cryptocurrency is known to have an infinite supply.",
                      "example": false
                    },
                    "urls": {
                      "type": "object",
                      "description": "An object containing various resource URLs for this cryptocurrency.",
                      "properties": {
                        "website": {
                          "type": "array",
                          "description": "Array of website URLs.",
                          "example": [
                            "https://bitcoin.org/"
                          ],
                          "items": {
                            "type": "string",
                            "x-format": {
                              "uri": true
                            }
                          },
                          "__$ref": "#/components/schemas/website"
                        },
                        "technical_doc": {
                          "type": "array",
                          "description": "Array of white paper or technical documentation URLs.",
                          "example": [
                            "https://bitcoin.org/bitcoin.pdf"
                          ],
                          "items": {
                            "type": "string",
                            "x-format": {
                              "uri": true
                            }
                          },
                          "__$ref": "#/components/schemas/technical_doc"
                        },
                        "explorer": {
                          "type": "array",
                          "description": "Array of block explorer URLs.",
                          "example": [
                            "https://blockchain.coinmarketcap.com/chain/bitcoin",
                            "https://blockchain.info/",
                            "https://live.blockcypher.com/btc/"
                          ],
                          "items": {
                            "type": "string",
                            "x-format": {
                              "uri": true
                            }
                          },
                          "__$ref": "#/components/schemas/explorer"
                        },
                        "source_code": {
                          "type": "array",
                          "description": "Array of source code URLs.",
                          "example": [
                            "https://github.com/bitcoin/"
                          ],
                          "items": {
                            "type": "string",
                            "x-format": {
                              "uri": true
                            }
                          },
                          "__$ref": "#/components/schemas/source_code"
                        },
                        "message_board": {
                          "type": "array",
                          "description": "Array of message board URLs.",
                          "example": [
                            "https://bitcointalk.org"
                          ],
                          "items": {
                            "type": "string",
                            "x-format": {
                              "uri": true
                            }
                          },
                          "__$ref": "#/components/schemas/message_board"
                        },
                        "chat": {
                          "type": "array",
                          "description": "Array of chat service URLs.",
                          "example": [],
                          "items": {
                            "type": "string",
                            "x-format": {
                              "uri": true
                            }
                          },
                          "__$ref": "#/components/schemas/chat"
                        },
                        "announcement": {
                          "type": "array",
                          "description": "Array of announcement URLs.",
                          "example": [],
                          "items": {
                            "type": "string",
                            "x-format": {
                              "uri": true
                            }
                          },
                          "__$ref": "#/components/schemas/announcement"
                        },
                        "reddit": {
                          "type": "array",
                          "description": "Array of Reddit community page URLs.",
                          "example": [
                            "https://reddit.com/r/bitcoin"
                          ],
                          "items": {
                            "type": "string",
                            "x-format": {
                              "uri": true
                            }
                          },
                          "__$ref": "#/components/schemas/reddit"
                        },
                        "twitter": {
                          "type": "array",
                          "description": "Array of official twitter profile URLs.",
                          "example": [
                            "https://twitter.com/Bitcoin"
                          ],
                          "items": {
                            "type": "string",
                            "x-format": {
                              "uri": true
                            }
                          },
                          "__$ref": "#/components/schemas/twitter"
                        }
                      },
                      "required": [
                        "website",
                        "technical_doc",
                        "explorer",
                        "source_code",
                        "message_board",
                        "chat",
                        "announcement",
                        "reddit",
                        "twitter"
                      ],
                      "__$ref": "#/components/schemas/Cryptocurrencies_Info_-_URLs_object"
                    }
                  },
                  "required": [
                    "id",
                    "name",
                    "symbol",
                    "category",
                    "slug",
                    "logo",
                    "description",
                    "date_added",
                    "date_launched",
                    "tags",
                    "platform",
                    "urls"
                  ],
                  "__$ref": "#/components/schemas/Cryptocurrencies_Info_-_Cryptocurrency_object._Please_note_this_will_be_wrapped_in_an_array_if_you_request_by_symbol_using_the_v2_endpoint."
                },
                "__$ref": "#/components/schemas/Cryptocurrency_Info_-_Results_map"
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
            "__$ref": "#/components/schemas/Cryptocurrencies_Info_-_Response_Model"
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
