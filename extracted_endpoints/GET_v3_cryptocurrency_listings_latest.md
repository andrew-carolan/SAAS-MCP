# GET /v3/cryptocurrency/listings/latest

**Summary:** Cryptocurrency Listings

**Description:** Returns a paginated list of all active cryptocurrencies with latest market data. The default "market_cap" sort returns cryptocurrency in order of CoinMarketCap's market cap rank (as outlined in [our methodology](https://coinmarketcap.com/methodology/)) but you may configure this call to order by another market ranking field. Use the "convert" option to return market values in multiple fiat and cryptocurrency conversions in the same call.


You may sort against any of the following:  
**market_cap**: CoinMarketCap's market cap rank as outlined in [our methodology](https://coinmarketcap.com/methodology/).  
**market_cap_strict**: A strict market cap sort (latest trade price x circulating supply).  
**name**: The cryptocurrency name.  
**symbol**: The cryptocurrency symbol.  
**date_added**: Date cryptocurrency was added to the system.  
**price**: latest average trade price across markets.  
**circulating_supply**: approximate number of coins currently in circulation.  
**total_supply**: approximate total amount of coins in existence right now (minus any coins that have been verifiably burned).  
**max_supply**: our best approximation of the maximum amount of coins that will ever exist in the lifetime of the currency.  
**num_market_pairs**: number of market pairs across all exchanges trading each currency.  
**market_cap_by_total_supply_strict**: market cap by total supply.  
**volume_24h**: rolling 24 hour adjusted trading volume.  
**volume_7d**: rolling 24 hour adjusted trading volume.  
**volume_30d**: rolling 24 hour adjusted trading volume.  
**percent_change_1h**: 1 hour trading price percentage change for each currency.  
**percent_change_24h**: 24 hour trading price percentage change for each currency.  
**percent_change_7d**: 7 day trading price percentage change for each currency.  

  **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
  - Basic
  - Hobbyist
  - Startup
  - Standard
  - Professional
  - Enterprise

