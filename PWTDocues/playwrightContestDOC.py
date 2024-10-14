import asyncio

from playwright.async_api import async_playwright


async def main():

    async with async_playwright() as playwright:
        # browser= await playwright.firefox.launch()
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://localhost:8000/")
        await page.wait_for_timeout(5000)
        await browser.close()


async def main3():
    async with async_playwright() as playwright:
        # Ignore self-signed certificate issues)
        api_request_context = await playwright.request.new_context(
            base_url="http://localhost:8000", ignore_https_errors=True
        )

        # Now, you can send requests relative to the base_url
        # This will request http://localhost:3000/bar.html
        response = await api_request_context.get("lucky/numbers2")
        text = await response.text()

        print(text[len(text) - 8: len(text) - 6])

        # Close the context when done
        await api_request_context.dispose()


async def main2():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context(viewport={"width": 900, "height": 1600})
        page = await context.new_page()

        await page.goto("https://localhost:8000/")
        await page.wait_for_timeout(100000)


#       await browser.close()


async def othermain():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context(viewport={"width": 100, "height": 900})
        page = await context.new_page()

        await page.goto("https://localhost:8000/")
        await page.wait_for_timeout(100000)


asyncio.run(main())
