from apicrawler.loader import redistools as rt
from scrapy_redis.spiders import  RedisSpider
from scrapy.item import Field, Item
from redis import Redis
import time
import scrapy
import json

class LolSlaveSpider(RedisSpider):

    name = 'lol_slave'
    redis_key = 'match_api:new_url'

    APIkey = "RGAPI-942f086a-c63e-4839-b02e-902db4cdc0ca"
    matchAPI = "https://na1.api.riotgames.com/lol/match/v4/matches/"
    playerAPI = "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/"


    allowed_domains = ["na1.api.riotgames.com"]
    end_index = 1

    def parse(self, response):

        # match = it.parse_match_body(self, response.body)
        match = json.loads(response.body)

        item = MatchItem()
        item['match_id'] = match['gameId']
        # TODO
        item['match_details'] = match

        '''Save the match item'''
        print("MatchID: {}".format(match['gameId']))

        '''trace players of a match'''
        player_list = match['participantIdentities']

        for item in player_list:

            player_id = item['player']['accountId']
            time.sleep(1)
            # build player api request
            player_api_request = self.playerAPI + str(player_id) + "?endIndex={}".format(self.end_index) + "&api_key={}".format(self.APIkey)

            '''Put new matchAPI requests into Redis Queue, with key match_api:start_urls'''
            redis = Redis()

            try:

                rt.filter_API(redis, player_api_request, "player_api:new_url")
                print("For Player: %s, new player_requests sent back to master Queue", player_id)

            except Exception as e:

                '''print the exception'''
                print(e)
                pass

        yield item

class MatchItem(Item):

    match_id = Field()
    match_details = Field()