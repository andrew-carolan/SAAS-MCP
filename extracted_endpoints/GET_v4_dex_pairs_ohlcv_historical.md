# GET /v4/dex/pairs/ohlcv/historical

**Summary:** OHLCV Historical

**Description:** Returns historical OHLCV (Open, High, Low, Close, Volume) data along with market cap for any spot pairs using time interval parameters.

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **contract_address** (query) - *Optional*: One contract address. Example:"0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640".
If network/dex/base asset/quote asset information is passed, contract address cannot be passed.
Note: contract_address is case sensitive for all non-EVM chains and not case sensitive for all EVM chains. EVM chains contract address addresses begin with 0x, and are followed by 40 alphanumeric characters(numerals and letters)
- **network_id** (query) - *Optional*: One or more CoinMarketCap cryptocurrency network ids
- **network_slug** (query) - *Optional*: Alternatively, one network names in URL friendly shorthand "slug" format (all lowercase, spaces replaced with hyphens).
- **time_period** (query) - *Optional*: Default:`"daily"`
Valid values: `"daily"` `"hourly"` `"1m"` `"5m"` `"15m"` `"4h"`
Time period to return OHLCV data for. If hourly, the open will be 01:00 and the close will be 01:59. If daily, the open will be 00:00:00 for the day and close will be 23:59:99 for the same day. See the main endpoint description for details.
- **time_start** (query) - *Optional*: Timestamp (Unix or ISO 8601) to start returning OHLCV time periods for. Only the date portion of the timestamp 
is used for daily OHLCV so it's recommended to send an ISO date format like "2018-09-19" without time.
- **time_end** (query) - *Optional*: Timestamp (Unix or ISO 8601) to stop returning OHLCV time periods for (inclusive). Optional, if not passed we'll default 
to the current time. Only the date portion of the timestamp is used for daily OHLCV so it's recommended to send an 
ISO date format like "2018-09-19" without time.
- **count** (query) - *Optional*: Optionally limit the number of time periods to return results for. The default is 10 items. The current query 
limit is 500 items.
- **interval** (query) - *Optional*: Default:`"daily"`
Valid values: `"1m"` `"5m"` `"15m"` `"30m"` `"1h"` `"4h"` `"8h"` `"12h"` `"daily"` `"weekly"` `"monthly"`
Optionally adjust the interval that "time_period" is sampled. For example with interval=monthly&time_period=daily you will see a daily OHLCV record for January, February, March and so on. See main endpoint description for available options.
- **aux** (query) - *Optional*: Default:`""`
Valid values: `"pool_created"` `"percent_pooled_base_asset"` `"num_transactions_24h"` `"pool_base_asset"` `"pool_quote_asset"` `"24h_volume_quote_asset"` `"total_supply_quote_asset"` `"total_supply_base_asset"` `"holders"` `"buy_tax"` `"sell_tax"` `"security_scan"` `"24h_no_of_buys"` `"24h_no_of_sells"` `"24h_buy_volume"` `"24h_sell_volume"`
Optionally specify a comma-separated list of supplemental data fields to return.
- **convert_id** (query) - *Optional*: Optionally calculate market quotes by CoinMarketCap ID instead of symbol. This option is identical to convert outside of ID format. Ex: convert_id=1,2781 would replace convert=BTC,USD in your query. This parameter cannot be used when convert is used.
- **skip_invalid** (query) - *Optional*: Pass true to relax request validation rules. When requesting records on multiple spot pairs an error is returned if no match is found for 1 or more requested spot pairs. If set to true, invalid lookups will be skipped allowing valid spot pairs to still be returned.
- **reverse_order** (query) - *Optional*: Pass true to invert the order of a spot pair. For example, a trading pair is set up as Token B/Token A in the contract and is commonly referred to as Token A/Token B. Using reverse_order would change the order to reflect the true Token B/Token A pairing as it exists in the pool.

### Raw Data

