import redis


class RedisHitCounterMiddleware:

    def __init__(self):
        self.redis = redis.StrictRedis(host='localhost', port=6379, db=0)

    def process_view(self, request, view_func, view_args, view_kwargs):
        self.redis.incr('views')
