import scrapy


def printAll(ls):
    for l in ls:
        print(l)


class GaSpider(scrapy.Spider):

    defenses = {
        1: 9,
        2: 9,
        3: 7,
        4: 7,
        5: 6,
        6: 6,
        7: 5,
        8: 4,
        9: 4,
        10: 4,
        11: 4
    }

    name = "ga"

    def start_requests(self):
        urls = [
            'https://swgoh.gg/p/146523987/gac-history/?gac=34&r=1',
            'https://swgoh.gg/p/146523987/gac-history/?gac=33',
            'https://swgoh.gg/p/146523987/gac-history/?gac=34&r=3&a=d'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print("Start")

        ga_info = response.css(
            '.btn.btn-default.dropdown-toggle::text').re(r'.+')
        banners = response.css('.gac-summary--win::text').re(r'Banners: (\d+)')
        battle_results = response.css('.gac-summary__status::text').re(r'\w+')

        printAll(ga_info)

        ga_battles = []
        i = 0

        for battle_result in battle_results:
            if battle_result == "WIN":
                ga_battles.append(int(banners[i]))
                i += 1

        avg_banners = sum(ga_battles) / len(ga_battles)
        win_percentage = battle_results.count("WIN") / len(battle_results)

        print("Avg. Banners: %d" % avg_banners)
        print("")

        print("End")
