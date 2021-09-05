import redis


def sub_msg():
    bob_r = redis.Redis(host='localhost', port=6379, db=0)
    bob_p = bob_r.pubsub()

    bob_p.subscribe('Temperature')

    return bob_p.get_message()




