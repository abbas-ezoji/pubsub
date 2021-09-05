import json

from .publisher import pub_msg
from .db import get_db
from sqlalchemy import create_engine

DATABASES = get_db()

# ----------------------- get data -------------------------------------------#
USER = DATABASES['pubsub']['USER']
PASSWORD = DATABASES['pubsub']['PASSWORD']
HOST = DATABASES['pubsub']['HOST']
PORT = DATABASES['pubsub']['PORT']
NAME = DATABASES['pubsub']['NAME']

con_string = f'mysql://{USER}:{PASSWORD}@{HOST}'
engine = create_engine(con_string)


devices = engine.execute('SELECT * FROM pubsub.subpub_emulator_device')

for d in devices:
    device_id = d.device_id
    latitude = d.latitude
    longitude = d.longitude

    while True:
        msg = pub_msg(device_id=device_id, latitude=latitude, longitude=longitude)
        data = json.load(msg)



