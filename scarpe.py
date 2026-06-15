import os, json
from playwright.sync_api import sync_playwright

# JS injected into each page to extract slug -> curl command from the rendered DOM.
# The curl code block is rendered client-side and never appears in window.DATA,
# so we scrape it directly from the DOM after the page finishes loading.
_EXTRACT_CURL_JS = """
() => {
    const results = {};
    const allCodes = document.querySelectorAll("code");
    const h2s = Array.from(document.querySelectorAll("h2[id]"));

    for (const code of allCodes) {
        const text = code.innerText.trim();
        if (!text.startsWith("curl --request") && !text.startsWith("curl --req")) continue;

        // Find the closest preceding h2[id] in document order
        let closestH2 = null;
        let closestDist = Infinity;
        for (const h2 of h2s) {
            const pos = h2.compareDocumentPosition(code);
            // Bit 4 (DOCUMENT_POSITION_FOLLOWING) means code comes after h2
            if (pos & 4) {
                const dist = code.getBoundingClientRect().top - h2.getBoundingClientRect().top;
                if (dist >= 0 && dist < closestDist) {
                    closestDist = dist;
                    closestH2 = h2;
                }
            }
        }
        if (closestH2) {
            results[closestH2.id] = text;
        }
    }
    return results;
}
"""


class Scraper:
    def __init__(
        self,
        output_dir="scraped_api_data",
        start_url="https://pro.coinmarketcap.com/api/documentation/pro-api-reference/cryptocurrency",
    ):
        self.output_dir = output_dir
        self.start_url = start_url

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _extract_curl_commands(self, page) -> dict:
        """
        Extract all slug -> curl_command mappings from the current rendered page.
        Returns a dict like { "coinmarketcap-id-map": "curl --request GET ...", ... }
        """
        try:
            return page.evaluate(_EXTRACT_CURL_JS) or {}
        except Exception as e:
            print(f"   ⚠️  Could not extract curl commands: {e}")
            return {}

    def _inject_curl_into_data(self, data: dict, curl_map: dict) -> dict:
        """
        Walk window.DATA and inject the curl_command string into every operation
        that has a matching slug.  The slug is stored in the 'slug' field of each
        operation inside queries[3].state.data.schema.tag.operations[].
        """
        if not curl_map or not isinstance(data, dict):
            return data

        queries = data.get("queries", [])
        for query in queries:
            state = query.get("state", {})
            qdata = state.get("data")
            if not isinstance(qdata, dict):
                continue
            schema = qdata.get("schema", {})
            if not isinstance(schema, dict):
                continue
            tag = schema.get("tag", {})
            if not isinstance(tag, dict):
                continue
            operations = tag.get("operations", [])
            if not isinstance(operations, list):
                continue

            for op in operations:
                if not isinstance(op, dict):
                    continue
                slug = op.get("slug", "")
                if slug and slug in curl_map:
                    op["curl_command"] = curl_map[slug]

        return data

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def scrape(self, start_url=None):
        """
        Discovers documentation URLs, extracts window.DATA from each page,
        enriches it with curl_command fields scraped from the rendered DOM,
        and saves the result as JSON files.
        """
        url = start_url or self.start_url
        os.makedirs(self.output_dir, exist_ok=True)

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()

            print(f"🌍 Loading initial page: {url}")
            page.goto(url, wait_until="networkidle")

            api_links = sorted(
                {
                    u
                    for u in page.evaluate(
                        "() => Array.from(document.querySelectorAll('a'), a => a.href)"
                    )
                    if u and "pro-api-reference" in u
                }
            )
            print(f"✅ Found {len(api_links)} API reference sections. Scraping...")

            for link in api_links:
                print(f"Scraping: {link}")
                # wait_until='networkidle' ensures JS has fully resolved all queries
                page.goto(link, wait_until="networkidle")

                data = page.evaluate("window.DATA")
                if data:
                    # Extract curl commands from the rendered DOM and inject them
                    curl_map = self._extract_curl_commands(page)
                    if curl_map:
                        print(f"   -> 🔗 Found {len(curl_map)} curl command(s)")
                        data = self._inject_curl_into_data(data, curl_map)

                    filepath = os.path.join(
                        self.output_dir, f"{link.strip('/').split('/')[-1]}.json"
                    )
                    with open(filepath, "w", encoding="utf-8") as f:
                        json.dump(data, f, indent=4)
                    print(f"   -> Saved to {filepath}")
                else:
                    print(f"   -> ⚠️ Warning: Could not find window.DATA on {link}")

            browser.close()
            print("\n🎉 All sections scraped successfully!")

    def __call__(self, start_url=None):
        """Allows calling the scraper object directly: scraper(url)."""
        return self.scrape(start_url)


if __name__ == "__main__":
    from paths import SCRAPED_JSON_DIR

    scraper = Scraper(output_dir=str(SCRAPED_JSON_DIR))
    scraper("https://pro.coinmarketcap.com/api/documentation/pro-api-reference/cryptocurrency")
