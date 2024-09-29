import asyncio

from pyppeteer import launch


async def scrape_wikipedia():
    browser = await launch({"args": ["--proxy-server=ip:port"], "headless": False})
    page = await browser.newPage()

    await page.goto("https://quotes.toscrape.com/")

    await page.setViewport({"width": 1600, "height": 900})
    await page.screenshot({"path": "testingggg2.png"})

    # Close the browser
    await browser.close()


# Run the scraping function
asyncio.get_event_loop().run_until_complete(scrape_wikipedia())
