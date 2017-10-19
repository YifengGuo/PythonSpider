# coding:utf-8
# precondition is the web is static
# no content is loaded by JavaScript dynamically
import sys
reload(sys)
sys.setdefaultencoding('utf-8') # make sure content is encoded by utf-8 instead of ascii which cannot represent Chinese
import json
import requests
from bs4 import BeautifulSoup

user_agent = 'Mozzila/4.0 (compatible; MISE 5.5; Windows NT)'
headers = {'User-Agent':user_agent}
r = requests.get('http://seputu.com', headers=headers)
print r.text # print html

soup = BeautifulSoup(r.text, 'html.parser')
content = []
for mulu in soup.find_all(class_="mulu"):   # type of mulu: bs4.element.Tag (list)
    h2 = mulu.find('h2')
    if h2 != None:
        h2_title = h2.string # obtain title
        list = []
        for a in mulu.find(class_='box').find_all('a'):
            href = a.get('href')
            box_title = a.get('title')
            list.append({'href':href, 'box_title':box_title})
        content.append({'title':h2_title,'content':list})
with open('daomubiji.json','wb') as fp:
    json.dump(content,fp=fp,indent=4,ensure_ascii=False)
