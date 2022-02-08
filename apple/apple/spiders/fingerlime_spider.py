import scrapy
from apple.items import Product, BB_Variations_Details
import chompjs

# Bestbuy.com


class FignerlimeSpider(scrapy.Spider):
    name = "fingerlime"

    # add external list here
    start_urls = [
        'https://www.bestbuy.com/site/insignia-32-class-n10-series-led-hd-tv/6395127.p?skuId=6395127',
        'https://www.bestbuy.com/site/microsoft-surface-go-3-10-5-touch-screen-intel-pentium-gold-4gb-memor-y-64gb-emmc-device-only-latest-model-platinum/6478759.p?skuId=6478759',
        'https://www.bestbuy.com/site/samsung-galaxy-tab-a7-lite-8-7-32gb-with-wi-fi-dark-gray/6464584.p?skuId=6464584'

    ]

    def parse(self, response):        

        for product in response.xpath('//div[@class="container-v2"]'):
            
            name = product.xpath('//div[@class="shop-product-title"]//h1/text()').get()
            price = product.xpath('//div[contains(@class, "price-box")]//div[@class="priceView-hero-price priceView-customer-price"]/span[@aria-hidden]/text()').get()
            image = product.xpath('//img[@class="primary-image"]/@src').get()

            item = Product()

            options_script = response.xpath('//*[contains (@id, "shop-product-variations")]/script[3]/text()').get()
            
            # parse script to json using chompjs 
            options_data = chompjs.parse_js_object(options_script, unicode_escape=True, jsonlines=True)
            filtered_data = options_data[1]

            # extract json data
            item_options = []
            
            for category in filtered_data['categories']:

                variation_type = [category]
    
                variation_details = BB_Variations_Details()
                variation_details['name'] = variation_type[0]['displayName']
                variation_details['variations'] = variation_type[0]['variations']

                item_options.append(variation_details)
 
            item['name'] = name
            item['price'] = price
            item['image'] = image
            item['options'] = item_options

            yield item
     

