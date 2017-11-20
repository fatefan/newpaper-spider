# -*- coding: utf-8 -*-
from scrapy.spider import Spider
from scrapy.selector import Selector
from newpaper.items import NewpaperItem

class FtSpider(Spider):
    name = 'ft'
    allowed_domains = ['http://www.ftchinese.com']
    start_urls = ['http://www.ftchinese.com/rss/feed']

    def parse(self, response):
            select = Selector(text=response.body)
            print select.xpath('//title/text()').extract()
            pass
