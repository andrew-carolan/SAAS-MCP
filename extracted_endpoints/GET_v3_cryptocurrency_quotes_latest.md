# GET /v3/cryptocurrency/quotes/latest

**Summary:** Cryptocurrency Quotes Latest

**Description:** Returns the latest market quote for 1 or more cryptocurrencies. Use the "convert" option to return market values in multiple fiat and cryptocurrency conversions in the same call.

**Please note**: This documentation relates to our updated V3 endpoint, which may be incompatible with our V2 versions. Documentation for deprecated endpoints can be found [the deprecated section](/pro-api-reference/deprecated).


**This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
- Basic
- Startup
- Hobbyist
- Standard
- Professional
- Enterprise

**Cache / Update frequency:** Every 60 seconds.  
**Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up) and 1 call credit per \`convert\` option beyond the first.  
**CMC equivalent pages:** Latest market data pages for specific cryptocurrencies like [coinmarketcap.com/currencies/bitcoin/](https://coinmarketcap.com/currencies/bitcoin/).  
   
***NOTE:** Use this endpoint to request the latest quote for specific cryptocurrencies. If you need to request all cryptocurrencies use `/v3/cryptocurrency/listings/latest` which is optimized for that purpose. The response data between these endpoints is otherwise the same.*

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **id** (query) - *Optional*: One or more comma-separated cryptocurrency CoinMarketCap IDs.
- **slug** (query) - *Optional*: Alternatively pass a comma-separated list of cryptocurrency slugs.
- **symbol** (query) - *Optional*: Alternatively pass one or more comma-separated cryptocurrency symbols.
- **convert** (query) - *Optional*: Optionally calculate market quotes in up to 120 currencies at once by passing a comma-separated list of cryptocurrency or fiat currency symbols.
- **convert_id** (query) - *Optional*: Optionally calculate market quotes by CoinMarketCap ID instead of symbol.
- **aux** (query) - *Optional*: Optionally specify a comma-separated list of supplemental data fields to return.
- **skip_invalid** (query) - *Optional*: Pass true to relax request validation rules. When requesting records on multiple cryptocurrencies an error is returned if no match is found for 1 or more requested cryptocurrencies. If set to true, invalid lookups will be skipped allowing valid cryptocurrencies to still be returned.

### Raw Data

```json
{
  "slug": "cryptocurrency-quotes-latest",
  "summary": "Cryptocurrency Quotes Latest",
  "method": "get",
  "description": "Returns the latest market quote for 1 or more cryptocurrencies. Use the \"convert\" option to return market values in multiple fiat and cryptocurrency conversions in the same call.\n\n**Please note**: This documentation relates to our updated V3 endpoint, which may be incompatible with our V2 versions. Documentation for deprecated endpoints can be found [the deprecated section](/pro-api-reference/deprecated).\n\n\n**This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**\n- Basic\n- Startup\n- Hobbyist\n- Standard\n- Professional\n- Enterprise\n\n**Cache / Update frequency:** Every 60 seconds.  \n**Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up) and 1 call credit per \\`convert\\` option beyond the first.  \n**CMC equivalent pages:** Latest market data pages for specific cryptocurrencies like [coinmarketcap.com/currencies/bitcoin/](https://coinmarketcap.com/currencies/bitcoin/).  \n   \n***NOTE:** Use this endpoint to request the latest quote for specific cryptocurrencies. If you need to request all cryptocurrencies use `/v3/cryptocurrency/listings/latest` which is optimized for that purpose. The response data between these endpoints is otherwise the same.*",
  "operationId": "getV3CryptocurrencyQuotesLatest",
  "contentTypes": [],
  "path": "/v3/cryptocurrency/quotes/latest",
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
      "description": "One or more comma-separated cryptocurrency CoinMarketCap IDs.",
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
      "name": "slug",
      "in": "query",
      "description": "Alternatively pass a comma-separated list of cryptocurrency slugs.",
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
      "name": "symbol",
      "in": "query",
      "description": "Alternatively pass one or more comma-separated cryptocurrency symbols.",
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
      "name": "convert",
      "in": "query",
      "description": "Optionally calculate market quotes in up to 120 currencies at once by passing a comma-separated list of cryptocurrency or fiat currency symbols.",
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
      "description": "Optionally calculate market quotes by CoinMarketCap ID instead of symbol.",
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
      "description": "Optionally specify a comma-separated list of supplemental data fields to return.",
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
      "name": "skip_invalid",
      "in": "query",
      "description": "Pass true to relax request validation rules. When requesting records on multiple cryptocurrencies an error is returned if no match is found for 1 or more requested cryptocurrencies. If set to true, invalid lookups will be skipped allowing valid cryptocurrencies to still be returned.",
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
                  "format": "int32"
                },
                "name": {
                  "type": "string"
                },
                "symbol": {
                  "type": "string"
                },
                "slug": {
                  "type": "string"
                },
                "platform": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "integer",
                      "format": "int32"
                    },
                    "slug": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "symbol": {
                      "type": "string"
                    },
                    "token_address": {
                      "type": "string"
                    }
                  },
                  "__$ref": "#/components/schemas/Platform"
                },
                "quote": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "integer",
                        "description": "Currency ID",
                        "format": "int32"
                      },
                      "symbol": {
                        "type": "string",
                        "description": "Currency symbol"
                      },
                      "price": {
                        "type": "number",
                        "description": "Current price in the specified currency",
                        "format": "bigdecimal"
                      },
                      "volume_24h": {
                        "type": "number",
                        "description": "24-hour trading volume",
                        "format": "bigdecimal"
                      },
                      "volume_24h_reported": {
                        "type": "number",
                        "description": "Reported 24-hour trading volume",
                        "format": "bigdecimal"
                      },
                      "volume_7d": {
                        "type": "number",
                        "description": "7-day trading volume",
                        "format": "bigdecimal"
                      },
                      "volume_7d_reported": {
                        "type": "number",
                        "description": "Reported 7-day trading volume",
                        "format": "bigdecimal"
                      },
                      "volume_30d": {
                        "type": "number",
                        "description": "30-day trading volume",
                        "format": "bigdecimal"
                      },
                      "volume_30d_reported": {
                        "type": "number",
                        "description": "Reported 30-day trading volume",
                        "format": "bigdecimal"
                      },
                      "volume_change_24h": {
                        "type": "number",
                        "description": "24-hour volume change percentage",
                        "format": "bigdecimal"
                      },
                      "percent_change_1h": {
                        "type": "number",
                        "description": "1-hour percentage change",
                        "format": "bigdecimal"
                      },
                      "percent_change_24h": {
                        "type": "number",
                        "description": "24-hour percentage change",
                        "format": "bigdecimal"
                      },
                      "percent_change_7d": {
                        "type": "number",
                        "description": "7-day percentage change",
                        "format": "bigdecimal"
                      },
                      "percent_change_30d": {
                        "type": "number",
                        "description": "30-day percentage change",
                        "format": "bigdecimal"
                      },
                      "percent_change_60d": {
                        "type": "number",
                        "description": "60-day percentage change",
                        "format": "bigdecimal"
                      },
                      "percent_change_90d": {
                        "type": "number",
                        "description": "90-day percentage change",
                        "format": "bigdecimal"
                      },
                      "market_cap": {
                        "type": "number",
                        "description": "Current market capitalization",
                        "format": "bigdecimal"
                      },
                      "market_cap_dominance": {
                        "type": "number",
                        "description": "Market cap dominance percentage",
                        "format": "bigdecimal"
                      },
                      "fully_diluted_market_cap": {
                        "type": "number",
                        "description": "Fully diluted market capitalization",
                        "format": "bigdecimal"
                      },
                      "tvl": {
                        "type": "number",
                        "description": "Total Value Locked",
                        "format": "bigdecimal"
                      },
                      "market_cap_by_total_supply": {
                        "type": "number",
                        "description": "Market cap calculated by total supply",
                        "format": "bigdecimal"
                      },
                      "last_updated": {
                        "type": "string",
                        "description": "Last updated timestamp"
                      }
                    },
                    "__$ref": "#/components/schemas/Quote"
                  }
                },
                "tags": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "slug": {
                        "type": "string"
                      },
                      "name": {
                        "type": "string"
                      },
                      "category": {
                        "type": "string"
                      }
                    },
                    "__$ref": "#/components/schemas/CryptoTag"
                  }
                },
                "is_active": {
                  "type": "integer",
                  "format": "int32"
                },
                "infinite_supply": {
                  "type": "boolean"
                },
                "is_market_cap_included_in_calc": {
                  "type": "integer",
                  "format": "int32"
                },
                "is_fiat": {
                  "type": "integer",
                  "format": "int32"
                },
                "circulating_supply": {
                  "type": "number",
                  "description": "Circulating supply of the cryptocurrency",
                  "format": "bigdecimal"
                },
                "total_supply": {
                  "type": "number",
                  "description": "Total supply of the cryptocurrency",
                  "format": "bigdecimal"
                },
                "max_supply": {
                  "type": "number",
                  "description": "Maximum supply of the cryptocurrency",
                  "format": "bigdecimal"
                },
                "date_added": {
                  "type": "string"
                },
                "num_market_pairs": {
                  "type": "integer",
                  "format": "int32"
                },
                "cmc_rank": {
                  "type": "integer",
                  "format": "int32"
                },
                "last_updated": {
                  "type": "string"
                },
                "tvl_ratio": {
                  "type": "number",
                  "description": "TVL to market cap ratio",
                  "format": "bigdecimal"
                },
                "self_reported_circulating_supply": {
                  "type": "number",
                  "description": "Self-reported circulating supply",
                  "format": "bigdecimal"
                },
                "self_reported_market_cap": {
                  "type": "number",
                  "description": "Self-reported market capitalization",
                  "format": "bigdecimal"
                },
                "unlocked_circulating_supply": {
                  "type": "number",
                  "description": "Unlocked circulating supply",
                  "format": "bigdecimal"
                },
                "unlocked_market_cap": {
                  "type": "number",
                  "description": "Unlocked market capitalization",
                  "format": "bigdecimal"
                }
              },
              "__$ref": "#/components/schemas/CryptoQuoteV3DTO"
            }
          }
        }
      ]
    }
  ]
}
```
