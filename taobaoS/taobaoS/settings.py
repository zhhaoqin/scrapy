# -*- coding: utf-8 -*-

# Scrapy settings for taobaoS project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'taobaoS'

SPIDER_MODULES = ['taobaoS.spiders']
NEWSPIDER_MODULE = 'taobaoS.spiders'

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 1

COOKIES_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}

ITEM_PIPELINES = {
    'taobaoS.pipelines.MongoPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 301
}

MONGO_URI = 'localhost'
MONGO_DATABASE = 'taobaoS'

SCHEDULER = "scrapy_redis.scheduler.Scheduler"

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

REDIS_URL = 'redis://@192.168.0.102:6379'