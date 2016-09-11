from django.db import models

class Activity(models.Model):
    sport = models.CharField(max_length=30)
    date = models.DateTimeField('date')
    duration = models.DurationField('elapsed time')
    distance = models.FloatField('distance')

class TrkPt(models.Model):
    act = models.ForeignKey(Activity, on_delete=models.CASCADE)
    delta = models.DurationField('elapsed time')
    lon = models.FloatField('longitude')
    lat = models.FloatField('latitude')
    ele = models.FloatField('elevation')
    hr = models.PositiveSmallIntegerField('heart rate')   # might be not set
