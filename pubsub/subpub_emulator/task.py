from __future__ import absolute_import, unicode_literals
import time
import json
from celery import task
from celery.utils.log import get_task_logger
from .emulator.publisher import pub_msg
from .emulator.subscriber import sub_msg
from .models import *

logger = get_task_logger(__name__)


@task(bind=True, name="test")
def test(self, a, b):
    return a + b


@task(bind=True, name="PublishMassage")
def pub_async(self, device_id, latitude, longitude):
    device = Device.obejcts.get(device_id=device_id)
    status = device.status
    while status:
        logger.info(f"Publishing deviceId ={device_id}")
        try:
            logger.info("Start:")
            q = pub_msg(deviceId=device_id, latitude=latitude, longitude=longitude)
        except Exception as e:
            logger.error(e)
            q = ''
        time.sleep(2)
        status = device.status


@task(bind=True, name="SubscribeMassage")
def sub_async(self):
    logger.info(f"Subscribing Massages")
    while True:
        msg = sub_msg()
        data = json.loads(msg)

        device_id = data['data']['deviceId']
        ts = data['data']['time']
        temperature = data['data']['temperature']

        device = Device.obejcts.get(device_id=device_id)

        _id = device.id
        name = device.name

        temperature_obj = Temperature(device=device, time=ts, temperature=temperature)
        temperature_obj.save()

        print(f'device: {name} -- time: {ts} -- temperature: {temperature}')


