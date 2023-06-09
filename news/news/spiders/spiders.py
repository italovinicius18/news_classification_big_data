from scrapy import Spider, Request
from bs4 import BeautifulSoup

from .urls import data


# class G1Spider(Spider):
#     name = "news"
#     allowed_domains = ["g1.globo.com"]
#     start_urls = data.g1

#     def start_requests(self):
#         for url in self.start_urls:
#             yield Request(url, meta={"root_url": url}, callback=self.parse)

#     def parse(self, response):
#         for url in response.css(".feed-post-link::attr(href)").getall():
#             # yield title news
#             yield Request(
#                 url,
#                 callback=self.parse_news,
#                 meta={"root_url": response.meta["root_url"], "url": url},
#             )

#         try:
#             next_page = response.css(".load-more a").attrib["href"]
#         except KeyError:
#             next_page = None

#         if next_page:
#             yield Request(next_page, meta={"root_url": next_page}, callback=self.parse)
#         else:
#             print("No more pages")

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


class CNNSpider(Spider):
    name = "news"
    start_urls = data.cnn_brasil

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, meta={"root_url": url}, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, "lxml")
        urls = soup.find_all("loc")
        for url in urls:
            # yield title news
            yield Request(
                url.text,
                callback=self.parse_list,
                meta={"root_url": response.meta["root_url"]},
            )

    def parse_list(self, response):
        soup = BeautifulSoup(response.text, "lxml")
        urls = soup.find_all("loc")
        for url in urls:
            # yield title news
            yield Request(
                url.text,
                callback=self.parse_news,
                meta={"root_url": response.meta["root_url"], "url": url.text},
            )

    def parse_news(self, response):
        yield {
            "parent_url": response.meta["root_url"],
            "url": response.meta["url"],
            "title": response.xpath('//h1[@class="post__title"]/text()').get(),
            "subtitle": response.xpath('//p[@class="post__excerpt"]/text()').get(),
            "author": response.xpath('//p[@class="author__name"]/text()').get(),
            "date": response.xpath('//span[@class="post__data"]/text()').get(),
            "text": " ".join(response.css(".post__content p::text").getall()),
        }


class G1SiteMapSpider(Spider):
    name = "news"
    start_urls = data.g1_site_map

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, meta={"root_url": url}, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, "lxml")
        urls = soup.find_all("loc")
        for url in urls:
            # yield title news
            yield Request(
                url.text,
                callback=self.parse_list,
                meta={"root_url": response.meta["root_url"]},
            )

    def parse_list(self, response):
        soup = BeautifulSoup(response.text, "lxml")
        urls = soup.find_all("loc")
        for url in urls:
            # yield title news
            yield Request(
                url.text,
                callback=self.parse_news,
                meta={"root_url": response.meta["root_url"], "url": url.text},
            )

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


class UolSiteMapSpider(Spider):
    name = "news"
    start_urls = data.uol_site_map

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, meta={"root_url": url}, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, "lxml")
        urls = soup.find_all("loc")
        for url in urls:
            # yield title news
            yield Request(
                url.text,
                callback=self.parse_list,
                meta={"root_url": response.meta["root_url"]},
            )

    def parse_list(self, response):
        soup = BeautifulSoup(response.text, "lxml")
        urls = soup.find_all("loc")
        for url in urls:
            # yield title news
            yield Request(
                url.text,
                callback=self.parse_news,
                meta={"root_url": response.meta["root_url"], "url": url.text},
            )

    def parse_news(self, response):
        yield {
            "parent_url": response.meta["root_url"],
            "url": response.meta["url"],
            "title": response.xpath('//i[@class=" custom-title"]/text()').get(),
            "subtitle": response.xpath(
                '//h2[@class="content-head__subtitle"]/text()'
            ).get(),
            "author": response.xpath('//p[@class="p-author thisOne"]/text()').get(),
            "date": response.xpath(
                '//p[@class="p-author time"]/@ia-date-publish'
            ).get(),
            "text": " ".join(response.css(".text").getall()),
        }
