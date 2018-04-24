# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class TaobaoItem(Item):

    name = Field()
    url = Field()
    price = Field()
    sales_volume = Field()
    shopname = Field()
    shopaddress = Field()
