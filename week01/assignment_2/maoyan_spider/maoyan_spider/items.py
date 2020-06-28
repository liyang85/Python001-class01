# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass

    name = scrapy.Field()
    category = scrapy.Field()
    release_info = scrapy.Field()
