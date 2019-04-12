from scrapy import cmdline
from apicrawler import settings
cmdline.execute("scrapy crawl -a key={} lol_slave".format(settings.API_KEY).split())
