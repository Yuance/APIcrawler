from scrapy import cmdline
from apicrawler import settings

cmdline.execute("scrapy crawl -a key={} lol_master".format(settings.API_KEY).split())