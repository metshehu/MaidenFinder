import asyncio

from playwright.async_api import async_playwright


async def login_and_get_session(username: str, password: str):
    async with async_playwright() as p:
        # Launch browser (set headless=True to run it without UI)
        # Use headless=True for non-visual mode
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()

        # Open a new page
        page = await context.new_page()

        # Navigate to Instagram login page
        await page.goto("https://www.instagram.com/accounts/login/")

        # Wait for the username and password fields to be visible
        await page.wait_for_selector("input[name='username']")
        await page.wait_for_selector("input[name='password']")

        # Fill in the username and password fields
        await page.fill("input[name='username']", username)
        await page.fill("input[name='password']", password)

        # Click the login button
        await page.click("button[type='submit']")
        await page.wait_for_timeout(6000)
        await page.goto("https://www.instagram.com/redonblakajj/")
        await page.wait_for_timeout(30000)
        # Wait for the home page or some element that confirms successful login
        try:
            # Wait for Instagram to redirect to the home page
            await page.wait_for_url(
                "https://www.instagram.com/", timeout=30000
            )  # Wait up to 30 seconds
            print("Login successful!")
            cookies = await context.cookies()
            await browser.close()
            print(cookies)
            return cookies
        except Exception as e:
            print(f"Error: {e}")
            await browser.close()
            return None


async def loginCrft(username: str, password: str):
    async with async_playwright() as p:
        # Launch browser (set headless=True to run it without UI)
        # Use headless=True for non-visual mode
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()

        # Open a new page
        page = await context.new_page()

        # Navigate to Instagram login page
        await page.goto("https://www.scrapingcourse.com/login/csrf")

        # Wait for the username and password fields to be visible
        await page.wait_for_selector("input[name='username']")
        await page.wait_for_selector("input[name='password']")

        # Fill in the username and password fields
        await page.fill("input[name='username']", username)
        await page.fill("input[name='password']", password)

        # Click the login button
        await page.click("button[type='submit']")
        await page.wait_for_timeout(100000)
        await page.wait_for_timeout(100000)
        # Wait for the home page or some element that confirms successful login
        #try:
            # Wait for Instagram to redirect to the home page
        #await page.wait_for_url(
        #    "https://www.instagram.com/", timeout=30000
        #)  # Wait up to 30 seconds
        print("Login successful!")
        cookies = await context.cookies()
        await browser.close()
        print(cookies)
        return cookies
        #except Exception as e:
       #     print(f"Error: {e}")
      #      await browser.close()
     #       return None


# Example usage
if __name__ == "__main__":
    username = "michaeljohnsonth3@gmail.com"

    password = "helloitsme1234"
    #    session_id = asyncio.run(login_and_get_session(username, password))

    session_id = asyncio.run(login_and_get_session(username, password))
    if session_id:
        print("Session ID:", session_id)
    else:
        print("Failed to retrieve session ID.")
