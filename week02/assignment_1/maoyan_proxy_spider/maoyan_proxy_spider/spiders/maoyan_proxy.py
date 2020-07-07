import scrapy
from scrapy.selector import Selector
from maoyan_proxy_spider.items import MaoyanProxySpiderItem


class MaoyanProxySpider(scrapy.Spider):
    name = 'maoyan_proxy'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://m.maoyan.com/?showType=3']

    def start_requests(self):
        url = 'https://m.maoyan.com/?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = MaoyanProxySpiderItem()

        movies = Selector(response=response).xpath('//div[@class="classic-movies-list"]/a/div/div[2]')

        for movie in movies:
            name = movie.xpath('./div[1]/text()').get()
            category = movie.xpath('./div[3]/text()').get()
            release_info = movie.xpath('./div[4]/text()').get()

            item['name'] = name
            item['category'] = category
            item['release_info'] = release_info

            yield item
