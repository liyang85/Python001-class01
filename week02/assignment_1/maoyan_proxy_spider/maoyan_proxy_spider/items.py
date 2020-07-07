# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanProxySpiderItem(scrapy.Item):
    name = scrapy.Field()
    category = scrapy.Field()
    release_info = scrapy.Field()