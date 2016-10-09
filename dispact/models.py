from django.db import models
from django.contrib import admin
import datetime

class Activity(models.Model):
    name = models.CharField(default='', max_length=200)
    sport = models.CharField(default='', max_length=30)
    date = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        ordering = ('date',)

    @property
    def distance(self):
        return 0.

    @property
    def end(self):
        return self.date

    @property
    def duration(self):
        return self.end - self.date

admin.site.register(Activity)

class Track(models.Model):
    act = models.ForeignKey(Activity, on_delete=models.CASCADE)
    delta = models.DurationField('elapsed time')
    lon = models.FloatField('longitude')
    lat = models.FloatField('latitude')
    ele = models.FloatField('elevation')
    hr = models.SmallIntegerField('heart rate')   # might be not set

    class Meta:
        pass
