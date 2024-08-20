import asyncio
import time

from pyppeteer import launch


async def scrape_instagram():

    browser = await launch()
    page = await browser.newPage()
    await page.goto("https://www.instagram.com/mandyyliuu/")

    # await page.goto("https://www.instagram.com/redonblakajj/")
    time.sleep(20)
    await page.waitForSelector("header section")
    # time.sleep(20)
    await page.screenshot({"path": "fyou.png"})
    page_html = await page.querySelector('span')
    title = page_html.getProperties("textContent")
    print("title", title)
    await browser.close()


asyncio.get_event_loop().run_until_complete(scrape_instagram())
