from django.contrib.auth.models import User
from django.db import models
from pump_app.model_classes.Course import Course

class Lesson(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.TextField(null=True, blank=False)

    description = models.TextField(null=True, blank=False)

    open = models.NullBooleanField(null=True)

    startDate = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)

    endTime = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)

    course = models.ForeignKey(Course, null=False, blank=False, related_name='lessons')