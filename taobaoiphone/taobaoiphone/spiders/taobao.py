# -*- coding: utf-8 -*-

import json
from scrapy import Spider, Request, Selector
from taobaoiphone.items import TaobaoItem


class TaobaoSpider(Spider):
    name = 'taobao'
    keyword = '耳机'
    allowed_domains = ['s.taobao.com']
    url = 'https://s.taobao.com/search?q=' + keyword
    start_urls = ['https://s.taobao.com/search?app=mainSrp&q=%E6%89%8B%E6%9C%BA&cd=false&bcoffset=0&ntoffset=6&p4ppushleft=1%2C48&s=88']

    def parse(self, response):
        r = response.xpath('/html/head/script[43]/text()').extract_first()
        print(r)




      
    """
    def parse(self, response):
        page = 0
        while page < 50:
            count = 44 * page
            start_url = self.url + '&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=' + str(count)
            yield Request(start_url, callback=self.parse_item)
            page += 1
    

    def parse_item(self, response):
        sels = Selector(response).xpath('//div')
        for sel in sels:
            item = TaobaoItem()
            item['url'] = sel.xpath('//div[@class="pic"]/a/@href').extract()
            item['name'] = sel.xpath('//div[@class="pic"]/a/img/@alt').extract()
            item['price'] = sel.xpath('//div[@class="price g_price g_price-highlight"]/strong/text()').extract()
            item['sales_volume'] = sel.xpath('//div[@class="deal-cnt"]/text()').extract()
            item['shopname'] = sel.xpath('//div[@class="shop"]/a/span[2]/text()').extract()
            item['shopaddress'] = sel.xpath('//div[@class="location"]/text()').extract()      
        yield item
    """





        
