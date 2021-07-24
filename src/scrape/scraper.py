import scrapy

class Scraper(scrapy.Spider):
    name = None
    start_urls = ['http://example.com/setting_is_overwrited/by_scrape_args']
    desc = None
    search = None

    """
    args expcetation example:
        scrape_args = {
            name: 'example',
            url: 'http://example.com',
            search: [
                {
                    'desc': 'title',
                    'path': '/html/head/title'
                },
                {
                    'desc: 'each_p',
                    'path': '/html/body/div[1]/p'
                }
            ]
        }
    """
    def __init__(self, scrape_args):
        self.name = scrape_args['name']
        self.start_urls = [scrape_args['url']]
        self.search = scrape_args['search']

    def parse(self, response):
        for s in self.search:
            for target in response.xpath(s['xpath']):
                yield { s['desc'] : target.extract() }
