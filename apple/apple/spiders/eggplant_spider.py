import scrapy
from apple.items import Product, ProductDetails

# set up user agent (perhaps variable)

class EggplantSpider(scrapy.Spider):
    name = "eggplant"

    # add external list here
    start_urls = [
        # 'https://www.wiggle.co.uk/wahoo-kickr-core-smart-turbo-trainer',
        # 'https://www.wiggle.co.uk/wahoo-kickr-smart-turbo-trainer-5',
        'https://www.wiggle.co.uk/dhb-aeron-lab-carbon-road-shoe-dial',
        # 'https://www.wiggle.co.uk/dhb-aeron-winter-weight-merino-sock'
    ]

    def parse(self, response):        

        for product in response.xpath('//div[@id="wiggle"]'):
            
            name = product.xpath('//h1[@id="productTitle"]/text()').get().strip()
            price = product.xpath('//p[@class="bem-pricing__product-price js-unit-price"]/text()').get().strip()
            image = product.xpath('//img[@id="pdpGalleryImage"]/@src').get()

            item = Product()

            
            item_options = []
            options = response.xpath('//div[@class="bem-sku-selector__option sku-items-children  js-size-selections hide"]')

            for option in options:
                
                option_name = option.xpath('./@data-colour').get()
                choices = option.xpath('.//ul/li')

                options_data = []
                for choice in choices:
                    
                    # add nested item here
                    # TODO: do not add info if data == None
                    item_details = ProductDetails()
                    item_details['title'] = choice.xpath('./@title').get()
                    item_details['colour'] = choice.xpath('./input/@data-colour').get()
                    item_details['price'] = choice.xpath('./input/@data-unit-price').get()
                    item_details['availability'] = choice.xpath('./input/@data-available-to-order').get()

                    options_data.append(item_details)

                selection = {option_name: options_data}
                item_options.append(selection)
 
            item['name'] = name
            item['price'] = price
            item['image'] = image
            item['options'] = item_options

            yield item
     

