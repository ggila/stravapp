from django.db import models

class Activity(models.Model):
    name = models(CharField(max_length=200))
    sport = models.CharField(max_length=30)
    date = models.DateTimeField('date')
    end = models.DurationField('end')
    distance = models.FloatField('distance')

    class Meta:
        ordering = (created,)

    @property
    def duration(self):
        return self.end - self.date

class TrkPt(models.Model):
    act = models.ForeignKey(Activity, on_delete=models.CASCADE)
    delta = models.DurationField('elapsed time')
    lon = models.FloatField('longitude')
    lat = models.FloatField('latitude')
    ele = models.FloatField('elevation')
    hr = models.PositiveSmallIntegerField('heart rate')   # might be not set
