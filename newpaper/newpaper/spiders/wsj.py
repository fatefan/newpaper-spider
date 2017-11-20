# -*- coding: utf-8 -*-
import scrapy


class WsjSpider(scrapy.Spider):
    name = 'wsj'
    allowed_domains = ['cn.wsj.com']
    start_urls = ['http://cn.wsj.com/']

    def parse(self, response):
        pass
