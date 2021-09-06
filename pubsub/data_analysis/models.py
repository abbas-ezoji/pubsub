from django.db import models


class STL(models.Model):
    datetime = models.DateTimeField()
    temperature = models.FloatField()
    residual = models.FloatField()
    trend = models.FloatField()
    seasonal = models.FloatField()
    weights = models.FloatField()
    baseline = models.FloatField()
    score = models.FloatField()
    anomaly = models.IntegerField

    def __str__(self):
        return str(self.datetime)

    class Meta:
        verbose_name_plural = 'STL TimeSeries Analysis'

