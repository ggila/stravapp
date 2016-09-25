from django.db import models
from django.contrib import admin
import datetime

class Activity(models.Model):
    name = models.CharField(default='', max_length=200)
    sport = models.CharField(default='', max_length=30)
    date = models.DateTimeField(default=datetime.datetime.now())
    end = models.DateTimeField(default=datetime.datetime.now())
    distance = models.FloatField(default=0)

    class Meta:
        ordering = ('date',)

    @property
    def duration(self):
        return self.end - self.date

admin.site.register(Activity)

class TrkPt(models.Model):
    act = models.ForeignKey(Activity, on_delete=models.CASCADE)
    delta = models.DurationField('elapsed time')
    lon = models.FloatField('longitude')
    lat = models.FloatField('latitude')
    ele = models.FloatField('elevation')
    hr = models.PositiveSmallIntegerField('heart rate')   # might be not set
