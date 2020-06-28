# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from maoyan_spider.items import MaoyanSpiderItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://m.maoyan.com/?showType=3']

    def start_requests(self):
        url = 'https://m.maoyan.com/?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # pass

        item = MaoyanSpiderItem()

        # Copied XPath from Chrome
        # /html/body/div[2]/section[2]/div[4]/div[2]/div/div/div[1]/div/div/a[1]/div/div[2]/div[1]
        # /html/body/div[2]/section[2]/div[4]/div[2]/div/div/div[1]/div/div/a[1]/div/div[2]/div[3]
        # /html/body/div[2]/section[2]/div[4]/div[2]/div/div/div[1]/div/div/a[1]/div/div[2]/div[4]

        movies = Selector(response=response).xpath('//div[@class="classic-movies-list"]/a/div/div[2]')
        # split_line = '=*= '
        # print(split_line * 20)
        # print(movies)
        # print(split_line * 20)

        for movie in movies:
            name            = movie.xpath('./div[1]/text()').get()
            category        = movie.xpath('./div[3]/text()').get()
            release_info    = movie.xpath('./div[4]/text()').get()

            # print(split_line * 20)
            # print(name)
            # print(category)
            # print(release_info)
            # print(split_line * 20)

            item['name'] = name
            item['category'] = category
            item['release_info'] = release_info

            yield item


