#! /usr/bin/python
# encoding:utf-8

import redis

def create_redis(params):
    r = redis.StrictRedis(host="127.0.0.1", port=6379)
    r.set("new_date",params)

def get_redis_data():
    pass