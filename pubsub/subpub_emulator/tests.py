import datetime
import time

from django.test import TestCase
from django.utils import timezone

from . import models


class TemperatureModelTests(TestCase):

    def test_was_published_recently(self):
        ts = time.mktime((timezone.now() + datetime.timedelta(seconds=30)).timetuple)
        temperature = Temperature(device=1, time=ts, temperature=12)
        self.assertIs(temperature.was_published_recently(), False)