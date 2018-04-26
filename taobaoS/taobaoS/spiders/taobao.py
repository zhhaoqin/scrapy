# -*- coding: utf-8 -*-

import re
import json
from scrapy import Spider, Request, FormRequest
from taobaoS.items import TaobaoItem


class TaobaoSpider(Spider):
    name = 'taobao'
    keyword = '耳机'
    allowed_domains = ['s.taobao.com']
    url = 'https://s.taobao.com/search?q=' + keyword

    def start_requests(self):       
        for n in range(0, 101):
            print(n)
            url = self.url + '&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=' + str(44 * n)            
            print(url)
            yield FormRequest(url, callback=self.parse)

    def parse(self, response):       
        r = response.xpath('//head/script[last()]/text()').extract_first().strip()
        text = re.match(r'.*?"auctions":(.*)', r).group(1)
        results = json.loads(re.match(r'(.*?)recommendAuctions', text).group(1)[:-2])
        for result in results:
            item = TaobaoItem()
            item['title'] = result.get("raw_title")
            item['link'] = result.get("detail_url")
            item['price'] = result.get("view_price")
            item['view_sales'] = result.get("view_sales")
            item['shop'] = result.get("nick")
            item['location'] = result.get("item_loc")
            yield item

    
            




        






        
