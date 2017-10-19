# coding: utf-8
import requests

'''
HtmlDownloader offers download(self,url) interface which 
is to download and return given url html content
'''


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        user_agent = 'Mozilla 4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            r.encoding = 'utf-8'  # to avoid messy code, remember to check the encoding of source
            return r.text

        return None