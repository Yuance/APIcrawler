'''
This method get the request stored
corresponding to the key given in redis and filter the duplicates
'''
import six

def filter_API(redis, request, key):

    is_new_url = bool(redis.pfadd(key + "_filter", request))

    if is_new_url:
        redis.lpush(key, request)

def bytes_to_str(s, encoding='utf-8'):
    """Returns a str if a bytes object is given."""
    if six.PY3 and isinstance(s, bytes):
        return s.decode(encoding)
    return s