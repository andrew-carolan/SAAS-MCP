# GET /v4/dex/listings/quotes

**Summary:** DEX Listings Latest

**Description:** Returns a paginated list of all decentralised cryptocurrency exchanges including 
the latest aggregate market data for each exchange. Use the "convert" option to 
return market values in multiple fiat and cryptocurrency conversions in the same call.

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **start** (query) - *Optional*: Optionally offset the start (1-based index) of the paginated list of items to return.
- **limit** (query) - *Optional*: Optionally specify the number of results to return. Use this parameter and the 
"start" parameter to determine your own pagination size.
- **sort** (query) - *Optional*: Default:`"volume_24h"`
Valid values: `"name"` `"volume_24h"` `"market_share"` `"num_markets"`
What field to sort the list of exchanges by.
- **sort_dir** (query) - *Optional*: Default:`"desc"`
Valid values: `"desc"` `"asc"`
The direction in which to order exchanges against the specified sort.
- **type** (query) - *Optional*: Default:`"all"`
Valid values: `"all"` `"orderbook"` `"swap"` `"aggregator"`
The category for this exchange.
- **aux** (query) - *Optional*: Default:`""`
Valid values: `"date_launched"`
Optionally specify a comma-separated list of supplemental data fields to return.
- **convert_id** (query) - *Optional*: Optionally calculate market quotes in up to 30 currencies at once by passing a comma-separated list of cryptocurrency 
or fiat currency IDs. Each additional convert option beyond the first requires an additional call credit. A list of 
supported fiat options can be found in our API document. Each conversion is returned in its own "quote" object.

### Raw Data

```json
{
  "slug": "dex-listings-latest",
  "summary": "DEX Listings Latest",
  "method": "get",
  "description": "Returns a paginated list of all decentralised cryptocurrency exchanges including \nthe latest aggregate market data for each exchange. Use the \"convert\" option to \nreturn market values in multiple fiat and cryptocurrency conversions in the same call.",
  "operationId": "getLatestListings",
  "contentTypes": [],
  "path": "/v4/dex/listings/quotes",
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
      "required": false,
      "schema": {
        "type": "string",
        "default": "1"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "limit",
      "in": "query",
      "description": "Optionally specify the number of results to return. Use this parameter and the \n\"start\" parameter to determine your own pagination size.",
      "required": false,
      "schema": {
        "type": "string",
        "default": "50"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "sort",
      "in": "query",
      "description": "Default:`\"volume_24h\"`\nValid values: `\"name\"` `\"volume_24h\"` `\"market_share\"` `\"num_markets\"`\nWhat field to sort the list of exchanges by.",
      "required": false,
      "schema": {
        "type": "string",
        "default": "volume_24h"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "sort_dir",
      "in": "query",
      "description": "Default:`\"desc\"`\nValid values: `\"desc\"` `\"asc\"`\nThe direction in which to order exchanges against the specified sort.",
      "required": false,
      "schema": {
        "type": "string",
        "default": "desc"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "type",
      "in": "query",
      "description": "Default:`\"all\"`\nValid values: `\"all\"` `\"orderbook\"` `\"swap\"` `\"aggregator\"`\nThe category for this exchange.",
      "required": false,
      "schema": {
        "type": "string",
        "default": "all"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "aux",
      "in": "query",
      "description": "Default:`\"\"`\nValid values: `\"date_launched\"`\nOptionally specify a comma-separated list of supplemental data fields to return.",
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
      "name": "convert_id",
      "in": "query",
      "description": "Optionally calculate market quotes in up to 30 currencies at once by passing a comma-separated list of cryptocurrency \nor fiat currency IDs. Each additional convert option beyond the first requires an additional call credit. A list of \nsupported fiat options can be found in our API document. Each conversion is returned in its own \"quote\" object.",
      "required": false,
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
                "type": {
                  "type": "string",
                  "description": "The type of DEX this exchange is, such as, Orderbook, Swap, and Aggregator."
                },
                "quote": {
                  "type": "array",
                  "description": "A map of market quotes in different currency conversions. The default map included is USD.",
                  "items": {
                    "type": "object",
                    "properties": {
                      "convert_id": {
                        "type": "string",
                        "description": "id of specified currency."
                      },
                      "market_type": {
                        "type": "string",
                        "description": "Type of market data being returned, such as Spot, Perpetual, and Futures. "
                      },
                      "last_updated": {
                        "type": "string",
                        "description": "Timestamp (ISO 8601) of when the conversion currency's current value was referenced for this conversion.",
                        "format": "date-time"
                      },
                      "volume_24h": {
                        "type": "number",
                        "description": "Reported 24 hour volume in the specified currency."
                      },
                      "percent_change_volume_24h": {
                        "type": "number",
                        "description": "24 hour volume change percentage in the specified currency. Only applicable for fiat conversions."
                      },
                      "num_transactions_24h": {
                        "type": "number",
                        "description": "Total number of transactions in the past 24 hours. This field will return null if not available."
                      }
                    },
                    "description": "DEX exchange quote information",
                    "__$ref": "#/components/schemas/DexInfoQuote"
                  }
                },
                "date_launched": {
                  "type": "string",
                  "description": "Timestamp (ISO 8601) of the date this exchange launched. This field is only returned if requested through the aux request parameter.",
                  "format": "date-time"
                },
                "num_market_pairs": {
                  "type": "string",
                  "description": "The number of trading pairs actively tracked on this exchange."
                },
                "last_updated": {
                  "type": "string",
                  "description": "Timestamp (ISO 8601) of the last time this record was updated."
                },
                "market_share": {
                  "type": "number",
                  "description": "Percentage of DEX market share based on volume.",
                  "format": "bigdecimal"
                }
              },
              "__$ref": "#/components/schemas/DexInfoDTO"
            }
          }
        }
      ]
    }
  ]
}
```
