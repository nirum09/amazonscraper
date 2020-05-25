# -*- coding: utf-8 -*-
import scrapy
from scraper.scraper.items import ScraperItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    # allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.in/']

    def parse(self, response):
        data = response.css()

        for item in data:
            each_item=ScraperItem()

            yield each_item
