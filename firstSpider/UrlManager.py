 # coding: utf-8
"""
Url Manager for first spider
UrlManager is to manage urls, maintain two sets, one is to store urls which has been crawled
and the other one is to store urls which has not been crawled
UrlManager also offers interface for adding new url(s) to be crawled
"""
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()  # urls which has not been crawled
        self.old_urls = set()  # urls which has been crawled


    def has_new_url(self):
        '''
        to check if there is any new url which has not been crawled
        :return: true if there is some new url which has not been crawled
        '''
        return self.new_url_size() != 0


    def get_new_url(self):
        '''
        obtain a url which has not been crawled
        :return: 
        '''
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_url(self, url):
        '''
        add a new non-crawled url to new_urls 
        :param url: 
        :return: 
        '''
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)


    def add_new_urls(self, urls):
        '''
        add new non-crawled urls into new_urls
        :param urls: url collection 
        :return: 
        '''
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            if url not in self.new_urls and url not in self.old_urls:
                self.new_urls.add(url)


    def new_urls_size(self):
        '''
        get current new_urls size
        :return: 
        '''
        return len(self.new_urls)


    def old_urls_size(self):
        '''
        get current old_urls size
        :return: 
        '''
        return len(self.old_urls)