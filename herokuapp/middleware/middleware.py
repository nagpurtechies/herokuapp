from herokuapp.settings import REDIS


class RedisHitCounterMiddleware:

    def __init__(self):
        pass

    def process_view(self, request, view_func, view_args, view_kwargs):
        REDIS.incr('views')
