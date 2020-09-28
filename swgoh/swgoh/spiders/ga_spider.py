import scrapy


class GaSpider(scrapy.Spider):
    name = "ga"

    def start_requests(self):
        urls = [
            'https://swgoh.gg/p/146523987/gac-history/?gac=34&r=1'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        banners = response.css('.gac-summary--win::text').re(r'Banners: \d+')
        for banner in banners:
            print(banner[-2:])
        # with open('results', 'wb') as f:
        #     f.write(banners)
