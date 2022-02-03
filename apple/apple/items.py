# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Product(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    image = scrapy.Field()
    options = scrapy.Field()

class ProductDetails(scrapy.Item):
    title = scrapy.Field()
    colour = scrapy.Field()
    price = scrapy.Field()
    availability = scrapy.Field()

class ProductOption(scrapy.Item):
    option = scrapy.Field()
    selection = scrapy.Field()
