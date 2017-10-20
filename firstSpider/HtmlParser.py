# coding: utf-8
"""
Use BeautifulSoup4 to parse the HTML
For this spider, we need to fetch current entry's url, title and summary
By analysing the HTML, find out:
                    title: <dd class="lemmaWgt-lemmaTtile-title"><h1>XXX</h1></dd>
                    summary: <div class="lemma-summary" label-module="lemmaSummary">
                    url: the format is like <a target="_blank" href="/view/7833.htm">XXX</a>
                        so this is the format of relative url, we can use urlparse.urljoin() to
                        concatenate current website url and relative url to make it complete
"""
import urlparse
import re
from bs4 import BeautifulSoup


class HtmlParser(object):

    def parser(self, page_url, html_cont):
        '''
        to parse html, fetch url and data we need
        :param page_url: download page urls (current website url, incomplete)
        :param html_cont: downloaded html contents for BeautifulSoup to parse
        :return: entry url and data
        '''
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser') # initialize soup
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        ''' 
        set of complete urls of entries
        :param page_url: current entry partial url
        :param soup: soup
        :return: set of urls which is complete after concatenation
        '''
        new_urls = set()
        # fetch qualified links with <a>
        links = soup.find_all('a', href=re.compile(r'/item/\S+\d+'))
        for link in links:
            # fetch href property
            partial_url = link.get('href')
            # concatenate complete url
            new_complete_url = urlparse.urljoin(page_url, partial_url)
            new_urls.add(new_complete_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        '''
        fetch data we need(title and summary of entry)
        :param page_url: current entry url
        :param soup: soup
        :return: dict of data we need
        '''
        data={}
        data['url'] = page_url
        title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title'] = title.get_text()
        summary = soup.find('div', class_='lemma-summary')
        # .text == get_text() if no parameter need
        data['summary'] = summary.get_text()
        return data

