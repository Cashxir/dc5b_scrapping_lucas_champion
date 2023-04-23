import requests
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/simple/'
s = requests.Session()
r = s.get(url)

soup = BeautifulSoup(r.content, 'html.parser')
country = soup.find_all('div', {'class': 'col-md-4 country'})

for div in country:
    text = div.get_text()
    print(text)