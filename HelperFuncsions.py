import asyncio
import json

from playwright.async_api import async_playwright


async def ExtractImgs(img_elements, Path, Dtype):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        Addon = 0
        for img in img_elements:
            if img and (img.startswith("http://") or img.startswith("https://")):
                await page.goto(img)
                path = f"{Path}{Addon}.{Dtype}"
                await page.screenshot(path=path)
                Addon += 1


async def ExtractImgsFromHTMl(img_elements, Path, Dtype):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        Addon = 0
        f = open("demofile2.txt", "a")
        print(img_elements)
        for img in img_elements:
            cImg = await img.get_attribute("src")
            if cImg and (cImg.startswith("http://") or cImg.startswith("https://")):
                await page.goto(cImg)
                path = f"{Path}{Addon}.{Dtype}"
                print(cImg)
                f.write("hello its me ")

                await page.screenshot(path=path)
                Addon += 1
        f.close()


async def ExtractImgsPWI(PlayWrightInstcace, img_elements):
    page2 = await PlayWrightInstcace.new_page()
    Addon = 0
    starting_text = "Smash"
    f = open("demofile2.txt", "a")
    print(img_elements)
    for img in img_elements:
        cImg = await img.get_attribute("src")
        if cImg and (cImg.startswith("http://") or cImg.startswith("https://")):
            await page2.goto(cImg)
            path = f"{starting_text}{Addon}.png"
            print(cImg)
            f.write("hello its me ")
            await page2.screenshot(path=path)
            Addon += 1

    f.close()
