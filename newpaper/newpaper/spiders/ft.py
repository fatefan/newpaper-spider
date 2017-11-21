# -*- coding: utf-8 -*-
import json
from scrapy.spider import Spider
from scrapy.selector import Selector
class FtSpider(Spider):
    name = 'ft'
    allowed_domains = ['http://www.ftchinese.com']
    start_urls = ['http://www.ftchinese.com/rss/feed']
    def parse(self, response):
            select = Selector(text=response.body,type='xml')
            itemlist = select.xpath('//item')
            for index,item in enumerate(itemlist):
                    des = item.xpath('./description/text()').extract()    
                    title = item.xpath('./title/text()').extract()    
                    link = item.xpath('./link/text()').extract()    
                    time = item.xpath('./pubDate/text()').extract()
                    print index,title[0].encode('utf-8'),link[0].encode('utf-8'),time[0].encode('utf-8') 
            pass
