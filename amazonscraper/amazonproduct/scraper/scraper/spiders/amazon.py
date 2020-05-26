# -*- coding: utf-8 -*-
import scrapy
from amazonproduct.scraper.scraper.items import ScraperItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    # allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.in/s?k=samsung&ref=nb_sb_noss_2']

    def parse(self, response):
        data = response.css()

        for item in data:
            each_item=ScraperItem()

            each_item['item_name']= item.css(".a-color-base.a-text-normal").css('::text').extract()
            each_item['item_price'] = item.css(".a-price-whole::text").extract()
            each_item['item_rating'] = item.css(".aok-align-bottom::text").extract()
            each_item['item_numrating'] = item.css(".a-size-small .a-size-base").css('::text').extract()
            yield each_item
