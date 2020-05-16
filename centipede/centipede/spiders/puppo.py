from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class PuppoSpider(CrawlSpider):
    name = 'puppo'
    allowed_domains = [
      # 'www.ilshorthairrescue.com', 
      # 'www.moonsongmals.org', 
      'https://anjingdijual.com'
    ]
    start_urls = [
      # "https://www.ilshorthairrescue.com/adoptable-dogs/",
      # "https://www.moonsongmals.org/adoption/mmrfosters.html",
      # "https://anjingdijual.com/jual-anjing/dalmatian/"
      "https://anjingdijual.com/jual-anjing/pembroke-welsh-corgi/"
    ]

    # rules = ( callback="parse_item", follow=True )

    def parse(self, response):
      print('Processing...' + response.url)