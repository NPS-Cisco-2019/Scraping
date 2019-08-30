import scrapy


class QuotesSpider(scrapy.Spider):
    name = "answerbot"

    def start_requests(self):
        urls = ['https://brainly.in/question/694122']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.log("YOOOOOOOO")
        with open('brainlyyyyy.txt', 'a+') as f:
            f.write('yeet')
            self.log("DOOOOO SOMETHINGNGG")
            f.write(str(response.xpath('//script[@type="application/ld+json"]/text()').getall()))
            f.close
        
