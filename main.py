import pyperclip
import requests
from bs4 import BeautifulSoup

spam = pyperclip.paste()

# Replace with the URL you want to scrape
Url = "https://www.instagram.com/mandyyliuu/"


response = requests.get(Url)
soup = BeautifulSoup(response.text, "html.parser")

img_tags = soup.find_all("img")

# img_tags = soup.find("img")


def printText(absstring):
    return True

print(len(img_tags))

pyperclip.copy(img_tags[1]["src"])
