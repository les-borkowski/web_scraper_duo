import scrapy

# set up user agent (perhaps variable)

class CherrySpider(scrapy.Spider):
    name = "cherry"

    # add external list here
    start_urls = [
        'https://www.wiggle.co.uk/wahoo-kickr-core-smart-turbo-trainer',
        'https://www.wiggle.co.uk/wahoo-kickr-smart-turbo-trainer-5',
        'https://www.wiggle.co.uk/dhb-aeron-lab-carbon-road-shoe-dial'
    ]

    def parse(self, response):        

        for product in response.xpath('//div[@id="wiggle"]'):
            
            name = product.xpath('//h1[@id="productTitle"]/text()').get().strip()
            price = product.xpath('//p[@class="bem-pricing__product-price js-unit-price"]/text()').get().strip()
            image = product.xpath('//img[@id="pdpGalleryImage"]/@src').get()

            options_list = []
            options = product.xpath('//div[@class="bem-sku-selector__option-wrapper"]/ul').getall()
            for option in options:
                # this part needs reviewing
                option_name = product.xpath('//div[@class="bem-sku-selector__option-wrapper"]/ul/@name').get()
                option_choices = product.xpath('//div[@class="bem-sku-selector__option-wrapper"]/ul/li/@title').getall()
                selection = {option_name: option_choices}
                options_list.append(selection)
 
            yield {
                'name': name,
                'price': price,
                'image': image,
                'options':options_list 
            }
     

