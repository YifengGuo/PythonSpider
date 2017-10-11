# precondition is the web is static
# no content is loaded by JavaScript dynamically
import requests
from bs4 import BeautifulSoup

user_agent = 'Mozzila/4.0 (compatible; MISE 5.5; Windows NT)'
headers = {'User-Agent':user_agent}
r = requests.get('http://seputu.com', headers=headers)
print r.text

soup = BeautifulSoup(r.text, 'html.parser',from_encoding='utf-8')
for mulu in soup.find_all(class_="mulu"):
    h2 = mulu.find('h2')
    if h2 != None:
        h2_title = h2.string # obtain title
        for a in mulu.find(class_='box').find_all('a'):
            href = a.get('href')
            box_title = a.get('title')
            print href,box_title