import asyncio
from typing import NewType

import aiofiles
from bs4 import BeautifulSoup

type imgList = list[str]
type FollowrsList = list[str]


async def pageParser(html_content) -> imgList:
    all_imgs = []
    soup = BeautifulSoup(html_content, "html.parser")

    src_tags = soup.find_all(attrs={"src": True})

    src_list = [tag["src"] for tag in src_tags]
    for src in src_list:
        all_imgs.append(src)
    return all_imgs


async def pageParserFromFile(file: str) -> imgList:
    all_imgs = []
    async with aiofiles.open(file, "r", encoding="utf-8") as file:
        html_content = await file.read()
    soup = BeautifulSoup(html_content, "html.parser")

    src_tags = soup.find_all(attrs={"src": True})

    src_list = [tag["src"] for tag in src_tags]
    for src in src_list:
        all_imgs.append(src)
    return all_imgs


async def pageFollowers(html_content) -> FollowrsList:

    # Sample HTML content (replace with your actual HTML content)

    soup = BeautifulSoup(html_content, "html.parser")

    # Sample HTML content (replace with your actual HTML content)

    # Parse the HTML content with BeautifulSoup
    results = []
    for div in soup.find_all(
        "div", class_="x9f619 x1ja2u2z x78zum5 x2lah0s x1n2onr6 x1qughib x6s0dn4 xozqiw3 x1q0g3np"
    ):
        a_tag = div.find("a")
        name_tag = div.find("span")

        # Extract the link and name if they exist
        if a_tag and name_tag:
            profile_link = a_tag["href"]
            profile_name = name_tag.text.strip()
            results.append((profile_name, profile_link))

    # Print the results
    # for name, link in results:
    # print(f"Profile Name: {name}, Profile Link: {link}")
    # soup = BeautifulSoup(html_content, "html.parser")

    # Extract the link from the <a> tag
    #  a_tag = soup.find("a", class_="x1i10hfl x1qjc9v5 xjbqb8w")

    # Extract the name from the <span> tag
    # print(a_tag)
    return results


async def pageFollowersFromFile(file: str) -> FollowrsList:

    # Sample HTML content (replace with your actual HTML content)
    async with aiofiles.open(file, "r", encoding="utf-8") as file:
        html_content = await file.read()
    soup = BeautifulSoup(html_content, "html.parser")
    # print(html_content)

    # Sample HTML content (replace with your actual HTML content)

    # Parse the HTML content with BeautifulSoup
    results = []
    for div in soup.find_all(
        "div", class_="x9f619 x1ja2u2z x78zum5 x2lah0s x1n2onr6 x1qughib x6s0dn4 xozqiw3 x1q0g3np"
    ):
        a_tag = div.find("a")
        name_tag = div.find("span")

        # Extract the link and name if they exist
        if a_tag and name_tag:
            profile_link = a_tag["href"]
            profile_name = name_tag.text.strip()
            results.append((profile_name, profile_link))

    # Print the results
    for name, link in results:
        print(f"Profile Name: {name}, Profile Link: {link}")
        soup = BeautifulSoup(html_content, "html.parser")

        # Extract the link from the <a> tag
        a_tag = soup.find("a", class_="x1i10hfl x1qjc9v5 xjbqb8w")

        # Extract the name from the <span> tag
        print(a_tag)


async def pageFollowersFromFile2(file: str) -> FollowrsList:

    # Sample HTML content (replace with your actual HTML content)
    async with aiofiles.open(file, "r", encoding="utf-8") as file:
        html_content = await file.read()
    await pageFollowers(html_content)


if __name__ == "__main__":
    asyncio.run(pageFollowersFromFile2("page_contentFollowrs2.html"))
