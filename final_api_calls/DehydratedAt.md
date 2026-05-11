{
  "name": "DehydratedAt",
  "method": "Query",
  "url": "/__zuplo/docs/dehydratedAt",
  "description": "Retrieve the dehydrated at timestamp for a specific query key.",
  "parameters": [
    {
      "name": "queryKey",
      "type": "string"
    }
  ],
  "curlExample": "curl -X GET \"/__zuplo/docs/dehydratedAt?queryKey=[\"queryKey\"]\"",
  "jsonResponseExample": "{\"dataUpdateCount\":0,\"dataUpdatedAt\":0,\"error\":null,\"errorUpdateCount\":0,\"errorUpdatedAt\":0,\"fetchFailureCount\":0,\"fetchFailureReason\":null,\"fetchMeta\":null,\"isInvalidated\":false,\"status\":\"pending\",\"fetchStatus\":\"idle\"}"
}