import scrapy
import json
from scrapy_redis.spiders import RedisSpider
from redis import Redis
import time
from apicrawler.loader import redistools as rt



class LolMasterSpider(RedisSpider):

    name = 'lol_master'
    redis_key = 'player_api:new_url'

    # APIkey = "RGAPI-db483276-d9fc-4b9e-9ca9-b9d48ea2d877"
    matchAPI = "https://na1.api.riotgames.com/lol/match/v4/matches/"
    playerAPI = "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/"

    allowed_domains = ["na1.api.riotgames.com"]

    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        # self.allowed_domains = filter(None, domain.split(','))
        api_key = kwargs.pop('key', '')
        self.APIkey = api_key
        super(LolMasterSpider, self).__init__(*args, **kwargs)

    def make_request_from_data(self, data):

        url = rt.bytes_to_str(data, self.redis_encoding)
        return self.make_requests_from_url(url + "api_key=" + self.APIkey)


    def parse(self, response):

        time.sleep(1)
        match_list = json.loads(response.body)
        match_list = match_list['matches']

        redis = Redis()
        for match in match_list:
            match_id = match['gameId']

            match_api_request = self.matchAPI + str(match_id)

            '''Put new matchAPI requests into Redis Queue, with key match_api:start_urls'''
            try:
                rt.filter_API(redis, match_api_request, "match_api:new_url")
                print("new match:%s requests has been added to queue" % match_id)

            except Exception as e:
                '''print the exception'''
                print(e)
                pass



