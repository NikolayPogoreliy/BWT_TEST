import random
import time
from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.utils.project import get_project_settings
from scrapy.utils.response import response_status_message


class ProxyMiddleware:
    def process_request(self, request, spider):
        request.meta['proxy'] = random.choice(get_project_settings().get('PROXY_LIST'))
        spider.logger.info(f'Using proxy: {request.meta["proxy"]}')


class Response429RetryMiddleware(RetryMiddleware):
    def __init__(self, crawler):
        super().__init__(crawler.settings)
        self.crawler = crawler

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_response(self, request, response, spider):
        if request.meta.get('dont_retry', False):
            return response
        if response.status == 429 and not request.meta.get('proxy'):
            self.crawler.engine.pause()
            time.sleep(60)
            self.crawler.engine.unpause()
            reason = response_status_message(response.status)
            return self._retry(request, reason, spider) or response
        if response.status in self.retry_http_codes:
            reason = response_status_message(response.status)
            return self._retry(request, reason, spider) or response
        return response