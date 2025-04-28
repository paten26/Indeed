import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.detik.com/terpopuler')
#req = requests.get(url)
#print(req.status_code)

soup = BeautifulSoup(url.text, 'html-parser')

print(soup)