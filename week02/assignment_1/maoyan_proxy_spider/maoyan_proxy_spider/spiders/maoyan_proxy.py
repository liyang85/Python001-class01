import scrapy


class MaoyanProxySpider(scrapy.Spider):
    name = 'maoyan_proxy'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    def parse(self, response):
        pass
