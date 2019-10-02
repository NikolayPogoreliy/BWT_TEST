# -*- coding: utf-8 -*-

# Scrapy settings for bwt_test project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'bwt_test'

SPIDER_MODULES = ['bwt_test.spiders']
NEWSPIDER_MODULE = 'bwt_test.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bwt_test (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'bwt_test.middlewares.BwtTestSpiderMiddleware': 543,
#}

# Retry many times since proxies often fail
RETRY_TIMES = 20
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408, 429]

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'bwt_test.middlewares.Response429RetryMiddleware': 90,
    'bwt_test.middlewares.ProxyMiddleware': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
}

PROXY_LIST = [
    'http://78.141.220.172:3128',
    'http://185.44.231.2:34244',
    'http://185.78.221.113:80',
    'http://125.26.7.11:36082',
    'http://88.250.114.75:8118',
    'http://103.205.15.97:8080',
    'http://162.243.159.46:3128',
    'http://223.25.99.163:8080',
    'http://27.147.216.35:48194',
    'http://27.68.131.218:8080',
    'http://103.206.81.7:8080',
    'http://83.219.1.80:43916',
    'http://50.197.20.162:55389',
    'http://185.44.231.2:34244',
    'http://31.129.161.43:52822',
    'http://140.227.230.89:60088',
    'http://5.23.103.98:30979',
    'http://164.160.130.24:8080',
    'http://168.90.140.26:58790',
    'http://92.255.205.227:30359',
    'http://95.68.115.202:53281',
    'http://49.51.70.42:1080',
    'http://46.130.249.18:46282',
    'http://181.129.140.226:39977',
    'http://198.50.214.17:8585',
    'http://159.224.73.208:23500',
    'http://178.32.80.239:1080',
    'http://1.9.71.2:8080',
    'http://201.231.214.242:8888',
    'http://41.208.20.50:8888',
    'http://173.54.193.242:50200',
    'http://178.76.69.132:45014',
    'http://103.141.123.2:41674'
]

# Validation of the selected location
# just comment if you don't need to check
ENABLED_LOCATIONS = ['NY', 'LA', 'SF']

# Validation of the selected category
# just comment if you don't need to check
ENABLED_CATEGORIES = ['restaurants', 'gym', 'spa']

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'bwt_test.pipelines.BwtTestItemToDbPipeline': 100,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


XPATHES = {
    "search_url": {
        "sel": "https://www.yelp.com/search?find_desc={category}&find_loc={location}"
    },
    "item_link": {
        "sel": "//ul/li//p/a[contains(@href, 'biz/')]"
    },
    "next_link": {
        "sel": "//a[contains(@class, 'next-link')]"
    },
    "default": {
        "phone": {
            "sel": "//span[contains(@class,'biz-phone')]/text()"
        },
        "address": {
            "sel": "//div[contains(@class, 'map-box-address')]//address/text()"
        },
        "link": {
            "sel": ".//span[contains(@class,'biz-website')]/a/text()"
        },
        "title": {
            "sel": "//h1/text()"
        },
        "reviews": {
            "sel": "//h1//parent::div/following-sibling::div/div[1]/div[1]/span/text()"
        },
        "about": {
            "sel": "//h3[text()='From the business']/following-sibling::p/text()"
        },
        "working_hours": {
            "sel":  "//table[@class='table table-simple hours-table']//tr/th/text() |"
                    " //table[@class='table table-simple hours-table']//tr/td[1]//span/text()"
        },
        "photo_url": {
            "sel": "//div[@class='showcase-photos' or @class='showcase-photos current']/"
                   "div[contains(@class, 'photo-2')][1]/div[1]//img[1]/@src"
        },
    },
    "restaurants": {
        "phone": {
            "sel": "//p[text()= 'Phone number']/following-sibling::p/text()"
        },
        "address": {
            "sel": "//div[contains(@class, 'stickySidebar__')]//address/p/span/text()"
        },
        "link": {
            "sel": "//div[contains(@class, 'stickySidebar__')]//section//p[text()= 'Business website']"
                   "/following-sibling::a/text()"
        },
        "title": {
            "sel": "//h1/text()"
        },
        "reviews": {
            "sel": "//h1//parent::div/following-sibling::div/div[2]/p//text()"
        },
        "about": {
            "sel": "//h3[text()='About the Business']/parent::div/parent::div"
                   "/following-sibling::div//p/span/span//text()"
        },
        "working_hours": {
            "sel": "//h3[text()='Location & Hours']/parent::div/parent::div"
                   "/following-sibling::div/div[2]/div/div/table//tr//th//text() | "
                   "//h3[text()='Location & Hours']/parent::div/parent::div/following-sibling::div/div[2]/div/div"
                   "/table//tr//td[1]//p/text()"
        },
        "photo_url": {
            "sel": "//div[contains(@class, 'photo-header-media__')][2]//img/@scr"
        },
    }
}

CONNECTION_STRING = "{drivername}://{user}:{passwd}@{host}:{port}/{db_name}?charset=utf8".format(
    drivername="mysql",
    user="demo",
    passwd="demodemo",
    host="localhost",
    port="3306",
    db_name="bwt_test",
)