import os
import json
import asyncio
from playwright.async_api import async_playwright

async def get_doc_urls(browser, start_url):
    """Function 1: Pulls all relevant documentation URLs from the page."""
    print(f"Finding links on: {start_url}")
    page = await browser.new_page()
    try:
        await page.goto(start_url, wait_until="networkidle", timeout=60000)
        # Find links that are part of the pro-api-reference
        urls = await page.evaluate("""
            () => Array.from(document.querySelectorAll('a'))
                .map(a => a.href)
                .filter(href => href.includes('pro-api-reference/'))
        """)
        unique_urls = sorted(list(set(urls)))
        return unique_urls
    finally:
        await page.close()

async def scrape_json_to_folder(browser, urls, output_dir="scraped_json"):
    """Function 2: Pulls window.DATA from each page and saves it to a folder."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    semaphore = asyncio.Semaphore(5) # Limit to 5 concurrent pages for speed + stability

    async def scrape_single_page(url):
        async with semaphore:
            page = await browser.new_page()
            try:
                print(f"  --> Scraping: {url}")
                await page.goto(url, wait_until="networkidle", timeout=60000)
                
                # Grab the actual structured data object
                raw_json_str = await page.evaluate("() => window.DATA ? JSON.stringify(window.DATA) : null")
                
                if raw_json_str:
                    # Clean the URL to make a filename (e.g. .../exchange#metadata -> exchange_metadata)
                    slug = url.rstrip('/').split('/')[-1].replace('#', '_').split('?')[0] or "overview"
                    path = os.path.join(output_dir, f"{slug}.json")
                    
                    data = json.loads(raw_json_str)
                    with open(path, 'w') as f:
                        json.dump(data, f, indent=4)
                    print(f"      [✓] Saved {slug}.json")
                else:
                    print(f"      [!] No window.DATA found on {url}")
            except Exception as e:
                print(f"      [X] Error on {url}: {e}")
            finally:
                await page.close()

    # Run all scrapes concurrently
    tasks = [scrape_single_page(url) for url in urls]
    await asyncio.gather(*tasks)

async def main():
    target_url = "https://coinmarketcap.com/api/documentation/pro-api-reference/endpoint-overview"
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        # 1. Get the URLs
        urls = await get_doc_urls(browser, target_url)
        print(f"Found {len(urls)} documentation pages.\n")
        
        # 2. Scrape and save
        if urls:
            await scrape_json_to_folder(browser, urls)
        
        await browser.close()
    
    print(f"\nDone! All files are in the 'scraped_json/' directory.")

if __name__ == "__main__":
    asyncio.run(main())
