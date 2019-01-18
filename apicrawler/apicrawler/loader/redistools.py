'''
This method get the request stored
corresponding to the key given in redis and filter the duplicates
'''
def filter_API(redis, request, key):

    is_new_url = bool(redis.pfadd(key + "_filter", request))

    if is_new_url:
        redis.lpush(key, request)