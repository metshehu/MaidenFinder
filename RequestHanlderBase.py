import asyncio

from playwright.async_api import async_playwright


async def scrape_user(username: str):
    """Scrape Instagram user's data using Playwright."""
    async with async_playwright() as p:
        # Start a browser instance
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        )

        # Create a new page
        page = await context.new_page()

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
    #    print(data["edges"]["thumbnail_resources"])
    allData=[]
    data = data["edge_owner_to_timeline_media"]["edges"]
    for i in data:
        allData.append(await parseSrc(i["node"]["thumbnail_resources"]))
    print(len(data))
    return allData


async def main():
    username = "mettusha8"  # Replace with the desired Instagram username
    user_data = await scrape_user(username)

    if user_data:
        # print(user_data)
        a = await parse(user_data)
        for i in a:
            print(i)
            print("\n")

        print(a)
    else:
        print("No user data retrieved.")


# Run the main function
if __name__ == "__main__":
    asyncio.run(main())