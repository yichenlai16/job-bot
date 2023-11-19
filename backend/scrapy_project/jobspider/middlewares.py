# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from collections import defaultdict
import json
import random
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class JobspiderSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class JobspiderDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class RandomProxyMiddleware(HttpProxyMiddleware):
    proxyList = ['http://114.35.237.117:4145',
                 'http://210.61.216.66:33990',
                 'http://210.61.91.71:5678',
                 'http://114.33.10.109:5678',
                 'http://60.251.122.153:5678',
                 'http://59.127.185.70:1088',
                 'http://59.125.141.168:5678',
                 'http://210.61.91.72:5678'
                 ]

    # Downloader Middleware的核心方法，只有實現了其中一個或多個方法才算自定義了一個Downloader Middleware
    def process_request(self, request, spider):
        # 隨機從其中選擇一個，並去除左右兩邊空格
        proxy = random.choice(self.proxyList).strip()
        # 列印結果出來觀察
        print("this is request ip:" + proxy)
        # 設定request的proxy屬性的內容為代理ip
        request.meta['proxy'] = proxy

    # Downloader Middleware的核心方法，只有實現了其中一個或多個方法才算自定義了一個Downloader Middleware
    def process_response(self, request, response, spider):
        # 請求失敗不等於200
        if response.status != 200:
            # 重新選擇一個代理ip
            proxy = random.choice(self.proxyList).strip()
            print("this is response ip:" + proxy)
            # 設定新的代理ip內容
            request.mete['proxy'] = proxy
            return request
        return response
