from django.contrib.auth.models import User
from django.db import models
from pump_app.model_classes.Course import Course

class Lesson(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.TextField(null=True, blank=False)

    description = models.TextField(null=True, blank=False)

    open = models.NullBooleanField(null=True)

    date = models.DateField(null=True, auto_now=False, auto_now_add=False)

    startTime = models.TimeField(null=True, auto_now=False, auto_now_add=False)

    endTime = models.TimeField(null=True, auto_now=False, auto_now_add=False)

    course = models.ForeignKey(Course, null=True, blank=True, related_name='lessons')

    def __unicode__(self):
        return str(self.date)
