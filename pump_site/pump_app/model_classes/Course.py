from django.contrib.auth.models import User
from django.db import models
from pump_app.model_classes.CourseCatalog import CourseCatalog
import datetime


class Course(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.TextField(null=True, blank=False)

    description = models.TextField(null=True, blank=False)

    open = models.NullBooleanField(null=True)

    startDate = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)

    endTime = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)

    if open:
        coursecatalog = models.ForeignKey(CourseCatalog, null=False, blank=False, related_name='Activatedcourses')
    else:
        coursecatalog = models.ForeignKey(CourseCatalog, null=False, blank=False, related_name='Dectivatedcourses')
    # startDate e endDate sono degli oggetti di tipo datetime
    def addLesson(self, startDate, endDate, startTime, endTime, frequency):
        from pump_app.model_classes.Lesson import Lesson

        while startDate <= endDate:
            lesson = Lesson()

            lesson.date = startDate
            startDate = startDate + datetime.timedelta(days=frequency)
            lesson.startTime = startTime
            lesson.endTime = endTime
            lesson.Course = self
            lesson.save()


    def setInfo(self, aName, aDescription, aOpen, aStartDate, aEndDate):
        pass

    def __unicode__(self):
        return self.name
