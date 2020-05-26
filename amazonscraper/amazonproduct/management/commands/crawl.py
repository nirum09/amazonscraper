from django.core.management.base import BaseCommand, CommandError
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
# from scraper.scraper.spiders.amazon import AmazonSpider
from amazonproduct.scraper.scraper.spiders.amazon import AmazonSpider

class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())

        process.crawl(AmazonSpider)
        process.start()