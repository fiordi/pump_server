from django.contrib.auth.models import User
from django.db import models
from pump_app.model_classes.CourseCatalog import CourseCatalog
import datetime


class Course(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.TextField(null=True, blank=False, default='Undefined')

    description = models.TextField(null=True, blank=False)

    open = models.BooleanField(null=False, default=False)

    activated = models.BooleanField(null=False, default=False)

    startDate = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)

    endDate = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)

    confirmed = models.BooleanField(null=False, default=False)

    if activated:
        coursecatalog = models.ForeignKey(CourseCatalog, null=True, blank=False, on_delete=models.CASCADE, related_name='activatedcourses')
    else:
        coursecatalog = models.ForeignKey(CourseCatalog, null=True, blank=False, on_delete=models.CASCADE, related_name='deactivatedcourses')

    def createCourse(self, open):
        self.open = open
        self.save()
        return self

    def setInfo(self, name, description, open, startDate, endDate):
        self.name = name
        self.description = description
        self.open = open
        self.startDate = startDate
        self.endDate = endDate
        self.save()


    # startDate e endDate sono degli oggetti di tipo datetime
    def addLesson(self, startDate, endDate, startTime, endTime, frequency):
        from pump_app.model_classes.Lesson import Lesson

        while startDate <= endDate:
            lesson = Lesson().makeNewLesson()

            lesson.setLessonInfo(startDate, startTime, endTime)
            startDate = startDate + datetime.timedelta(days=frequency)


    def setInfo(self, aName, aDescription, aOpen, aStartDate, aEndDate):
        pass

    def __unicode__(self):
        return self.name + '(' + str(self.id) + ')'