**Cache / Update frequency:** Every 60 seconds.  
**Plan credit use:** 1 call credit per 200 cryptocurrencies returned (rounded up) and 1 call credit per \`convert\` option beyond the first.
**CMC equivalent pages:** Our latest cryptocurrency listing and ranking pages like [coinmarketcap.com/all/views/all/](https://coinmarketcap.com/all/views/all/), [coinmarketcap.com/tokens/](https://coinmarketcap.com/tokens/), [coinmarketcap.com/gainers-losers/](https://coinmarketcap.com/gainers-losers/), [coinmarketcap.com/new/](https://coinmarketcap.com/new/).     
  
***NOTE:** Use this endpoint if you need a sorted and paginated list of all cryptocurrencies. If you want to query for market data on a few specific cryptocurrencies use `/v3/cryptocurrency/quotes/latest` which is optimized for that purpose. The response data between these endpoints is otherwise the same.* 

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **start** (query) - *Optional*: Optionally offset the start (1-based index) of the paginated list of items to return.
- **limit** (query) - *Optional*: Optionally specify the number of results to return. Use this parameter and the \"start\" parameter to determine your own pagination size.
- **price_min** (query) - *Optional*: Optionally specify a threshold of minimum USD price to filter results by.
- **price_max** (query) - *Optional*: Optionally specify a threshold of maximum USD price to filter results by.
- **market_cap_min** (query) - *Optional*: Optionally specify a threshold of minimum market cap to filter results by.
- **market_cap_max** (query) - *Optional*: Optionally specify a threshold of maximum market cap to filter results by.
- **volume_24h_min** (query) - *Optional*: Optionally specify a threshold of minimum 24 hour USD volume to filter results by.
- **volume_24h_max** (query) - *Optional*: Optionally specify a threshold of maximum 24 hour USD volume to filter results by.
- **circulating_supply_min** (query) - *Optional*: Optionally specify a threshold of minimum circulating supply to filter results by.
- **circulating_supply_max** (query) - *Optional*: Optionally specify a threshold of maximum circulating supply to filter results by.
- **percent_change_24h_min** (query) - *Optional*: Optionally specify a threshold of minimum 24 hour percent change to filter results by.
- **percent_change_24h_max** (query) - *Optional*: Optionally specify a threshold of maximum 24 hour percent change to filter results by.
- **convert** (query) - *Optional*: Optionally calculate market quotes in up to 120 currencies at once by passing a comma-separated list of cryptocurrency or fiat currency symbols. Each additional convert option beyond the first requires an additional call credit. Each conversion is returned in its own "quote" object.
- **convert_id** (query) - *Optional*: Optionally calculate market quotes by CoinMarketCap ID instead of symbol. This option is identical to `convert` outside of ID format. Ex: convert_id=1,2781 would replace convert=BTC,USD in your query. This parameter cannot be used when `convert` is used.
- **sort** (query) - *Optional*: What field to sort the list of cryptocurrencies by.
- **sort_dir** (query) - *Optional*: The direction in which to order cryptocurrencies against the specified sort.
- **cryptocurrency_type** (query) - *Optional*: The type of cryptocurrency to include.
- **tag** (query) - *Optional*: The tag of cryptocurrency to include.
- **aux** (query) - *Optional*: Optionally specify a comma-separated list of supplemental data fields to return. Pass num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply,market_cap_by_total_supply,volume_24h_reported,volume_7d,volume_7d_reported,volume_30d,volume_30d_reported,is_market_cap_included_in_calc to include all auxiliary fields.

### Raw Data

```json
{
  "slug": "cryptocurrency-listings",
  "summary": "Cryptocurrency Listings",
  "method": "get",
  "description": "Returns a paginated list of all active cryptocurrencies with latest market data. The default \"market_cap\" sort returns cryptocurrency in order of CoinMarketCap's market cap rank (as outlined in [our methodology](https://coinmarketcap.com/methodology/)) but you may configure this call to order by another market ranking field. Use the \"convert\" option to return market values in multiple fiat and cryptocurrency conversions in the same call.\n\n\nYou may sort against any of the following:  \n**market_cap**: CoinMarketCap's market cap rank as outlined in [our methodology](https://coinmarketcap.com/methodology/).  \n**market_cap_strict**: A strict market cap sort (latest trade price x circulating supply).  \n**name**: The cryptocurrency name.  \n**symbol**: The cryptocurrency symbol.  \n**date_added**: Date cryptocurrency was added to the system.  \n**price**: latest average trade price across markets.  \n**circulating_supply**: approximate number of coins currently in circulation.  \n**total_supply**: approximate total amount of coins in existence right now (minus any coins that have been verifiably burned).  \n**max_supply**: our best approximation of the maximum amount of coins that will ever exist in the lifetime of the currency.  \n**num_market_pairs**: number of market pairs across all exchanges trading each currency.  \n**market_cap_by_total_supply_strict**: market cap by total supply.  \n**volume_24h**: rolling 24 hour adjusted trading volume.  \n**volume_7d**: rolling 24 hour adjusted trading volume.  \n**volume_30d**: rolling 24 hour adjusted trading volume.  \n**percent_change_1h**: 1 hour trading price percentage change for each currency.  \n**percent_change_24h**: 24 hour trading price percentage change for each currency.  \n**percent_change_7d**: 7 day trading price percentage change for each currency.  \n\n  **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**\n  - Basic\n  - Hobbyist\n  - Startup\n  - Standard\n  - Professional\n  - Enterprise\n\n**Cache / Update frequency:** Every 60 seconds.  \n**Plan credit use:** 1 call credit per 200 cryptocurrencies returned (rounded up) and 1 call credit per \\`convert\\` option beyond the first.\n**CMC equivalent pages:** Our latest cryptocurrency listing and ranking pages like [coinmarketcap.com/all/views/all/](https://coinmarketcap.com/all/views/all/), [coinmarketcap.com/tokens/](https://coinmarketcap.com/tokens/), [coinmarketcap.com/gainers-losers/](https://coinmarketcap.com/gainers-losers/), [coinmarketcap.com/new/](https://coinmarketcap.com/new/).     \n  \n***NOTE:** Use this endpoint if you need a sorted and paginated list of all cryptocurrencies. If you want to query for market data on a few specific cryptocurrencies use `/v3/cryptocurrency/quotes/latest` which is optimized for that purpose. The response data between these endpoints is otherwise the same.* ",
  "operationId": "getV3CryptocurrencyListingsLatest",
  "contentTypes": [],
  "path": "/v3/cryptocurrency/listings/latest",
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
      "description": "Optionally specify the number of results to return. Use this parameter and the \\\"start\\\" parameter to determine your own pagination size.",
      "required": false,
      "schema": {
        "type": "string",
        "default": "100"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "price_min",
      "in": "query",
      "description": "Optionally specify a threshold of minimum USD price to filter results by.",
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
      "name": "price_max",
      "in": "query",
      "description": "Optionally specify a threshold of maximum USD price to filter results by.",
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
      "name": "market_cap_min",
      "in": "query",
      "description": "Optionally specify a threshold of minimum market cap to filter results by.",
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
      "name": "market_cap_max",
      "in": "query",
      "description": "Optionally specify a threshold of maximum market cap to filter results by.",
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
      "name": "volume_24h_min",
      "in": "query",
      "description": "Optionally specify a threshold of minimum 24 hour USD volume to filter results by.",
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
      "name": "volume_24h_max",
      "in": "query",
      "description": "Optionally specify a threshold of maximum 24 hour USD volume to filter results by.",
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
      "name": "circulating_supply_min",
      "in": "query",
      "description": "Optionally specify a threshold of minimum circulating supply to filter results by.",
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
      "name": "circulating_supply_max",
      "in": "query",
      "description": "Optionally specify a threshold of maximum circulating supply to filter results by.",
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
      "name": "percent_change_24h_min",
      "in": "query",
      "description": "Optionally specify a threshold of minimum 24 hour percent change to filter results by.",
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
      "name": "percent_change_24h_max",
      "in": "query",
      "description": "Optionally specify a threshold of maximum 24 hour percent change to filter results by.",
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
      "description": "Optionally calculate market quotes in up to 120 currencies at once by passing a comma-separated list of cryptocurrency or fiat currency symbols. Each additional convert option beyond the first requires an additional call credit. Each conversion is returned in its own \"quote\" object.",
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
      "description": "Optionally calculate market quotes by CoinMarketCap ID instead of symbol. This option is identical to `convert` outside of ID format. Ex: convert_id=1,2781 would replace convert=BTC,USD in your query. This parameter cannot be used when `convert` is used.",
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
      "name": "sort",
      "in": "query",
      "description": "What field to sort the list of cryptocurrencies by.",
      "required": false,
      "schema": {
        "type": "string",
        "default": "market_cap"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "sort_dir",
      "in": "query",
      "description": "The direction in which to order cryptocurrencies against the specified sort.",
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
      "name": "cryptocurrency_type",
      "in": "query",
      "description": "The type of cryptocurrency to include.",
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
      "name": "tag",
      "in": "query",
      "description": "The tag of cryptocurrency to include.",
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
      "description": "Optionally specify a comma-separated list of supplemental data fields to return. Pass num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply,market_cap_by_total_supply,volume_24h_reported,volume_7d,volume_7d_reported,volume_30d,volume_30d_reported,is_market_cap_included_in_calc to include all auxiliary fields.",
      "required": false,
      "schema": {
        "type": "string",
        "default": "num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply"
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
                    "type": "string"
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
                  "type": [
                    "number",
                    "null"
                  ],
                  "description": "Self-reported circulating supply",
                  "format": "bigdecimal"
                },
                "self_reported_market_cap": {
                  "type": [
                    "number",
                    "null"
                  ],
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
              "__$ref": "#/components/schemas/CryptoListingDTO"
            }
          }
        }
      ]
    }
  ]
}
```
