import requests
user_agent = 'Mozilla/4.0 (compatible; MISE 5.5; Windows NT)'
headers = {'User-Agent':user_agent}
r = requests.get('http://www.baidu.com', headers=headers)
for cookie in r.cookies.keys():
    print cookie+':'+r.cookies.get(cookie)
