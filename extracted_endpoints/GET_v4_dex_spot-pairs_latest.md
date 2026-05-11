# GET /v4/dex/spot-pairs/latest

**Summary:** Pairs Listings Latest

**Description:** Returns a paginated list of all active dex spot pairs with latest market data. Use the "convert" option to return market values in multiple fiat and cryptocurrency conversions in the same call.

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **network_id** (query) - *Optional*: One or more comma-separated CoinMarketCap cryptocurrency network ids.
- **network_slug** (query) - *Optional*: Alternatively, one or more comma-separated network names in URL friendly shorthand slug format (all lowercase, spaces replaced with hyphens). At least one id or slug is required.
- **dex_id** (query) - *Optional*: One or more comma-separated CoinMarketCap dex exchange ids
- **dex_slug** (query) - *Optional*: Alternatively, one or more comma-separated dex exchange names in URL friendly shorthand slug format (all lowercase, spaces replaced with hyphens). At least one id or slug is required.
- **base_asset_id** (query) - *Optional*: One or more comma-separated CoinMarketCap cryptocurrency ids.
- **base_asset_symbol** (query) - *Optional*: Alternatively, one or more comma-separated network symbol in URL friendly shorthand slug format (all lowercase, spaces replaced with hyphens).At least one id or slug is required.
- **base_asset_contract_address** (query) - *Optional*: Alternatively, one base asset contract address in URL friendly shorthand slug format (all lowercase, spaces replaced with hyphens).At least one id or slug is required.
- **base_asset_ucid** (query) - *Optional*: One or more comma-separated CoinMarketCap cryptocurrency IDs.
- **quote_asset_id** (query) - *Optional*: One or more comma-separated CoinMarketCap cryptocurrency ids.
- **quote_asset_symbol** (query) - *Optional*: Alternatively, one or more comma-separated network symbol in URL friendly shorthand slug format (all lowercase, spaces replaced with hyphens). At least one id or slug is required.
- **quote_asset_contract_address** (query) - *Optional*: Alternatively, one quote asset contract address in URL friendly shorthand slug format (all lowercase, spaces replaced with hyphens). At least one id or slug is required.
- **quote_asset_ucid** (query) - *Optional*: One or more comma-separated CoinMarketCap cryptocurrency IDs.
- **scroll_id** (query) - *Optional*: After your initial query, the API responds with the initial set of results and a scroll_ids. To retrieve the next set of results, provide this scroll_id of the last JSON with your follow-up request. scroll_id is an alternative to traditional pagination techniques.
- **limit** (query) - *Optional*: Optionally specify the number of results to return. Use this parameter and the start parameter to determine your own pagination size.
- **liquidity_min** (query) - *Optional*: Optionally specify a threshold of minimum liquidity to filter results by.
- **liquidity_max** (query) - *Optional*: Optionally specify a threshold of maximum liquidity to filter results by.
- **volume_24h_min** (query) - *Optional*: Optionally specify a threshold of minimum 24 hour USD volume to filter results by.
- **volume_24h_max** (query) - *Optional*: Optionally specify a threshold of maximum 24 hour USD volume to filter results by.
- **no_of_transactions_24h_min** (query) - *Optional*: Optionally specify a threshold of minimum 24h no. of transactions to filter results by.
- **no_of_transactions_24h_max** (query) - *Optional*: Optionally specify a threshold of maximum 24h no. of transactions to filter results by.
- **percent_change_24h_min** (query) - *Optional*: Optionally specify a threshold of minimum 24 hour percent change to filter results by.
- **percent_change_24h_max** (query) - *Optional*: Optionally specify a threshold of maximum 24 hour percent change to filter results by.
- **sort** (query) - *Optional*: Default:`"volume_24h"`
Valid values:  `"volume_24h"` `"liquidity"` `"no_of_transactions_24h"` `"percent_change_24h"` // todo
Sort the list of dex spot pairs by.
- **sort_dir** (query) - *Optional*: Default:`"desc"`
Valid values: `"desc"` `"asc"`
The direction in which to order dex spot pairs against the specified sort.
- **aux** (query) - *Optional*: Default:`""`
Valid values: `"pool_created"` `"percent_pooled_base_asset"` `"num_transactions_24h"` `"pool_base_asset"` `"pool_quote_asset"` `"24h_volume_quote_asset"` `"total_supply_quote_asset"` `"total_supply_base_asset"` `"holders"` `"buy_tax"` `"sell_tax"` `"security_scan"` `"24h_no_of_buys"` `"24h_no_of_sells"` `"24h_buy_volume"` `"24h_sell_volume"`
Optionally specify a comma-separated list of supplemental data fields to return.
- **reverse_order** (query) - *Optional*: Pass true to invert the order of a spot pair. For example, a trading pair is set up as Token B/Token A in the contract and is commonly referred to as Token A/Token B. Using reverse_order would change the order to reflect the true Token B/Token A pairing as it exists in the pool.
- **convert_id** (query) - *Optional*: Optionally calculate market quotes by CoinMarketCap ID instead of symbol. This option is identical to convert outside of ID format. Ex: convert_id=1,2781 would replace convert=BTC,USD in your query. This parameter cannot be used when convert is used.

