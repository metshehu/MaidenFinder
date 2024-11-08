import asyncio

import aiofiles
from playwright.async_api import async_playwright

from HelperFuncsions import ExtractImgs
from Parsers import get_images_in_div, getPrivateState, pageFollowers, pageParser
from RequestHanlderBase import getImgs

NAME = "sun_tzu_bab"
username = "suttonelara@gmail.com"
password = "helloitsme1234"


async def loginPage(username, password, playWrightInstance, context):
    browser = await playWrightInstance.chromium.launch(headless=False)
    page = await context.new_page()

    await page.goto("https://www.instagram.com/accounts/login/")
    await page.wait_for_selector("input[name='username']")
    await page.wait_for_selector("input[name='password']")
    await page.fill("input[name='username']", username)
    await page.fill("input[name='password']", password)
    await page.click("button[type='submit']")
    await page.wait_for_timeout(10000)
    await page.goto(f"https://www.instagram.com/{NAME}/")
    await page.wait_for_timeout(10000)

    return page


async def GetUsers():
    return 0


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        )
        page = await loginPage(username, password, p, context)
        html_content = await page.content()
        await page.click(f"a[href='/{NAME}/followers/']")

        await page.wait_for_timeout(10000)
        await page.eval_on_selector(
            ".xyi19xy.x1ccrb07.xtf3nb5", "el => el.scrollTop = el.scrollHeight"
        )
        await page.wait_for_timeout(10000)
        html_content_followrs = await page.content()
        data = await pageFollowers(html_content_followrs)

        r = []
        name = []
        for i in data:
            await page.goto(f"https://www.instagram.com/{i[0]}/")
            # await page.wait_for_load_state(state="load", timeout=30000)# maybe better still have to do some testing
            await page.wait_for_timeout(5000)
            html_content = await page.content()
            filename = "page_content_" + i[0] + ".html"
            state = await getPrivateState(html_content)

            if i[0] != "lisazaimii":
                with open(filename, "w", encoding="utf-8") as file:
                    file.write(html_content)
            if state != False:
                print(i[0] + " is Privat Fucking Incless")
            else:
                photos = await get_images_in_div(html_content)
                length = len(photos)
                if length > 0:
                    print(i[0] + " YAYYY have PHotos")
                    print(length)
                    r.append(photos)
                    name.append(i[0])
                else:
                    print(i[0] + " not incellss but no PhotosGay")
            await page.wait_for_timeout(3000)
        index = 0
        for value in r:
            await ExtractImgs(value, name[index], "png")
            index += 1
        await page.wait_for_timeout(10000)

    return page


session_id = asyncio.run(main())
