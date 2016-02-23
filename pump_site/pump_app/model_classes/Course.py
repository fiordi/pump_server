from django.contrib.auth.models import User
from django.db import models
from pump_app.model_classes.CourseCatalog import CourseCatalog


class Course(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.TextField(null=True, blank=False)

    description = models.TextField(null=True, blank=False)

    open = models.NullBooleanField(null=True)

    startDate = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)

    endTime = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)

    if open:
        coursecatalog = models.ForeignKey(CourseCatalog, null=False, blank=False, related_name='Activatedcourse')
    else:
        coursecatalog = models.ForeignKey(CourseCatalog, null=False, blank=False, related_name='Dectivatedcourse')

    def addLesson(self, aWeekDay, aStarTime, aEndTime, aTrainer, aFrequency):
        pass

    def setInfo(self, aName, aDescription, aOpen, aStartDate, aEndDate):
        pass
