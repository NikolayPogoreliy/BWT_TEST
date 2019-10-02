import scrapy
from scrapy.loader.processors import Join

from bwt_test.processors import SplitNumbers


class BwtTestItem(scrapy.Item):
    title = scrapy.Field()
    address = scrapy.Field(output_processor=Join(separator=', '))
    phone = scrapy.Field()
    link = scrapy.Field()
    working_hours = scrapy.Field()
    about = scrapy.Field()
    reviews = scrapy.Field(output_processor=SplitNumbers())
    photo_url = scrapy.Field()
