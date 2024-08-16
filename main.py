import requests
from bs4 import BeautifulSoup

# Replace with the URL you want to scrape
Url = "https://www.instagram.com/4rb3r/"


response = requests.get(Url)
soup = BeautifulSoup(response.text, "html.parser")

img_tags = soup.find_all("img")
print(img_tags)
