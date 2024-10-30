import asyncio
from playwright.async_api import async_playwright


def a():
    print(1)


async def ExtractImgs(context, img_elements):
    page2 = await context.new_page()
    name_n = 0
    starting_text = "Smash"
    f = open("demofile2.txt", "a")
    print(img_elements)
    for img in img_elements:
        cImg = await img.get_attribute("src")
        if cImg and (cImg.startswith("http://")
                     or cImg.startswith("https://")):
            # Navigate to the image URL and take a screenshot
            await page2.goto(cImg)
            path = f"{starting_text}{name_n}.png"
            print(cImg)
            f.write("hello its me ")

            await page2.screenshot(path=path)
            name_n += 1

    f.close()


async def GetButtons(button_elemts):
    x = 0
    for butt in button_elemts:
        x += 1


async def main():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        # Go to Instagram page
        # await page.goto("https://en.wikipedia.org/wiki/Assembly_language")
        await page.goto("https://www.instagram.com/xblertaaa/")

        # await page.goto("https://www.facebook.com/profile.php?id=61555982545946")

        # await page.goto("https://www.instagram.com/oxnela/")
        # await page.goto("https://www.facebook.com/profile.php?id=61550882552807")
        # Set viewport size

        await page.set_viewport_size({"width": 1600, "height": 900})

        # Wait for 10 seconds
        await page.wait_for_timeout(10000)
        # Select all img elements
        img_elements = await page.query_selector_all("img")
        buttons_elemts = await page.query_selector_all("button")
        # await page.get_by_role("but").click(force=True)
        # Open a new page for downloading images
        # await page.get_by_role("but").click()

        # a =await page.locator("button")
        # #await GetButtons(buttons_elemts)

        await ExtractImgs(context, img_elements)
        # search_term = "Python (programming language)"
        # await page.fill("input[name='search']", search_term)

        # await page.press("input[name='search']", "Enter")

        #  await page.wait_for_timeout(2000)
        # Loop through selected images from the 6th to the 20th
        await page.screenshot(path="start.png")
        # if name_n == 0:
        # print(str(img))
        # await page2.goto(cImg)
        # path = f"{starting_text}{name_n}.png"
        # await page2.screenshot(path=path)
        # name_n += 1

        # await browser.close()


# import asyncio

# from playwright.async_api import async_playwright

asyncio.run(main())
