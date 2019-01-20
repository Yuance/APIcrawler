from apicrawler.loader import redistools as rt
from scrapy_redis.spiders import  RedisSpider, Spider
from scrapy.item import Field, Item
from redis import Redis
import time
import scrapy
import json

class LolSlaveSpider(RedisSpider):

    name = 'lol_slave'
    redis_key = 'match_api:new_url'

    # APIkey = "RGAPI-db483276-d9fc-4b9e-9ca9-b9d48ea2d877"
    matchAPI = "https://na1.api.riotgames.com/lol/match/v4/matches/"
    playerAPI = "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/"


    allowed_domains = ["na1.api.riotgames.com"]
    end_index = 1

    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        # self.allowed_domains = filter(None, domain.split(','))
        api_key = kwargs.pop('key', '')
        self.APIkey = api_key
        super(LolSlaveSpider, self).__init__(*args, **kwargs)

    def make_request_from_data(self, data):

        url = rt.bytes_to_str(data, self.redis_encoding)
        return self.make_requests_from_url(url + "?api_key=" + self.APIkey)

    def parse(self, response):

        # match = it.parse_match_body(self, response.body)
        match = json.loads(response.body)

        # item = MatchItem()
        # item['match_id'] = match['gameId']
        # item['match_details'] = json.dumps(match)

        '''Save the match item'''
        print("MatchID: {}".format(match['gameId']))
        yield match

        '''trace players of a match'''
        player_list = match['participantIdentities']

        for player in player_list:

            player_id = player['player']['accountId']
            time.sleep(1)
            # build player api request
            player_api_request = self.playerAPI + str(player_id) + "?endIndex={}".format(self.end_index) + "&"

            '''Put new matchAPI requests into Redis Queue, with key match_api:start_urls'''
            redis = Redis()

            try:

                rt.filter_API(redis, player_api_request, "player_api:new_url")
                print("For Player: %s, new player_requests sent back to master Queue" % player_id)

            except Exception as e:

                '''print the exception'''
                print(e)
                pass



class MatchItem(Item):

    match_id = Field()
    match_details = Field()