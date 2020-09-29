import scrapy


def printAll(ls):
    for l in ls:
        print(l)


class GaSpider(scrapy.Spider):

    max_banners = {
        1: 8 * 64 + 72,
        2: 8 * 64 + 72,
        3: 6 * 64 + 72,
        4: 6 * 64 + 72,
        5: 5 * 64 + 72,
        6: 5 * 64 + 72,
        7: 4 * 64 + 72,
        8: 3 * 64 + 72,
        9: 3 * 64 + 72,
        10: 3 * 64 + 72,
        11: 3 * 64 + 72
    }

    name = "ga"

    # allycode => (avg banners, win percentage, cleared percentage)
    results = {}

    def start_requests(self):
        urls = [
            'https://swgoh.gg/g/68989/the-senate-ksdagobahks/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.init)

    def init(self, response):
        # todo need to parse request and find urls
        print("Results:")
        urls = ["https://swgoh.gg/" + x +
                "gac-history/?gac=34&r=1" for x in response.css('a::attr(href)').re(r'/p/\d{9}/')]

        for url in urls:
            # yield scrapy.Request(url=url, callback=self.parse)
            print(url)

        yield scrapy.Request(url=urls[0], callback=self.parse)

    def parse(self, response):
        print("Start")

        ga_info = response.css(
            '.btn.btn-default.dropdown-toggle::text').re(r'.+')
        banners = response.css('.gac-summary--win::text').re(r'Banners: (\d+)')
        battle_results = response.css('.gac-summary__status::text').re(r'\w+')
        banners = response.css('.m-a-0::text').re(r'(\d+) - \d+')
        print(banners)

        print(response.css('.m-a-0::text').get())
        printAll(ga_info)
        ally = response.request.url.split('/')[-3]
        print(ally)

        ga_battles = []
        i = 0

        for battle_result in battle_results:
            if battle_result == "WIN":
                ga_battles.append(int(banners[i]))
                i += 1

        avg_banners = sum(ga_battles) / len(ga_battles)
        win_percentage = battle_results.count("WIN") / len(battle_results)
        # banner_percentage =

        print("Average Banners: %d" % avg_banners)
        print("Win Percentage: %d" % win_percentage)
        # prints("Banner Pecentage %d%" % banner_percentage)

        print("End")
