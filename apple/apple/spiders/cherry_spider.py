import scrapy
from apple.items import Product, ProductOptions

# set up user agent (perhaps variable)

class CherrySpider(scrapy.Spider):
    name = "cherry"

    # add external list here
    start_urls = [
        # 'https://www.wiggle.co.uk/wahoo-kickr-core-smart-turbo-trainer',
        # 'https://www.wiggle.co.uk/wahoo-kickr-smart-turbo-trainer-5',
        'https://www.wiggle.co.uk/dhb-aeron-lab-carbon-road-shoe-dial'
    ]

    def parse(self, response):        

        for product in response.xpath('//div[@id="wiggle"]'):
            
            name = product.xpath('//h1[@id="productTitle"]/text()').get().strip()
            price = product.xpath('//p[@class="bem-pricing__product-price js-unit-price"]/text()').get().strip()
            image = product.xpath('//img[@id="pdpGalleryImage"]/@src').get()

            item = Product()
            item_options = ProductOptions()

            
            item_options['option'] = []
            options = response.xpath('//div[@class="bem-sku-selector__option-wrapper"]/ul[li]')

            for option in options:
                
                # add nested item here, don't add data if value == '' or None
                # fix json encoding
                option_name = option.xpath('./@name').get()
                choices = option.xpath('./li')

                item_options['selection'] = []
                for choice in choices:
                    single_choice = {'title': choice.xpath('./@title').get(), 'colour': choice.xpath('./input/@data-colour').get(), 'price': choice.xpath('./input/@data-unit-price').get(), 'availability': choice.xpath('./input/@data-available-to-order').get()}
                    item_options['selection'].append(single_choice)
        
                selection = {option_name: item_options['selection']}
                item_options['option'].append(selection)
 
            item['name'] = name
            item['price'] = price
            item['image'] = image
            item['options'] = item_options

            yield item
     

