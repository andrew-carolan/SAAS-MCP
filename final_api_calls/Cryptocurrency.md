Cryptocurrency
Method: GET
URL: /pro-api-reference/cryptocurrency
Description: Get cryptocurrency data.
Parameters:
- path (string): Path to navigate within the category
- label (string): Label for the item in the navigation menu
- badge (object): Badge for the item, including label, color, and invert status
- type (string): Type of the link or category
- items (array): Array of sub-items under a category
JSON Response Example:
```json
[
  {
    "type": "link",
    "label": "Airdrop",
    "to": "/pro-api-reference/cryptocurrency#airdrop",
    "badge": {
      "label": "get",
      "color": "green",
      "invert": true
    }
  },
  ...
]
```

---

--- ENDPOINT START: Exchange ---
Exchange
Method: GET
URL: /pro-api-reference/exchange
Description: Get exchange data.
Parameters:
- path (string): Path to navigate within the category
- label (string): Label for the item in the navigation menu
- badge (object): Badge for the item, including label, color, and invert status
- type (string): Type of the link or category
- items (array): Array of sub-items under a category
JSON Response Example:
```json
[
  {
    "type": "link",
    "label": "Metadata",
    "to": "/pro-api-reference/exchange#metadata",
    "badge": {
      "label": "get",
      "color": "green",
      "invert": true
    }
  },
  ...
]
```

---

--- ENDPOINT START: Global Metrics ---
Global Metrics
Method: GET
URL: /pro-api-reference/global-metrics
Description: Get global metrics data.
Parameters:
- path (string): Path to navigate within the category
- label (string): Label for the item in the navigation menu
- badge (object): Badge for the item, including label, color, and invert status
- type (string): Type of the link or category
- items (array): Array of sub-items under a category
JSON Response Example:
```json
[
  {
    "type": "link",
    "label": "CMC Crypto Fear and Greed Latest",
    "to": "/pro-api-reference/global-metrics#cmc-crypto-fear-and-greed-latest",
    "badge": {
      "label": "get",
      "color": "green",
      "invert": true
    }
  },
  ...
]
```

---