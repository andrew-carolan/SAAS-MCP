# GET /v4/dex/listings/info

**Summary:** DEX Metadata

**Description:** Returns all static metadata for one or more decentralised exchanges. This information includes details like launch 
date, logo, official website URL, social links, and market fee documentation URL.

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **id** (query) - *Optional*: One or more comma-separated CoinMarketCap cryptocurrency exchange ids.
- **aux** (query) - *Optional*: Default:`""`
Valid values: `"urls"` `"logo"` `"description"` `"date_launched"` `"notice"`
Optionally specify a comma-separated list of supplemental data fields to return.

### Raw Data

```json
{
  "slug": "dex-metadata",
  "summary": "DEX Metadata",
  "method": "get",
  "description": "Returns all static metadata for one or more decentralised exchanges. This information includes details like launch \ndate, logo, official website URL, social links, and market fee documentation URL.",
  "operationId": "getListingsInfo",
  "contentTypes": [],
  "path": "/v4/dex/listings/info",
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
      "description": "One or more comma-separated CoinMarketCap cryptocurrency exchange ids.",
      "required": false,
      "schema": {
        "type": "string"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "aux",
      "in": "query",
      "description": "Default:`\"\"`\nValid values: `\"urls\"` `\"logo\"` `\"description\"` `\"date_launched\"` `\"notice\"`\nOptionally specify a comma-separated list of supplemental data fields to return.",
      "required": false,
      "schema": {
        "type": "string",
        "default": ""
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
      "description": "OK",
      "content": [
        {
          "examples": [],
          "mediaType": "application/json",
          "encoding": null,
          "schema": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer",
                  "description": "The unique CoinMarketCap ID for this exchange.",
                  "format": "int32"
                },
                "name": {
                  "type": "string",
                  "description": "The name of this exchange."
                },
                "slug": {
                  "type": "string",
                  "description": "The web URL friendly shorthand version of this exchange name."
                },
                "logo": {
                  "type": "string",
                  "description": "Link to a CoinMarketCap hosted logo png for this exchange. 64px is default size returned. Replace \"64x64\" in the image path with these alternative sizes: 16, 32, 64, 128, 200"
                },
                "status": {
                  "type": "string",
                  "description": "Current status of the DEX. Can be \"active\" or \"inactive\". "
                },
                "description": {
                  "type": "string",
                  "description": "A CoinMarketCap supplied brief description of this DEX pair. This field will return null if a description is not available."
                },
                "notice": {
                  "type": "string",
                  "description": "A Markdown formatted message outlining a condition that is impacting the availability of the exchange's market data or the secure use of the exchange, otherwise null. This may include a maintenance event on the exchange's end or CoinMarketCap's end, an alert about reported issues with withdrawls from this exchange, or another condition that may be impacting the exchange and it's markets. If present, this notice is also displayed in an alert banner at the top of the exchange's page on coinmarketcap.com."
                },
                "urls": {
                  "type": "object",
                  "properties": {
                    "website": {
                      "type": "array",
                      "description": "Official website URLs.",
                      "items": {
                        "type": "string",
                        "description": "Official website URLs."
                      }
                    },
                    "blog": {
                      "type": "array",
                      "description": "Official blog URLs.",
                      "items": {
                        "type": "string",
                        "description": "Official blog URLs."
                      }
                    },
                    "chat": {
                      "type": "array",
                      "description": "Official chat URLs.",
                      "items": {
                        "type": "string",
                        "description": "Official chat URLs."
                      }
                    },
                    "fee": {
                      "type": "array",
                      "description": "Official web URLs covering exchange fees.",
                      "items": {
                        "type": "string",
                        "description": "Official web URLs covering exchange fees."
                      }
                    },
                    "twitter": {
                      "type": "array",
                      "description": "Official twitter profile URLs.",
                      "items": {
                        "type": "string",
                        "description": "Official twitter profile URLs."
                      }
                    }
                  },
                  "description": "An object containing various resource URLs for this exchange.",
                  "__$ref": "#/components/schemas/DexUrls"
                },
                "date_launched": {
                  "type": "string",
                  "description": "Timestamp (ISO 8601) of the date this exchange launched. This field is only returned if requested through the aux request parameter.",
                  "format": "date-time"
                }
              },
              "__$ref": "#/components/schemas/DexCommonInfoDTO"
            }
          }
        }
      ]
    }
  ]
}
```
