# web_scraper_duo
Learning web scraping with Scrapy
Sample Web Scraper for wiggle.co.uk
Sample Web Scraper for bestbuy.com


## spiders:

#### eggplant spider
*for: www.wiggle.co.uk*
Data extraction - xpaths
Relative xpath used to get the data


Sample data: apple/test7.json

#### fingerlime spider
*for: www.bestbuy.com*
Data extraction from the "<script/>" element.
Chompjs used to get convert contents of the "<script/>" tag from a string to a python list. Then, json data from the list is being extracted.

- Sample data: apple/test_bb_5.json
- dependancies: chompjs

