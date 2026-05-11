# GET /v1/cryptocurrency/quotes/latest

**Summary:** Quotes Latest v1 (deprecated)

**Description:** Returns the latest market quote for 1 or more cryptocurrencies. Use the "convert" option to return market values in multiple fiat and cryptocurrency conversions in the same call.


**This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
- Basic
- Startup
- Hobbyist
- Standard
- Professional
- Enterprise

**Cache / Update frequency:** Every 60 seconds.  
**Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up) and 1 call credit per `convert` option beyond the first.  
**CMC equivalent pages:** Latest market data pages for specific cryptocurrencies like [coinmarketcap.com/currencies/bitcoin/](https://coinmarketcap.com/currencies/bitcoin/).  
   
***NOTE:** Use this endpoint to request the latest quote for specific cryptocurrencies. If you need to request all cryptocurrencies use `/v1/cryptocurrency/listings/latest` which is optimized for that purpose. The response data between these endpoints is otherwise the same.*

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **id** (query) - *Optional*: One or more comma-separated cryptocurrency CoinMarketCap IDs. Example: 1,2
- **slug** (query) - *Optional*: Alternatively pass a comma-separated list of cryptocurrency slugs. Example: "bitcoin,ethereum"
- **symbol** (query) - *Optional*: Alternatively pass one or more comma-separated cryptocurrency symbols. Example: "BTC,ETH". At least one "id" *or* "slug" *or* "symbol" is required for this request.
- **convert** (query) - *Optional*: Optionally calculate market quotes in up to 120 currencies at once by passing a comma-separated list of cryptocurrency or fiat currency symbols. Each additional convert option beyond the first requires an additional call credit. A list of supported fiat options can be found [here](/guides/standards-and-conventions). Each conversion is returned in its own "quote" object.
- **convert_id** (query) - *Optional*: Optionally calculate market quotes by CoinMarketCap ID instead of symbol. This option is identical to `convert` outside of ID format. Ex: convert_id=1,2781 would replace convert=BTC,USD in your query. This parameter cannot be used when `convert` is used.
- **aux** (query) - *Optional*: Optionally specify a comma-separated list of supplemental data fields to return. Pass `num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply,market_cap_by_total_supply,volume_24h_reported,volume_7d,volume_7d_reported,volume_30d,volume_30d_reported,is_active,is_fiat` to include all auxiliary fields.
- **skip_invalid** (query) - *Optional*: Pass `true` to relax request validation rules. When requesting records on multiple cryptocurrencies an error is returned if no match is found for 1 or more requested cryptocurrencies. If set to true, invalid lookups will be skipped allowing valid cryptocurrencies to still be returned.

### Raw Data

```json
{
  "slug": "quotes-latest-v1-deprecated",
  "summary": "Quotes Latest v1 (deprecated)",
  "method": "get",
  "description": "Returns the latest market quote for 1 or more cryptocurrencies. Use the \"convert\" option to return market values in multiple fiat and cryptocurrency conversions in the same call.\n\n\n**This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**\n- Basic\n- Startup\n- Hobbyist\n- Standard\n- Professional\n- Enterprise\n\n**Cache / Update frequency:** Every 60 seconds.  \n**Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up) and 1 call credit per `convert` option beyond the first.  \n**CMC equivalent pages:** Latest market data pages for specific cryptocurrencies like [coinmarketcap.com/currencies/bitcoin/](https://coinmarketcap.com/currencies/bitcoin/).  \n   \n***NOTE:** Use this endpoint to request the latest quote for specific cryptocurrencies. If you need to request all cryptocurrencies use `/v1/cryptocurrency/listings/latest` which is optimized for that purpose. The response data between these endpoints is otherwise the same.*",
  "operationId": "getV1CryptocurrencyQuotesLatest",
  "contentTypes": [],
  "path": "/v1/cryptocurrency/quotes/latest",
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
      "name": "convert",
      "in": "query",
      "description": "Optionally calculate market quotes in up to 120 currencies at once by passing a comma-separated list of cryptocurrency or fiat currency symbols. Each additional convert option beyond the first requires an additional call credit. A list of supported fiat options can be found [here](/guides/standards-and-conventions). Each conversion is returned in its own \"quote\" object.",
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
      "name": "convert_id",
      "in": "query",
      "description": "Optionally calculate market quotes by CoinMarketCap ID instead of symbol. This option is identical to `convert` outside of ID format. Ex: convert_id=1,2781 would replace convert=BTC,USD in your query. This parameter cannot be used when `convert` is used.",
      "required": null,
      "schema": {
        "type": "string",
        "pattern": "(^\\d+(?:,\\d+)*$|(\\d,)*PLATFORM_ID+(?:,\\d+)*$)"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "aux",
      "in": "query",
      "description": "Optionally specify a comma-separated list of supplemental data fields to return. Pass `num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply,market_cap_by_total_supply,volume_24h_reported,volume_7d,volume_7d_reported,volume_30d,volume_30d_reported,is_active,is_fiat` to include all auxiliary fields.",
      "required": null,
      "schema": {
        "type": "string",
        "pattern": "^(num_market_pairs|cmc_rank|date_added|tags|platform|max_supply|circulating_supply|total_supply|market_cap_by_total_supply|volume_24h_reported|volume_7d|volume_7d_reported|volume_30d|volume_30d_reported|is_active|is_fiat)+(?:,(num_market_pairs|cmc_rank|date_added|tags|platform|max_supply|circulating_supply|total_supply|market_cap_by_total_supply|volume_24h_reported|volume_7d|volume_7d_reported|volume_30d|volume_30d_reported|is_active|is_fiat)+)*$",
        "default": "num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply,is_active,is_fiat"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "skip_invalid",
      "in": "query",
      "description": "Pass `true` to relax request validation rules. When requesting records on multiple cryptocurrencies an error is returned if no match is found for 1 or more requested cryptocurrencies. If set to true, invalid lookups will be skipped allowing valid cryptocurrencies to still be returned.",
      "required": null,
      "schema": {
        "type": "boolean",
        "default": true
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
                "description": "A map of cryptocurrency objects by ID, symbol, or slug (as used in query parameters).",
                "example": {
                  "1": {
                    "id": 1,
                    "name": "Bitcoin",
                    "symbol": "BTC",
                    "slug": "bitcoin",
                    "is_active": 1,
                    "is_fiat": 0,
                    "circulating_supply": 17199862,
                    "total_supply": 17199862,
                    "max_supply": 21000000,
                    "date_added": "2013-04-28T00:00:00.000Z",
                    "num_market_pairs": 331,
                    "cmc_rank": 1,
                    "last_updated": "2018-08-09T21:56:28.000Z",
                    "tags": [
                      "mineable"
                    ],
                    "platform": null,
                    "self_reported_circulating_supply": null,
                    "self_reported_market_cap": null,
                    "minted_market_cap": 1802955697670.94,
                    "quote": {
                      "USD": {
                        "price": 6602.60701122,
                        "volume_24h": 4314444687.5194,
                        "volume_change_24h": -0.152774,
                        "percent_change_1h": 0.988615,
                        "percent_change_24h": 4.37185,
                        "percent_change_7d": -12.1352,
                        "percent_change_30d": -12.1352,
                        "market_cap": 852164659250.2758,
                        "market_cap_dominance": 51,
                        "fully_diluted_market_cap": 952835089431.14,
                        "last_updated": "2018-08-09T21:56:28.000Z"
                      }
                    }
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
                    "is_active": {
                      "type": "integer",
                      "description": "1 if this cryptocurrency has at least 1 active market currently being tracked by the platform, otherwise 0. A value of 1 is analogous with `listing_status=active`.",
                      "example": 1,
                      "minimum": 0,
                      "maximum": 1
                    },
                    "is_fiat": {
                      "type": "integer",
                      "description": "1 if this is a fiat",
                      "example": 1,
                      "minimum": 0,
                      "maximum": 1
                    },
                    "cmc_rank": {
                      "type": "integer",
                      "description": "The cryptocurrency's CoinMarketCap rank by market cap.",
                      "example": 5
                    },
                    "num_market_pairs": {
                      "type": "integer",
                      "description": "The number of active trading pairs available for this cryptocurrency across supported exchanges.",
                      "example": 500
                    },
                    "circulating_supply": {
                      "type": "number",
                      "description": "The approximate number of coins circulating for this cryptocurrency.",
                      "example": 16950100
                    },
                    "total_supply": {
                      "type": "number",
                      "description": "The approximate total amount of coins in existence right now (minus any coins that have been verifiably burned).",
                      "example": 16950100
                    },
                    "market_cap_by_total_supply": {
                      "type": "number",
                      "description": "The market cap by total supply. *This field is only returned if requested through the `aux` request parameter.*",
                      "example": 158055024432
                    },
                    "max_supply": {
                      "type": "number",
                      "description": "The expected maximum limit of coins ever to be available for this cryptocurrency.",
                      "example": 21000000
                    },
                    "date_added": {
                      "type": "string",
                      "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                      "description": "Timestamp (ISO 8601) of when this cryptocurrency was added to CoinMarketCap.",
                      "example": "2013-04-28T00:00:00.000Z"
                    },
                    "tags": {
                      "type": "array",
                      "description": "Array of tags associated with this cryptocurrency. Currently only a mineable tag will be returned if the cryptocurrency is mineable. Additional tags will be returned in the future.",
                      "example": [
                        "mineable"
                      ],
                      "items": {
                        "type": "string"
                      },
                      "__$ref": "#/components/schemas/tags"
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
                    "last_updated": {
                      "type": "string",
                      "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                      "description": "Timestamp (ISO 8601) of the last time this cryptocurrency's market data was updated.",
                      "example": "2018-06-02T23:59:59.999Z"
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
                    "minted_market_cap": {
                      "type": "number",
                      "description": "The minted market cap for this cryptocurrency.",
                      "example": 1802955697670.94
                    },
                    "quote": {
                      "type": "object",
                      "description": "A map of market quotes in different currency conversions. The default map included is USD.",
                      "additionalProperties": {
                        "type": "object",
                        "description": "A market quote in the currency conversion option.",
                        "properties": {
                          "price": {
                            "type": "number",
                            "description": "Price in the specified currency.",
                            "example": 7139.82
                          },
                          "volume_24h": {
                            "type": "number",
                            "description": "Rolling 24 hour adjusted volume in the specified currency.",
                            "example": 4885880000
                          },
                          "volume_change_24h": {
                            "type": "number",
                            "description": "24 hour change in the specified currencies volume.",
                            "example": 5.75
                          },
                          "volume_24h_reported": {
                            "type": "number",
                            "description": "Rolling 24 hour reported volume in the specified currency. *This field is only returned if requested through the `aux` request parameter.*",
                            "example": 4885880000
                          },
                          "volume_7d": {
                            "type": "number",
                            "description": "Rolling 7 day adjusted volume in the specified currency. *This field is only returned if requested through the `aux` request parameter.*",
                            "example": 4885880000
                          },
                          "volume_7d_reported": {
                            "type": "number",
                            "description": "Rolling 7 day reported volume in the specified currency. *This field is only returned if requested through the `aux` request parameter.*",
                            "example": 4885880000
                          },
                          "volume_30d": {
                            "type": "number",
                            "description": "Rolling 30 day adjusted volume in the specified currency. *This field is only returned if requested through the `aux` request parameter.*",
                            "example": 4885880000
                          },
                          "volume_30d_reported": {
                            "type": "number",
                            "description": "Rolling 30 day reported volume in the specified currency. *This field is only returned if requested through the `aux` request parameter.*",
                            "example": 4885880000
                          },
                          "market_cap": {
                            "type": "number",
                            "description": "Market cap in the specified currency.",
                            "example": 121020662982
                          },
                          "market_cap_dominance": {
                            "type": "number",
                            "description": "Market cap dominance in the specified currency.",
                            "example": 121020662982
                          },
                          "fully_diluted_market_cap": {
                            "type": "number",
                            "description": "Fully diluted market cap in the specified currency.",
                            "example": 121020662982
                          },
                          "percent_change_1h": {
                            "type": "number",
                            "description": "1 hour change in the specified currency.",
                            "example": 0.03
                          },
                          "percent_change_24h": {
                            "type": "number",
                            "description": "24 hour change in the specified currency.",
                            "example": 5.75
                          },
                          "percent_change_7d": {
                            "type": "number",
                            "description": "7 day change in the specified currency.",
                            "example": -19.64
                          },
                          "percent_change_30d": {
                            "type": "number",
                            "description": "30 day change in the specified currency.",
                            "example": -19.64
                          },
                          "last_updated": {
                            "type": "string",
                            "format": "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
                            "description": "Timestamp (ISO 8601) of when the conversion currency's current value was referenced.",
                            "example": "2018-06-02T23:59:59.999Z"
                          }
                        },
                        "required": [
                          "price",
                          "volume_24h",
                          "market_cap",
                          "market_cap_dominance",
                          "fully_diluted_market_cap",
                          "percent_change_1h",
                          "percent_change_24h",
                          "percent_change_7d",
                          "percent_change_30d",
                          "last_updated"
                        ],
                        "__$ref": "#/components/schemas/Cryptocurrency_Quotes_Latest_-_Quote_object"
                      },
                      "__$ref": "#/components/schemas/Cryptocurrency_Quotes_Latest_-_Quote_map"
                    }
                  },
                  "required": [
                    "id",
                    "name",
                    "symbol",
                    "slug",
                    "last_updated",
                    "quote"
                  ],
                  "__$ref": "#/components/schemas/Cryptocurrency_Quotes_Latest_-_Cryptocurrency_object"
                },
                "__$ref": "#/components/schemas/Cryptocurrency_Quotes_Latest_-_Cryptocurrency_Results_map"
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
            "__$ref": "#/components/schemas/Cryptocurrency_Quotes_Latest_-_Response_Model"
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
