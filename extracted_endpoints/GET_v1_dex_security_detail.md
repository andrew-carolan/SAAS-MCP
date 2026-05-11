# GET /v1/dex/security/detail

**Summary:** Get security detail

**Description:** Get security audit information for a token

### Parameters

- **X-CMC_PRO_API_KEY** (header) - *Required*: Your CoinMarketCap Pro API key
- **platformName** (query) - *Optional*: Platform name
- **address** (query) - *Optional*: Token address

### Raw Data

```json
{
  "slug": "get-security-detail",
  "summary": "Get security detail",
  "method": "get",
  "description": "Get security audit information for a token",
  "operationId": "getSecurityDetail",
  "contentTypes": [],
  "path": "/v1/dex/security/detail",
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
      "name": "platformName",
      "in": "query",
      "description": "Platform name",
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
      "name": "address",
      "in": "query",
      "description": "Token address",
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
                "platformName": {
                  "type": "string",
                  "description": "Platform name",
                  "example": "ethereum"
                },
                "platformId": {
                  "type": "integer",
                  "description": "Platform ID",
                  "format": "int32",
                  "example": 1
                },
                "tokenContractAddress": {
                  "type": "string",
                  "description": "Token contract address",
                  "example": "0xabc123..."
                },
                "securityLevel": {
                  "type": "string",
                  "description": "Overall security level"
                },
                "categoryLevel": {
                  "type": "string",
                  "description": "Overall category level"
                },
                "securityBatchLevel": {
                  "type": "integer",
                  "description": "Overall security batch level",
                  "format": "int32"
                },
                "extra": {
                  "type": "object",
                  "properties": {
                    "buyTax": {
                      "type": "string",
                      "description": "Buy tax"
                    },
                    "sellTax": {
                      "type": "string",
                      "description": "Sell tax"
                    },
                    "isFlaggedByVendor": {
                      "type": "boolean",
                      "description": "Whether the token is flagged by third-party security vendors",
                      "example": false
                    },
                    "isVerified": {
                      "type": "boolean",
                      "description": "Whether the token contract is verified",
                      "example": true
                    },
                    "isReported": {
                      "type": "boolean",
                      "description": "Whether the token has been reported by users or security platforms",
                      "example": false
                    },
                    "source": {
                      "type": "string",
                      "description": "Data source of the security information",
                      "example": "GoPlus"
                    }
                  },
                  "description": "Extra security metadata provided by external vendors or on-chain analysis",
                  "__$ref": "#/components/schemas/BnSecurityExtraInfoDTO"
                },
                "securityItems": {
                  "type": "array",
                  "description": "Detailed security items",
                  "items": {
                    "type": "object",
                    "properties": {
                      "code": {
                        "type": "string",
                        "description": "Rule code"
                      },
                      "riskCode": {
                        "type": "string",
                        "description": "Risk classification code"
                      },
                      "riskyLevel": {
                        "type": "string",
                        "description": "Risk level"
                      },
                      "isHit": {
                        "type": "boolean",
                        "description": "Whether the risk was hit",
                        "example": true
                      },
                      "order": {
                        "type": "integer",
                        "description": "Display order",
                        "format": "int32"
                      },
                      "des": {
                        "type": "string",
                        "description": "Risk description"
                      },
                      "groupId": {
                        "type": "string",
                        "description": "Group ID for categorization"
                      }
                    },
                    "description": "Detailed security item",
                    "__$ref": "#/components/schemas/SecurityItem"
                  }
                },
                "evmDisplay": {
                  "type": "object",
                  "properties": {
                    "honeypotStatus": {
                      "type": "string",
                      "description": "EVM - Honeypot status",
                      "example": "Safe"
                    },
                    "unverifiedContractStatus": {
                      "type": "string",
                      "description": "EVM - Unverified contract status",
                      "example": "Verified"
                    },
                    "mintableStatus": {
                      "type": "string",
                      "description": "Solana - Mintable token status",
                      "example": "Non-mintable"
                    },
                    "freezableStatus": {
                      "type": "string",
                      "description": "Solana - Freezable status",
                      "example": "Non-freezable"
                    },
                    "rugPullStatus": {
                      "type": "string",
                      "description": "Solana - Rug pull detection",
                      "example": "No risk"
                    },
                    "fakeTokenStatus": {
                      "type": "string",
                      "description": "Solana - Fake token detection",
                      "example": "Genuine"
                    }
                  },
                  "description": "Security item display flags for EVM or Solana",
                  "__$ref": "#/components/schemas/DisplayItem"
                },
                "solanaDisplay": {
                  "type": "object",
                  "properties": {
                    "honeypotStatus": {
                      "type": "string",
                      "description": "EVM - Honeypot status",
                      "example": "Safe"
                    },
                    "unverifiedContractStatus": {
                      "type": "string",
                      "description": "EVM - Unverified contract status",
                      "example": "Verified"
                    },
                    "mintableStatus": {
                      "type": "string",
                      "description": "Solana - Mintable token status",
                      "example": "Non-mintable"
                    },
                    "freezableStatus": {
                      "type": "string",
                      "description": "Solana - Freezable status",
                      "example": "Non-freezable"
                    },
                    "rugPullStatus": {
                      "type": "string",
                      "description": "Solana - Rug pull detection",
                      "example": "No risk"
                    },
                    "fakeTokenStatus": {
                      "type": "string",
                      "description": "Solana - Fake token detection",
                      "example": "Genuine"
                    }
                  },
                  "description": "Security item display flags for EVM or Solana",
                  "__$ref": "#/components/schemas/DisplayItem"
                },
                "exist": {
                  "type": "boolean",
                  "description": "token security exist"
                },
                "tags": {
                  "type": "array",
                  "description": "token security exist",
                  "items": {
                    "type": "string",
                    "description": "token security exist"
                  }
                }
              },
              "description": "Token security response",
              "__$ref": "#/components/schemas/TokenSecurityResponseDTO"
            }
          }
        }
      ]
    }
  ]
}
```
