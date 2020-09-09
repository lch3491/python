import requests
from bs4 import BeautifulSoup

url = "http://google.com"
res = requests.get(url)
res.raise_for_status()
print(res.text)