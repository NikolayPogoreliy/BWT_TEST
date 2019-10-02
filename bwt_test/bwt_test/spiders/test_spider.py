import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
from scrapy.utils.project import get_project_settings

from bwt_test.items import BwtTestItem


XPATHES = get_project_settings().get('XPATHES')

if not XPATHES:
    raise ValueError('XPATHES is not set. Look at the settings.py')


class TestSpider(scrapy.Spider):
    name = 'test'
    category = ''
    location = ''

    def __get_selector(self, field_name):
        return XPATHES.get(self.category, XPATHES['default'])[field_name]['sel']

    @staticmethod
    def __get_link(link_name):
        return XPATHES.get(link_name)['sel']

    def start_requests(self):
        self.category = getattr(self, 'category', '').lower()
        self.location = getattr(self, 'location', '').upper()
        url = self.__get_link('search_url').format(category=self.category, location=self.location)
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for link in response.xpath(self.__get_link('item_link')):
            yield response.follow(link, self.parse_item)
        next_page = response.xpath(self.__get_link('next_link'))[0]
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_item(self, response):
        item_loader = ItemLoader(item=BwtTestItem(), response=response)
        item_loader.default_input_processor = MapCompose(str.strip)
        item_loader.default_output_processor = Join()
        for field_name in BwtTestItem.fields.keys():
            item_loader.add_xpath(field_name, self.__get_selector(field_name))
        yield item_loader.load_item()
