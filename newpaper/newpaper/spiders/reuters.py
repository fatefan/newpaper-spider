# -*- coding: utf-8 -*-
import scrapy


class ReutersSpider(scrapy.Spider):
    name = 'reuters'
    allowed_domains = ['cn.reuters.com']
    start_urls = ['http://cn.reuters.com/']

    def parse(self, response):
        pass
