import scrapy


class TestSpider(scrapy.Spider):
    name = "test2"
    allowed_domains = ["blog.scrapinghub.com"]
    start_urls = ["https://blog.scrapinghub.com/"]

    def parse(self, response):
        """
        :parm : response
        :return : Title Text
        """

        # 2가지(CSS Selector, XPath)
        # getall() <-> get(), extract() <-> extract_first()

        # 예제 1(CSS Selector)
        # css
        # 출력 옵션
        # -o 파일명.확장자 , -t 파일 타입(json, jsonlines, jl, csv, xml, marshal, pickle)
        # for text in response.css("div.post-header h2 a::text").getall():
        # Return Type : Request, BaseItem, dictionary, None
        # yield {"text": text}

        # 예제 2(Xpath)
        for i, text in enumerate(
            response.xpath('//div[@class="post-header"]/h2/a/text()').getall()
        ):
            yield {"num": i, "text": text}
