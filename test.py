import asyncio

from pyppeteer import launch


async def scrape_wikipedia():
    # Launch a headless browser

    browser = await launch()
    page = await browser.newPage()

    # Navigate to the Wikipedia page on History
    await page.goto("https://en.wikipedia.org/wiki/History")

    # Wait for the main content section to load
    await page.waitForSelector("#mw-content-text")

    # Extract the content
    content = await page.evaluate(
        """() => {
        // Select the main content area
        let mainContent = document.querySelector('#mw-content-text');
        return mainContent.innerText;
    }"""
    )

    # Print the extracted content
    print(content)

    # Optionally, save the content to a file
    with open("wikipedia_history.txt", "w", encoding="utf-8") as f:
        f.write(content)

    # Close the browser
    await browser.close()


# Run the scraping function
asyncio.get_event_loop().run_until_complete(scrape_wikipedia())
