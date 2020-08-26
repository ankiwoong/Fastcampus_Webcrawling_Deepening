from urllib import parse
import scrapy

# 스파이더 종류 : CrawlSpider, XMLFeedSpider, CSVFeedSpider, SitemapSpider
class TestSpider(scrapy.Spider):
    name = "test4"
    allowed_domains = ["blog.scrapinghub.com", "naver.com", "daum.net"]

    # 실행 방법 1
    # 멀티 도메인
    start_urls = [
        "http://blog.scrapinghub.com/",
        "https://www.naver.com",
        "https://www.daum.net",
    ]

    def parse(self, response):
        print(response)

    # 실행 방법 2
    # Request 각각 지정
    # def start_requests(self):
    #     yield scrapy.Request("http://blog.scrapinghub.com/", self.parse1)
    #     yield scrapy.Request("https://www.naver.com", self.parse2)
    #     yield scrapy.Request("https://www.daum.net", self.parse3)

    # def parse1(self, response):
    #     pass

    # def parse2(self, response):
    #     pass

    # def parse3(self, response):
    #     pass
