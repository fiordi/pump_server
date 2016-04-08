from django.contrib.auth.models import User
from django.db import models
from pump_app.model_classes.CourseCatalog import CourseCatalog
import datetime


class Course(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.TextField(null=True, blank=False, default='Undefined')

    description = models.TextField(null=True, blank=False)

    closed = models.BooleanField(null=False, default=False)

    subscrNumber = models.IntegerField(null=False, default=False)

    activated = models.BooleanField(null=False, default=False)

    startDate = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)

    endDate = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)

    confirmed = models.BooleanField(null=False, default=False)


    if activated:
        coursecatalog = models.ForeignKey(CourseCatalog, null=True, blank=False, on_delete=models.CASCADE, related_name='activatedcourses')
    else:
        coursecatalog = models.ForeignKey(CourseCatalog, null=True, blank=False, on_delete=models.CASCADE, related_name='deactivatedcourses')

    def createCourse(self, closed):
        self.closed = closed
        self.save()
        return self

    def setInfo(self, name, description, closed, activated, startDate, endDate, color):
        self.name = name
        self.description = description
        self.closed = closed
        self.activated = activated
        self.startDate = startDate
        self.endDate = endDate
        self.confirmed = False
        self.color = color
        self.save()

    def saveCourse(self):
        self.confirmed = True
        self.save()


    # startDate e endDate sono degli oggetti di tipo datetime
    def addLesson(self, startDate, endDate, startTime, endTime, frequency, weekDayOfLesson):
        from pump_app.model_classes.LessonFactory import LessonFactory
        LessonFactory().createLesson(self, startDate, endDate, startTime, endTime, frequency, weekDayOfLesson)


    def __unicode__(self):
        return self.name + '(' + str(self.id) + ')'
