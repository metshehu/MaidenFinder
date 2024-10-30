import asyncio

import aiofiles
from playwright.async_api import async_playwright

from Parsers import pageFollowers, pageParser

username = "michaeljohnsonth3@gmail.com"
password = "helloitsme1234"


async def loginPage(username, password, playWrightInstance, context):
    browser = await playWrightInstance.chromium.launch(headless=False)
    a = await context.new_page()

    # Navigate to Instagram login a
    await a.goto("https://www.instagram.com/accounts/login/")

    # Wait for the username and password fields to be visible
    await a.wait_for_selector("input[name='username']")
    await a.wait_for_selector("input[name='password']")

    # Fill in the username and password fields
    await a.fill("input[name='username']", username)
    await a.fill("input[name='password']", password)

    # Click the login button
    await a.click("button[type='submit']")
    await a.wait_for_timeout(10000)
    await a.goto("https://www.instagram.com/redonblakajj/")
    await a.wait_for_timeout(10000)

    return a


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        )
        a = await loginPage(username, password, p, context)
        # await a.goto("https://www.instagram.com/redonblakajj/")
        await a.wait_for_timeout(10000)
        html_content = await a.content()
        await a.goto("https://www.instagram.com/redonblakajj/followers/")
        # Save the HTML content to a file
        await a.wait_for_timeout(10000)
        html_content_followrs = await a.content()
        img_elements = await a.query_selector_all("img")

        # print(await pageParser(html_content))✅
        print(await pageFollowers(html_content_followrs)) 
        # Extract the 'src' attributes
        #img_srcs = [await img.get_attribute("src") for img in img_elements]

        # print(img_srcs)
        # Print the image 'src' links
        #with open("page_content.html", "w", encoding="utf-8") as file:
        #    file.write(html_content)
        #with open("page_contentFollowrs2.html", "w", encoding="utf-8") as file:
        #    file.write(html_content_followrs)
        # await a.goto("https://www.instagram.com/redonblakajj/followers/")
        await a.wait_for_timeout(10000)

    return a


session_id = asyncio.run(main())
