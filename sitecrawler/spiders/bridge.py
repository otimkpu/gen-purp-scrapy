import scrapy
from scrapy.loader import ItemLoader
from sitecrawler.items import SitecrawlerItem


class BridgeSpider(scrapy.Spider):
    name = 'bridge'
    allowed_domains = ['bp.com']
    start_urls = ['https://www.bp.com/en/global/corporate/sustainability.html']

    def parse(self, response):
        file_url = response.xpath("//a[contains(@href,'pdf') and (contains(@href, '2019') or contains(@href, '2020'))]/@href").extract()
        for link in file_url:
            loader = ItemLoader(item=SitecrawlerItem(), selector=link)
            absolute_url = response.urljoin(link[1:])
            loader.add_value('file_urls', absolute_url)
            yield loader.load_item()



