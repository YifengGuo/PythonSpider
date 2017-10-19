# function prototype urlretrieve(url, filename=None, reporthook=None, data=None)
# filename -> file storage path
# reporthook is a callback function, after connecting with server and download corresponding data block
# reporthook will be called. we can use the reporthook to check out the progress of download

import urllib
from bs4 import BeautifulSoup
import requests
from lxml import etree
import os


def schedule(blocknum,blocksize,totalsize):
    '''
    :param blocknum: downloaded blocks number
    :param blocksize: block size
    :param totalsize: total size of remote file
    :return: 
    '''
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    print 'current rate of download: %d'%percent


def get_HTML_from_url(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent};
    r = requests.get(url, headers=headers)
    return r.text

# initialize file to store images
if os.path.exists('images'):
    pass
else:
    print('Successfully make directory images')
    os.mkdir('images')


# parse the HTML and fetch images by BeautifulSoup
def download_images_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    img_urls = soup.find_all('img') # find all links with 'img' and store in a list
    i = 0
    for link in img_urls:
        url = link.get('src')  # url is img source address
        urllib.urlretrieve(url,'images/img'+str(i)+'.jpg', schedule) # download images by urlretrieve()
        i += 1

# fetch images by Xpath
# html = etree.HTML(r.text)
# img_urls = html.xpath('.//img/@src')
# i = 0
# for img_url in img_urls:
#     urllib.urlretrieve(img_url,'images/img'+str(i)+'.jpg',Schedule)
#     i+=1

if __name__ == "__main__":
    html = get_HTML_from_url('http://www.ivsky.com/tupian/ziranfengguang/')
    download_images_from_html(html)