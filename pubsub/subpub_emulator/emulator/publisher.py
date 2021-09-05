import redis
import uuid
import random
import time
import json

with open('pubsub/massage.json') as json_file:
    massage = json.load(json_file)
alice_r = redis.Redis(host='localhost', port=6379, db=0)


def pub_msg(deviceId, latitude, longitude):
    deviceId = str(uuid.uuid4()) if not deviceId else deviceId
    latitude = random.random() * 90 if not latitude else latitude
    longitude = random.random() * 90 if not longitude else longitude

    temperature = random.randint(12, 40)
    ts = int(time.time())

    massage['data']['deviceId'] = deviceId
    massage['data']['temperature'] = temperature
    massage['data']['time'] = ts
    massage['data']['location']['latitude'] = latitude
    massage['data']['location']['longitude'] = longitude

    msg_str = json.dumps(massage)
    try:
        alice_r.publish('Temperature', msg_str)
        print(f'Temperature: {temperature} at Time: {ts}')
    except:
        print('Error returned')

    return msg_str


if __name__ == "__main__":
    while True:
        pub_msg()


