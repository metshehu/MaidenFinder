import asyncio

from pyppeteer import launch


async def main():
    browser = await launch()
    page = await browser.newPage()
    # await page.goto("https://quotes.toscrape.com/")

    await page.goto("https://www.instagram.com/mandyyliuu/")

    await page.waitForSelector("header section")
    # Get Title
    img_elements = await page.querySelectorAll("img")

    # Get the src attribute of the 2nd and 3rd img elements
    img_src_2 = await (await img_elements[1].getProperty("src")).jsonValue()
    img_src_3 = await (await img_elements[2].getProperty("src")).jsonValue()

    #    img_element = await page.querySelector("img")
    #    img_src = await (await img_element.getProperty("src")).jsonValue()

    title_html = await page.querySelector("h2")
    title = await (await title_html.getProperty("textContent")).jsonValue()

    print("src1 -> ", img_src_2)
    print("-" * 100)
    print("src2 -> ", img_src_3)
    print("title:", title)

    browser2 = await launch()
    page2 = await browser2.newPage()
    x = 0
    for i in img_elements[:20]:
        cImg = await (await i.getProperty("src")).jsonValue()
        await page2.goto(cImg)
        await page2.waitFor(1000)
        text = "test" + str(x)+".png"
        await page2.screenshot({"path": text})
        x += 1


asyncio.get_event_loop().run_until_complete(main())
