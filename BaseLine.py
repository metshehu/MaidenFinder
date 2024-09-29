import asyncio

from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        # Launching the browser with user data directory and without headless mode
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # Go to Instagram page
        await page.goto("https://www.instagram.com/xblertaaa/")

        # Set viewport size
        await page.set_viewport_size({"width": 1600, "height": 900})

        # Wait for 10 seconds
        await page.wait_for_timeout(10000)

        # Select all img elements
        img_elements = await page.query_selector_all("img")

        # Open a new page for downloading images
        page2 = await context.new_page()
        name_n = 0
        starting_text = "playWrite.testthicBitch"

        # Loop through selected images from the 6th to the 20th
        for img in img_elements[5:20]:
            cImg = await img.get_attribute("src")
            if name_n == 0:
                print(str(img))
            await page2.goto(cImg)
            path = f"{starting_text}{name_n}.png"
            await page2.screenshot(path=path)
            name_n += 1

        await browser.close()


asyncio.run(main())
