from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Replace with the URL of the page you want to check
    # page.goto("https://www.instagram.com/liburn.bajraktari/")

    page.goto("https://www.instagram.com/spamiririt/")
    page.wait_for_load_state(state='load', timeout=30000)

    # Check if the text "This account is private" exists anywhere on the page

    response = page.content()
    soup = BeautifulSoup(str(response), "html.parser")
    if "This account is private" in soup.get_text():
        print("yes")
    else:
        print("no")

    browser.close()
