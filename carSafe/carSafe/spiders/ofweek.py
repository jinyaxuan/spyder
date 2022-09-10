import scrapy


class OfweekSpider(scrapy.Spider):
    name = 'ofweek'
    allowed_domains = ['nev.ofweek.com']
    start_urls = ['http://nev.ofweek.com/']

    def parse(self, response):
        title = response.xpath('//html/body/div[3]/div/div[1]/div[2]/div[2]/div[1]/h2/a/text()').extract()
        href = response.xpath('//html/body/div[3]/div/div[1]/div[2]/div[2]/div[1]/h2/a/@href').extract()
        print(href, title)
        pass
 