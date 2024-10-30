import asyncio
import datetime

import requests
from bs4 import BeautifulSoup


async def login(username, password):
    """Login to Instagram"""

    session = requests.session()
    time = str(int(datetime.datetime.now().timestamp()))
    print(time)
    enc_password = f"#PWD_INSTAGRAM_BROWSER:0:{time}:{password}"

    # set a cookie that signals Instagram the "Accept cookie" banner was closed
    session.cookies.set("ig_cb", "2")
    session.headers.update(
        {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
             Chrome/59.0.3071.115 Safari/537.36"
        }
    )
    session.headers.update({"Referer": "https://www.instagram.com"})
    res = session.get("https://www.instagram.com")

    csrftoken = None

    for key in res.cookies.keys():
        if key == "csrftoken":
            csrftoken = session.cookies["csrftoken"]

    session.headers.update({"X-CSRFToken": csrftoken})
    login_data = {"username": username, "enc_password": enc_password}

    login = session.post(
        "https://www.instagram.com/accounts/login/ajax/", data=login_data, allow_redirects=True
    )
    session.headers.update({"X-CSRFToken": login.cookies["csrftoken"]})

    cookies = login.cookies
    print(session.headers)
    print(login.text)

    return cookies
    # session.close()


async def Nlogin(username, password):
    """Login to Instagram and return cookies for Playwright"""
    session = requests.session()
    time = str(int(datetime.datetime.now().timestamp()))
    enc_password = f"#PWD_INSTAGRAM_BROWSER:0:{time}:{password}"

    # Set the cookie to simulate "Accept cookie" banner closure
    session.cookies.set("ig_cb", "2")
    session.headers.update(
        {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
        }
    )
    session.headers.update({"Referer": "https://www.instagram.com"})
    res = session.get("https://www.instagram.com")

    csrftoken = None

    for key in res.cookies.keys():
        if key == "csrftoken":
            csrftoken = session.cookies["csrftoken"]

    session.headers.update({"X-CSRFToken": csrftoken})
    login_data = {"username": username, "enc_password": enc_password}

    login = session.post(
        "https://www.instagram.com/accounts/login/ajax/", data=login_data, allow_redirects=True
    )
    session.headers.update({"X-CSRFToken": login.cookies["csrftoken"]})

    # Check if login was successful
    if login.status_code != 200 or not login.json().get("authenticated"):
        # print("Login failed:", login.text)
        return None

    # Extract cookies in Playwright format with domain and path
    cookies = [
        {
            "name": c.name,
            "value": c.value,
            "domain": c.domain if c.domain else "instagram.com",
            "path": c.path if c.path else "/",
            "httpOnly": c.has_nonstandard_attr("HttpOnly"),
            "secure": c.secure,
        }
        for c in session.cookies
    ]
    print(login)

    return cookies


async def CRFT_Challange(username, password):
    session = requests.session()
    time = str(int(datetime.datetime.now().timestamp()))
    # pip3 install requests beautifulsoup4

    # the URL of the login page
    login_url = "https://www.scrapingcourse.com/login/csrf"

    # the payload with your login credentials
    payload = {
        "email": username,
        "password": password,
    }

    # send the POST request to login
    response = requests.post(login_url, data=payload)

    # if the request went Ok, you should get a 200 status
    print(f"Status code: {response.status_code}")

    # parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # find the page title
    page_title = soup.title.string

    # print the result page title
    print(f"Page title: {page_title}")


async def main():
    # print(await CRFT_Challange("admin@example.com", "password"))
    print(await login("", "helloitsme1234"))
    print("other")
    print(await Nlogin("", "helloitsme1234"))


if __name__ == "__main__":
    asyncio.run(main())