```json
{
  "slug": "ohlcv-historical-2",
  "summary": "OHLCV Historical",
  "method": "get",
  "description": "Returns historical OHLCV (Open, High, Low, Close, Volume) data along with market cap for any spot pairs using time interval parameters.",
  "operationId": "getPairsHistoricalOHLCV",
  "contentTypes": [],
  "path": "/v4/dex/pairs/ohlcv/historical",
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
      "name": "contract_address",
      "in": "query",
      "description": "One contract address. Example:\"0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640\".\nIf network/dex/base asset/quote asset information is passed, contract address cannot be passed.\nNote: contract_address is case sensitive for all non-EVM chains and not case sensitive for all EVM chains. EVM chains contract address addresses begin with 0x, and are followed by 40 alphanumeric characters(numerals and letters)",
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
      "name": "network_id",
      "in": "query",
      "description": "One or more CoinMarketCap cryptocurrency network ids",
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
      "description": "Alternatively, one network names in URL friendly shorthand \"slug\" format (all lowercase, spaces replaced with hyphens).",
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
      "name": "time_period",
      "in": "query",
      "description": "Default:`\"daily\"`\nValid values: `\"daily\"` `\"hourly\"` `\"1m\"` `\"5m\"` `\"15m\"` `\"4h\"`\nTime period to return OHLCV data for. If hourly, the open will be 01:00 and the close will be 01:59. If daily, the open will be 00:00:00 for the day and close will be 23:59:99 for the same day. See the main endpoint description for details.",
      "required": false,
      "schema": {
        "type": "string",
        "default": "daily"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "time_start",
      "in": "query",
      "description": "Timestamp (Unix or ISO 8601) to start returning OHLCV time periods for. Only the date portion of the timestamp \nis used for daily OHLCV so it's recommended to send an ISO date format like \"2018-09-19\" without time.",
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
      "name": "time_end",
      "in": "query",
      "description": "Timestamp (Unix or ISO 8601) to stop returning OHLCV time periods for (inclusive). Optional, if not passed we'll default \nto the current time. Only the date portion of the timestamp is used for daily OHLCV so it's recommended to send an \nISO date format like \"2018-09-19\" without time.",
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
      "name": "count",
      "in": "query",
      "description": "Optionally limit the number of time periods to return results for. The default is 10 items. The current query \nlimit is 500 items.",
      "required": false,
      "schema": {
        "type": "string",
        "default": "10"
      },
      "style": null,
      "explode": null,
      "allowReserved": null,
      "examples": []
    },
    {
      "name": "interval",
      "in": "query",
      "description": "Default:`\"daily\"`\nValid values: `\"1m\"` `\"5m\"` `\"15m\"` `\"30m\"` `\"1h\"` `\"4h\"` `\"8h\"` `\"12h\"` `\"daily\"` `\"weekly\"` `\"monthly\"`\nOptionally adjust the interval that \"time_period\" is sampled. For example with interval=monthly&time_period=daily you will see a daily OHLCV record for January, February, March and so on. See main endpoint description for available options.",
      "required": false,
      "schema": {
        "type": "string",
        "default": "daily"
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
    },
    {
      "name": "skip_invalid",
      "in": "query",
      "description": "Pass true to relax request validation rules. When requesting records on multiple spot pairs an error is returned if no match is found for 1 or more requested spot pairs. If set to true, invalid lookups will be skipped allowing valid spot pairs to still be returned.",
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
                "quotes": {
                  "type": "array",
                  "description": "Collection of historical OHLCV quotes for the DEX pair",
                  "items": {
                    "type": "object",
                    "properties": {
                      "quote": {
                        "type": "array",
                        "description": "A map of market quotes in different currency conversions. The default map included is USD.",
                        "items": {
                          "type": "object",
                          "properties": {
                            "open": {
                              "type": "number",
                              "description": "Price from first datapoint of today in UTC time for the convert option requested.",
                              "format": "bigdecimal"
                            },
                            "high": {
                              "type": "number",
                              "description": "Highest price so far today in UTC time for the convert option requested.",
                              "format": "bigdecimal"
                            },
                            "low": {
                              "type": "number",
                              "description": "Lowest price today in UTC time for the convert option requested.",
                              "format": "bigdecimal"
                            },
                            "close": {
                              "type": "number",
                              "description": "Latest price today in UTC time for the convert option requested. This is not the final price during close as the current day period is not over.",
                              "format": "bigdecimal"
                            },
                            "volume": {
                              "type": "number",
                              "description": "Adjusted volume for this time series interval.",
                              "format": "bigdecimal"
                            },
                            "convert_id": {
                              "type": "string",
                              "description": "id of specified currency."
                            },
                            "last_updated": {
                              "type": "string",
                              "description": "Timestamp (ISO 8601) of when the conversion currency's current value was referenced for this conversion."
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
                          "description": "DEX OHLCV (Open, High, Low, Close, Volume) quote data",
                          "__$ref": "#/components/schemas/DexOhlcvQuote"
                        }
                      },
                      "time_open": {
                        "type": "string",
                        "description": "Timestamp (ISO 8601) of the start of this OHLCV period.",
                        "format": "date-time"
                      },
                      "time_close": {
                        "type": "string",
                        "description": "Timestamp (ISO 8601) of the end of this OHLCV period. Always null as the current day is incomplete. See last_updated for the last UTC time included in the current OHLCV calculation.",
                        "format": "date-time"
                      }
                    },
                    "description": "Historical OHLCV quotes data",
                    "__$ref": "#/components/schemas/DexPairsOhlcvHistoricalQuotes"
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
                }
              },
              "description": "DEX pairs OHLCV historical data",
              "__$ref": "#/components/schemas/DexPairsOhlcvHistoricalDTO"
            }
          }
        }
      ]
    }
  ]
}
```
