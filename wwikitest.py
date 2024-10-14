from playwright.sync_api import sync_playwright


def search_wikipedia(search_term):
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to the Wikipedia homepage
        page.goto("https://www.wikipedia.org/")

        # Click on the search input field
        page.fill("input[name='search']", search_term)
        # Optionally, you can press "Enter" to initiate the search
        page.press("input[name='search']", "Enter")

        page.screenshot(path="before.png")
        for i in page.get_by_role("button").all():
            print(i.all_inner_texts())
            if "hide" in i.all_inner_texts():
                print("in")
                i.click()

        # Wait for a while to see the results (optional)
        page.evaluate("window.scrollTo(0, 0)")

        page.screenshot(path="after.png")
        page.wait_for_timeout(3000)

        # Close the browser
        browser.close()


# Example usage
search_wikipedia("Python (programming language)")
