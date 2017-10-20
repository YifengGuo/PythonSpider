# coding:utf-8
from firstSpider.HtmlDownloader import HtmlDownloader
from firstSpider.UrlManager import UrlManager
from firstSpider.DataOutput import DataOutput
from firstSpider.HtmlParser import HtmlParser
"""
The SpiderMan is the scheduler of whole spider program
It will initialize each module first and control the workflow
of each module as designed
"""


class SpiderMan(object):
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self, root_url):
        # add root url into new_urls of manager
        self.manager.add_new_url(root_url)
        # check if new_urls has urls left and old_urls limit is out of bound
        while self.manager.has_new_url() and self.manager.old_urls_size()<40:
            try:
                # obtain new url from url manager
                new_url = self.manager.get_new_url()
                # download html code of given new url
                html = self.downloader.download(new_url)
                # parse and fetch data of html by parser
                new_urls, data = self.parser.parser(new_url, html)
                # add new fetched urls into manager.new_urls
                self.manager.add_new_urls(new_urls)
                # store crawled data
                self.output.store_data(data)

                print "%s entries have been crawled."%self.manager.old_urls_size()
            except Exception,e:
                print "Crawler failed."
        self.output.output_html()

if __name__=="__main__":
    spider = SpiderMan()
    spider.crawl("http://baike.baidu.com/view/284858.htm")