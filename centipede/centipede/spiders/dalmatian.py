import scrapy

class DalmatianSpider(scrapy.Spider):
  name = "dalmatian"

  start_urls = [
    "https://anjingdijual.com/jual-anjing/dalmatian/"
  ]
  def parse(self, response):
    for post in response.css('.my-row-item .col-xs-6 a::attr(href)').getall():
      print(post)