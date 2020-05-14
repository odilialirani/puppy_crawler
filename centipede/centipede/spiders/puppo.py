# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor


# class PuppoSpider(CrawlSpider):
#     name = 'puppo'
    # allowed_domains = ['www.ilshorthairrescue.com', 'www.moonsongmals.org']
    # start_urls = [
    #   "https://www.ilshorthairrescue.com/adoptable-dogs/",
    #   "https://www.moonsongmals.org/adoption/mmrfosters.html"
    # ]

#     rules = (
#         Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
#              callback="parse_item",
#              follow=True),)

#     def parse_item(self, response):
#         print('Processing..' + response.url)


import scrapy


class PuppoSpider(scrapy.Spider):
    name = 'puppo'
    allowed_domains = ['www.ilshorthairrescue.com', 'www.moonsongmals.org']
    start_urls = [
      "https://www.ilshorthairrescue.com/adoptable-dogs/",
      "https://www.moonsongmals.org/adoption/mmrfosters.html"
    ]

    def parse(self, response):
      print('Processing...' + response.url)