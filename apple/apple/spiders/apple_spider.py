import scrapy

class AppleSpider(scrapy.Spider):
    name = "apple"
    start_urls = [
        'https://www.wiggle.co.uk/wahoo-kickr-core-smart-turbo-trainer',
        'https://www.wiggle.co.uk/wahoo-kickr-smart-turbo-trainer-5'
    ]

    def parse(self, response):
        for product in response.xpath('//div[@id="wiggle"]'):
            yield {
                'name': response.xpath('//h1[@id="productTitle"]/text()').get().strip(),
                'price': response.xpath('//p[@class="bem-pricing__product-price js-unit-price"]/text()').get().strip(),
                'image': response.xpath('//img[@id="pdpGalleryImage"]/@src').get(),
            }