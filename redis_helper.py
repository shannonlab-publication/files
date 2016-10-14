# -*- coding: utf-8 -*-
"""
Redisを使いやすく、Pickleと連携したもの
"""

try:
    import cPickle as pickle
except:
    import pickle
# Redis
import redis

redis_con = redis.StrictRedis(host='localhost', port=6379, db=0)
# 期限(秒数)
# 3時間
EXPIRE_TIME = 3 * 60 * 60
# たまたま他のアプリケーションと名前がかぶることが有るため
# ベースとなるキーを決めておく
KEY_BASE = "TEST"


def set_value(key, value):
    """
    値をセット(上書きしない)
    """
    my_key = KEY_BASE + key
    redis_con.set(my_key, pickle.dumps(value))
    redis_con.expire(my_key, EXPIRE_TIME)




def get_value(key):
    """
    値を取得
    """
    my_key = KEY_BASE + key
    pickled_value = redis_con.get(my_key)
    if pickled_value is None:
        return None
    # pickle化された値を戻す
    return pickle.loads(pickled_value)


def delete_value(key):
    """
    値を削除
    """
    my_key = KEY_BASE + key
    return redis_con.delete(my_key)


def exists(key):
    """
    キーが存在するかどうか
    """
    my_key = KEY_BASE + key
    return redis_con.exists(my_key)

def set_redis(token ,key, value):
    """
    set_value（）のキーにトークンを付け加えたもの
    """
    new_key = token + '_' + key
    set_value(new_key, value)

def get_redis(token ,key):
    """
    get_value（）のキーにトークンを付け加えたもの
    """     
    new_key = token + '_' + key
    return get_value(new_key)
    
