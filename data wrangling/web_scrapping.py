import requests
from bs4 import BeautifulSoup

url = ""
source = requests.get(url)

soup = BeautifulSoup(source.content)

links = soup.find_all("a")

for link in links:
    print("<a href = '%s'>%s</a>" % (link.get("href"), link.text))


g_data = soup.find_all("div", {"class": "info"})
