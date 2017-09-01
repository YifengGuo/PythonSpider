import requests
proxies = {
    "http": "http://0.10.1.10:3128",
    "https": "http://10.10.1.10:1080",
}
r = requests.get("http://eclipse.org", proxies=proxies)
print r.content