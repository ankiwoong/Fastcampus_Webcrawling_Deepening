import scrapy
from ..items import ItArticle


class TestSpider(scrapy.Spider):
    name = "test6"
    allowed_domains = ["computerworld.com"]
    start_urls = ["https://www.computerworld.com/news"]

    # 메인 페이지  순회
    def parse(self, response):
        """
        :param : response
        :return : Request
        """
        for url in response.css(
            "div.river-well > div.post-cont > div.eyebrow > h3 > a::attr(href)"
        ).extract():
            yield scrapy.Request(response.urljoin(url), self.parse_article)

    def parse_article(self, response):
        """
        :param : response
        :return : Request
        """
        item = ItArticle()

        item["title"] = response.xpath('//h1[@itemprop="headline"]/text()').get()
        item["img_url"] = response.xpath('//img[@itemprop="contentUrl"]/@src').get()
        item["contents"] = "".join(
            response.xpath('//div[@itemprop="articleBody"]/p/text()').getall()
        )

        print(dict(item))
        print(dir(dict(item)))

        yield item