### Raw Data

```json
{
  "slug": "pairs-listings-latest",
  "summary": "Pairs Listings Latest",
  "method": "get",
  "description": "Returns a paginated list of all active dex spot pairs with latest market data. Use the \"convert\" option to return market values in multiple fiat and cryptocurrency conversions in the same call.",
  "operationId": "getSpotPairsLatest",
  "contentTypes": [],
  "path": "/v4/dex/spot-pairs/latest",
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
      "name": "network_id",
      "in": "query",
      "description": "One or more comma-separated CoinMarketCap cryptocurrency network ids.",
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
      "name": "network_slug",
      "in": "query",
      "description": "Alternatively, one or more comma-separated network names in URL friendly shorthand slug format (all lowercase, spaces replaced with hyphens). At least one id or slug is required.",
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
      "name": "dex_id",
      "in": "query",
      "description": "One or more comma-separated CoinMarketCap dex exchange ids",
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
      "name": "dex_slug",
      "in": "query",
      "description": "Alternatively, one or more comma-separated dex exchange names in URL friendly shorthand slug format (all lowercase, spaces replaced with hyphens). At least one id or slug is required.",
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
      "name": "base_asset_id",
      "in": "query",
      "description": "One or more comma-separated CoinMarketCap cryptocurrency ids.",
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
      "name": "base_asset_symbol",
      "in": "query",
      "description": "Alternatively, one or more comma-separated network symbol in URL friendly shorthand slug format (all lowercase, spaces replaced with hyphens).At least one id or slug is required.",
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
      "name": "base_asset_contract_address",
      "in": "query",
      "description": "Alternatively, one base asset contract address in URL friendly shorthand slug format (all lowercase, spaces replaced with hyphens).At least one id or slug is required.",
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
      "name": "base_asset_ucid",
      "in": "query",
      "description": "One or more comma-separated CoinMarketCap cryptocurrency IDs.",
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
      "name": "quote_asset_id",
      "in": "query",
      "description": "One or more comma-separated CoinMarketCap cryptocurrency ids.",
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
      "name": "quote_asset_symbol",
      "in": "query",
      "description": "Alternatively, one or more comma-separated network symbol in URL friendly shorthand slug format (all lowercase, spaces replaced with hyphens). At least one id or slug is required.",
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
      "name": "quote_asset_contract_address",
      "in": "query",
      "description": "Alternatively, one quote asset contract address in URL friendly shorthand slug format (all lowercase, spaces replaced with hyphens). At least one id or slug is required.",
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
      "name": "quote_asset_ucid",
      "in": "query",
      "description": "One or more comma-separated CoinMarketCap cryptocurrency IDs.",
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
      "name": "scroll_id",
      "in": "query",
      "description": "After your initial query, the API responds with the initial set of results and a scroll_ids. To retrieve the next set of results, provide this scroll_id of the last JSON with your follow-up request. scroll_id is an alternative to traditional pagination techniques.",
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
      "name": "limit",
      "in": "query",
      "description": "Optionally specify the number of results to return. Use this parameter and the start parameter to determine your own pagination size.",
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
      "name": "liquidity_min",
      "in": "query",
      "description": "Optionally specify a threshold of minimum liquidity to filter results by.",
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
      "name": "liquidity_max",
      "in": "query",
      "description": "Optionally specify a threshold of maximum liquidity to filter results by.",
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
      "name": "no_of_transactions_24h_min",
      "in": "query",
      "description": "Optionally specify a threshold of minimum 24h no. of transactions to filter results by.",
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
      "name": "no_of_transactions_24h_max",
      "in": "query",
      "description": "Optionally specify a threshold of maximum 24h no. of transactions to filter results by.",
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
      "name": "sort",
      "in": "query",
      "description": "Default:`\"volume_24h\"`\nValid values:  `\"volume_24h\"` `\"liquidity\"` `\"no_of_transactions_24h\"` `\"percent_change_24h\"` // todo\nSort the list of dex spot pairs by.",
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
      "name": "sort_dir",
      "in": "query",
      "description": "Default:`\"desc\"`\nValid values: `\"desc\"` `\"asc\"`\nThe direction in which to order dex spot pairs against the specified sort.",
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
      "description": "Default:`\"\"`\nValid values: `\"pool_created\"` `\"percent_pooled_base_asset\"` `\"num_transactions_24h\"` `\"pool_base_asset\"` `\"pool_quote_asset\"` `\"24h_volume_quote_asset\"` `\"total_supply_quote_asset\"` `\"total_supply_base_asset\"` `\"holders\"` `\"buy_tax\"` `\"sell_tax\"` `\"security_scan\"` `\"24h_no_of_buys\"` `\"24h_no_of_sells\"` `\"24h_buy_volume\"` `\"24h_sell_volume\"`\nOptionally specify a comma-separated list of supplemental data fields to return.",
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
      "name": "reverse_order",
      "in": "query",
      "description": "Pass true to invert the order of a spot pair. For example, a trading pair is set up as Token B/Token A in the contract and is commonly referred to as Token A/Token B. Using reverse_order would change the order to reflect the true Token B/Token A pairing as it exists in the pool.",
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
      "description": "Optionally calculate market quotes by CoinMarketCap ID instead of symbol. This option is identical to convert outside of ID format. Ex: convert_id=1,2781 would replace convert=BTC,USD in your query. This parameter cannot be used when convert is used.",
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
                "quote": {
                  "type": "array",
                  "description": "A map of market quotes in different currency conversions. The default map included is USD.",
                  "items": {
                    "type": "object",
                    "properties": {
                      "price": {
                        "type": "number",
                        "description": "Price in the specified currency for this spot pair.",
                        "format": "bigdecimal"
                      },
                      "liquidity": {
                        "type": "number",
                        "description": "Total liquidity available currently in the specified currency. This field will return null if not available.",
                        "format": "bigdecimal"
                      },
                      "convert_id": {
                        "type": "string",
                        "description": "id of specified currency."
                      },
                      "price_by_quote_asset": {
                        "type": "number",
                        "description": "Price of the base asset in quote asset for this spot pair.",
                        "format": "bigdecimal"
                      },
                      "last_updated": {
                        "type": "string",
                        "description": "Timestamp (ISO 8601) of when the conversion currency's current value was referenced for this conversion.",
                        "format": "date-time"
                      },
                      "volume_24h": {
                        "type": "number",
                        "description": "Reported 24 hour volume in the specified spot pair in the specified currency.",
                        "format": "bigdecimal"
                      },
                      "percent_change_price_1h": {
                        "type": "number",
                        "description": "1 hour price change percentage in the specified spot pair in the specified currency.",
                        "format": "bigdecimal"
                      },
                      "percent_change_price_24h": {
                        "type": "number",
                        "description": "24 hour price change percentage in the specified spot pair in the specified currency.",
                        "format": "bigdecimal"
                      },
                      "fully_diluted_value": {
                        "type": "number",
                        "description": "Fully Diluted Value = (Total Supply - Burned Supply) * Price. Returned in the specified currency.",
                        "format": "bigdecimal"
                      },
                      "24h_buy_volume": {
                        "type": "number",
                        "description": "24 hours buy volume of the asset",
                        "format": "bigdecimal"
                      },
                      "24h_sell_volume": {
                        "type": "number",
                        "description": "24 hours sell volume of the asset",
                        "format": "bigdecimal"
                      }
                    },
                    "description": "A map of market quotes in different currency conversions. The default map included is USD.",
                    "__$ref": "#/components/schemas/DexQuoteDTO"
                  }
                },
                "contract_address": {
                  "type": "string",
                  "description": "The unique contract address for this spot pair."
                },
                "name": {
                  "type": "string",
                  "description": "The name of this spot pair."
                },
                "base_asset_id": {
                  "type": "string",
                  "description": "The id of this base asset in the spot pair."
                },
                "base_asset_ucid": {
                  "type": "string",
                  "description": "The ucid of this base asset in the spot pair."
                },
                "base_asset_name": {
                  "type": "string",
                  "description": "The name of this base asset in the spot pair."
                },
                "base_asset_symbol": {
                  "type": "string",
                  "description": "The symbol of this base asset in the spot pair."
                },
                "base_asset_contract_address": {
                  "type": "string",
                  "description": "The contract addres of this base asset in the spot pair."
                },
                "quote_asset_id": {
                  "type": "string",
                  "description": "The id of this quote asset in the spot pair."
                },
                "quote_asset_ucid": {
                  "type": "string",
                  "description": "The ucid of this quote asset in the spot pair."
                },
                "quote_asset_name": {
                  "type": "string",
                  "description": "The name of this quote asset in the spot pair."
                },
                "quote_asset_symbol": {
                  "type": "string",
                  "description": "The symbol of this quote asset in the spot pair."
                },
                "quote_asset_contract_address": {
                  "type": "string",
                  "description": "The contract addresss of this quote asset in the spot pair."
                },
                "dex_id": {
                  "type": "string",
                  "description": "The id of this dex the spot pair is on."
                },
                "dex_slug": {
                  "type": "string",
                  "description": "The name of this dex the spot pair is on."
                },
                "network_id": {
                  "type": "string",
                  "description": "The id of the network the spot pair is on."
                },
                "network_slug": {
                  "type": "string",
                  "description": "The slug of the network the spot pair is on."
                },
                "last_updated": {
                  "type": "string",
                  "description": "Timestamp (ISO 8601) of the last time this record was updated.",
                  "format": "date-time"
                },
                "created_at": {
                  "type": "string",
                  "description": "Timestamp (ISO 8601) when we started tracking this asset.",
                  "format": "date-time"
                },
                "num_transactions_24h": {
                  "type": "integer",
                  "description": "Number of transactions in past 24 hours",
                  "format": "int64"
                },
                "holders": {
                  "type": "integer",
                  "description": "Number of holders of the asset",
                  "format": "int64"
                },
                "24h_no_of_buys": {
                  "type": "integer",
                  "description": "Number of asset buys in the past 24 hours",
                  "format": "int64"
                },
                "24h_no_of_sells": {
                  "type": "integer",
                  "description": "Number of asset sells in the past 24 hours",
                  "format": "int64"
                },
                "pool_created": {
                  "type": "string",
                  "description": "When the pool of the asset was created",
                  "format": "date-time"
                },
                "buy_tax": {
                  "type": "number",
                  "description": "Buy tax on the asset",
                  "format": "bigdecimal"
                },
                "sell_tax": {
                  "type": "number",
                  "description": "Sell tax on the asset",
                  "format": "bigdecimal"
                },
                "security_scan": {
                  "type": "array",
                  "description": "Security scan by Go+.\n\n\nAll infomation and data relating to contract detection are based on public third party information. CoinMarketCap does not confirm or verify the accuracy or timeliness of such information and data.\n\nCoinMarketCap shall have no responsibility or liability for the accuracy of data, nor have the duty to review, confirm, verify or otherwise perform any inquiry or investigation as to the completeness, accuracy, sufficiency, integrity, reliability or timeliness of any such information or data provided.\n\nOnly returned if passed in aux.",
                  "items": {
                    "type": "object",
                    "properties": {
                      "third_party": {
                        "type": "object",
                        "properties": {
                          "open_source": {
                            "type": "boolean"
                          },
                          "proxy": {
                            "type": "boolean"
                          },
                          "mintable": {
                            "type": "boolean"
                          },
                          "can_take_back_ownership": {
                            "type": "boolean"
                          },
                          "owner_change_balance": {
                            "type": "boolean"
                          },
                          "hidden_owner": {
                            "type": "boolean"
                          },
                          "self_destruct": {
                            "type": "boolean"
                          },
                          "external_call": {
                            "type": "boolean"
                          },
                          "cannot_buy": {
                            "type": "boolean"
                          },
                          "cannot_sell_all": {
                            "type": "boolean"
                          },
                          "slippage_modifiable": {
                            "type": "boolean"
                          },
                          "honeypot": {
                            "type": "boolean"
                          },
                          "transfer_pausable": {
                            "type": "boolean"
                          },
                          "blacklisted": {
                            "type": "boolean"
                          },
                          "whitelisted": {
                            "type": "boolean"
                          },
                          "in_dex": {
                            "type": "boolean"
                          },
                          "anti_whale": {
                            "type": "boolean"
                          },
                          "anti_whale_modifiable": {
                            "type": "boolean"
                          },
                          "trading_cool_down": {
                            "type": "boolean"
                          },
                          "personal_slippage_modifiable": {
                            "type": "boolean"
                          },
                          "trust_list": {
                            "type": "boolean"
                          },
                          "true_token": {
                            "type": "boolean"
                          },
                          "airdrop_scam": {
                            "type": "boolean"
                          }
                        },
                        "__$ref": "#/components/schemas/SecurityScan3rdResult"
                      },
                      "aggregated": {
                        "type": "object",
                        "properties": {
                          "contract_verified": {
                            "type": "boolean"
                          },
                          "honeypot": {
                            "type": "boolean"
                          }
                        },
                        "__$ref": "#/components/schemas/SecurityScanAggregatedResult"
                      }
                    },
                    "description": "Security scan by Go+.\n\n\nAll infomation and data relating to contract detection are based on public third party information. CoinMarketCap does not confirm or verify the accuracy or timeliness of such information and data.\n\nCoinMarketCap shall have no responsibility or liability for the accuracy of data, nor have the duty to review, confirm, verify or otherwise perform any inquiry or investigation as to the completeness, accuracy, sufficiency, integrity, reliability or timeliness of any such information or data provided.\n\nOnly returned if passed in aux.",
                    "__$ref": "#/components/schemas/SecurityScanResult"
                  }
                },
                "pool_base_asset": {
                  "type": "number",
                  "description": "Base asset in the pool",
                  "format": "bigdecimal"
                },
                "pool_quote_asset": {
                  "type": "number",
                  "description": "Quote asset in the pool",
                  "format": "bigdecimal"
                },
                "percent_pooled_base_asset": {
                  "type": "number",
                  "description": "Percentage of the base asset in the pool",
                  "format": "bigdecimal"
                },
                "24h_volume_quote_asset": {
                  "type": "number",
                  "description": "24 hours volume of the quote asset",
                  "format": "bigdecimal"
                },
                "total_supply_quote_asset": {
                  "type": "number",
                  "description": "Total supply of the quote asset",
                  "format": "bigdecimal"
                },
                "total_supply_base_asset": {
                  "type": "number",
                  "description": "Total supply of the quote asset",
                  "format": "bigdecimal"
                },
                "date_launched": {
                  "type": "string",
                  "description": "Timestamp (ISO 8601) of the launch date for this exchange.",
                  "format": "date-time"
                },
                "scroll_id": {
                  "type": "string",
                  "description": "A unique identifier used to fetch the next batch of results from the next API related API call, if applicable. scroll_id is an alternative to traditional pagingation techniques."
                }
              },
              "__$ref": "#/components/schemas/DexSpotPairDTO"
            }
          }
        }
      ]
    }
  ]
}
```
