import datetime
from django.utils import timezone
from django.db import models
from django.db.models import Avg, Max, Min, Count
from .task import pub_async, sub_async

device_status = (
    (1, ("Send")),
    (0, ("Stop")),
)


class Device(models.Model):
    name = models.CharField('Name', max_length=60)
    device_id = models.CharField('DeviceId', max_length=60)
    latitude = models.FloatField('Latitude')
    longitude = models.FloatField('Longitude')
    status = models.IntegerField(choices=device_status, null=True, blank=True)

    def max_temp(self):
        d = Device.objects.filter(id=self.id).annotate(num_temp=Max('temperature'))
        return d[0].num_temp

    def min_temp(self):
        d = Device.objects.filter(id=self.id).annotate(num_temp=Min('temperature'))
        return d[0].num_temp

    def avg_temp(self):
        d = Device.objects.filter(id=self.id).annotate(num_temp=Avg('temperature'))
        return d[0].num_temp

    def count_temp(self):
        d = Device.objects.filter(id=self.id).annotate(num_temp=Count('temperature'))
        return d[0].num_temp

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Device'

    def save(self, *args, **kwargs):
        if not self.id:
            super().save(*args, **kwargs)

        if self.status == 1:
            pub_async.delay(device_id=self.device_id, latitude=self.latitude, longitude=self.longitude)

        super(Device, self).save(*args, **kwargs)


class Temperature(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    time = models.IntegerField()
    temperature = models.IntegerField()

    def __str__(self):
        return self.device.name + '--' + str(self.temperature) + '--' + str(self.time)

    class Meta:
        verbose_name_plural = 'Device Temperatures'

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(hours=1) <= datetime.fromtimestamp(self.time) <= now


