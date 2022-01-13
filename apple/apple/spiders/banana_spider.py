import scrapy
from scrapy.loader import ItemLoader
from apple.items import Product

# TODO: load urls and xpaths from the external file or *arg

class BananaSpider(scrapy.Spider):
    name = "banana"
    start_urls = [
        'https://www.wiggle.co.uk/wahoo-kickr-core-smart-turbo-trainer',
        'https://www.wiggle.co.uk/wahoo-kickr-smart-turbo-trainer-5',
        'https://www.wiggle.co.uk/dhb-aeron-lab-carbon-road-shoe-dial'
    ]
    
    # TODO: nested loader for the options
    # TODO: clean received date (i/o processors)

    def parse(self, response):

        l = ItemLoader(item=Product(), response=response)
        l.add_xpath('name', '//h1[@id="productTitle"]/text()')
        l.add_xpath('price', '//p[@class="bem-pricing__product-price js-unit-price"]/text()')
        l.add_xpath('image', '//img[@id="pdpGalleryImage"]/@src')
        l.add_xpath('options', '//div[@class="bem-sku-selector__option-wrapper"]/ul/@name')

    
        return l.load_item()