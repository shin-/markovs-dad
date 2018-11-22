import os
import time

from redis import Redis, RedisError


GRAPH_KEY = 'markovs_dad.jokes.graph'


def get_config():
    return {
        'host': os.environ.get('REDIS_HOST'),
        'port': int(os.environ.get('REDIS_PORT')),
        'db': int(os.environ.get('REDIS_DB')),
        'password': os.environ.get('REDIS_PASS'),
    }


def get_redis_client():
    r = Redis(**get_config())
    for i in range(5):
        try:
            r.ping()
            return r
        except RedisError as e:
            time.sleep(i * 2)  # linear backoff, could be better
    raise e


def load_graph_data():
    r = get_redis_client()
    return r.get(GRAPH_KEY)


def save_graph_data(data):
    r = get_redis_client()
    return r.setex(GRAPH_KEY, time=3600 * 8, value=data)
