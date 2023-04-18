from scrapy import Spider, Request
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from urls import data


class G1Spider(Spider):
    name = "news"
    allowed_domains = ["g1.globo.com"]
    start_urls = data.g1

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, meta={"root_url": url}, callback=self.parse)

    def parse(self, response):
        for url in response.css(".feed-post-link::attr(href)").getall():
            # yield title news
            yield Request(
                url,
                callback=self.parse_news,
                meta={"root_url": response.meta["root_url"], "url": url},
            )

        next_page = response.css(".load-more a").attrib["href"]

        if next_page:
            yield Request(next_page, meta={"root_url": next_page}, callback=self.parse)
        else:
            print("No more pages")

    def parse_news(self, response):
        yield {
            "parent_url": response.meta["root_url"],
            "url": response.meta["url"],
            "title": response.xpath('//h1[@class="content-head__title"]/text()').get(),
            "subtitle": response.xpath(
                '//h2[@class="content-head__subtitle"]/text()'
            ).get(),
            "author": response.xpath(
                '//p[@class="content-publication-data__from"]/@title'
            ).get(),
            "date": response.xpath("//time/@datetime").get(),
            "text": "".join(response.css(".content-text__container ::text").getall()),
        }


# class G1Spider(Spider):
#     name = "news"
#     allowed_domains = ["g1.globo.com"]
#     start_urls = []

#     for url in g1:
#         template = f"{url}index/feed/pagina-<number>.ghtml"
#         for i in range(1, 10):
#             start_urls.append(template.replace("<number>", str(i)))

#     def start_requests(self):
#         for url in self.start_urls:
#             yield Request(url, meta={'root_url': url})

#     def parse(self, response):
#         for url in response.xpath(
#             '//div[@class="_evg"]//a[contains(@href, "https://g1.globo.com/")]/@href'
#         ).getall():
#             yield Request(url, callback=self.parse_news, meta={"root_url": response.meta["root_url"], "url": url})

#     def parse_news(self, response):
#         yield {
#             "parent_url": response.meta["root_url"],
#             "url": response.meta["url"],
#             "title": response.xpath('//h1[@class="content-head__title"]/text()').get(),
#             "subtitle": response.xpath(
#                 '//h2[@class="content-head__subtitle"]/text()'
#             ).get(),
#             "author": response.xpath(
#                 '//p[@class="content-publication-data__from"]/@title'
#             ).get(),
#             "date": response.xpath("//time/@datetime").get(),
#             "text": "".join(response.css(".content-text__container ::text").getall()),
#         }
