import asyncio

from playwright.async_api import async_playwright

from GetCockysInstagram import Nlogin, login
from HelperFuncsions import ExtractImgs
from PlayWirghtCockkcys import login_and_get_session


async def scrape_user(username: str, login_cookie: str):
    async with async_playwright() as p:
        # Start a browser instance
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        )

        # Create a new page
        page = await context.new_page()
        # if login_cookie != None:
        #     await context.add_cookies(login_cookie)
        # Make the request to Instagram API
        response = await page.request.get(
            f"https://i.instagram.com/api/v1/users/web_profile_info/?username={
                username}",
            headers={
                "x-ig-app-id": "936619743392459",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
                "Accept-Language": "en-US,en;q=0.9,ru;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept": "*/*",
                "X-Requested-With": "XMLHttpRequest",  # Common AJAX header
            },
        )

        # Check if the request was successful
        if response.status != 200:
            print(
                f"Failed to fetch user data: {
                    response.status} {response.status_text}"
            )
            await browser.close()
            return None

        # Parse the response
        data = await response.json()

        # Close the browser
        await browser.close()

        # Return the user data
        return data.get("data", {}).get("user", None)


async def parseSrc(thumbnail_resources):
    srcs = []
    for thumbnail in thumbnail_resources:
        # Replace escaped character
        src = thumbnail["src"].replace("\\u0026", "&")
        srcs.append(src)

    return src


async def parse(data):
    #    # print(data["edges"]["thumbnail_resources"])
    allData = []
    data = data["edge_owner_to_timeline_media"]["edges"]
    for i in data:
        allData.append(await parseSrc(i["node"]["thumbnail_resources"]))
    # # print(len(data))
    return allData


async def main():
    username = "michaeljohnsonth3@gmail.com"
    password = "helloitsme1234"
    username = "gjirafa50"  # Replace with the desired Instagram username
    # username = "redonblakajj"  # Replace with the desired Instagram username
    cook = await Nlogin(loginuser, password)
    user_data = await scrape_user(username, cook)

    if user_data:
        # print(user_data)
        userphotos = await parse(user_data)
        print(userphotos)
        testinga = await ExtractImgs(userphotos, "Redon", "png")

        # logi = await login(loginuser, password)
        # OtherLogin = await Nlogin(loginuser, password)

        # # print(a)
    else:
        print("No user data retrieved.")

    # Run the main function


if __name__ == "__main__":
    asyncio.run(main())
