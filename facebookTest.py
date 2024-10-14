# import json


from playwright.sync_api import sync_playwright

# contst id for post documents instagram.com
INSTAGRAM_DOCUMENT_ID = "8845758582119845"
shortcode = "CJ9KxZ2l8jT"  # the post id

variables = {
    "shortcode": shortcode,
    "fetch_tagged_user_count": None,
    "hoisted_comment_id": None,
    "hoisted_reply_id": None,
}
# variables = quote(json.dumps(variables, separators=(",", ":")))
# body = f"variables={variables}&doc_id={INSTAGRAM_DOCUMENT_ID}"


def get_Cokkie():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the Wikipedia homepage
        page.goto("https://www.facebook.com/")

        # Click on the search input field
        page.fill("input[name='email']", "shehumet")

        page.fill("input[name='pass']", "KripKing123")

        # Using the id from the button element

        page.click("[name='login']")

        cookies = context.cookies()[3]["value"]
        print(cookies)
        browser.close()


# Example usage
get_Cokkie()
