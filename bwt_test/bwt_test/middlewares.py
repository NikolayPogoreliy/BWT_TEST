import random
from scrapy.utils.project import get_project_settings


class ProxyMiddleware:
    def process_request(self, request, spider):
        request.meta['proxy'] = random.choice(get_project_settings().get('PROXY_LIST'))
        spider.logger.info(f'Using proxy: {request.meta["proxy"]}')
