# -*- coding: utf-8 -*-
import scrapy


class PuppoSpider(scrapy.Spider):
    name = 'puppo'
    allowed_domains = ['www.puppyfind.com']
    start_urls = ['http://www.puppyfind.com/']

    def parse(self, response):
        pass
