from django.contrib.auth.models import User
from django.db import models
from pump_app.model_classes.Course import Course

"""
RepeatedLesson Class
"""
class RepeatedLesson(models.Model):
    id = models.AutoField(primary_key=True)

    weekDay = models.IntegerField(null=True)

    startDate = models.DateField(null=True, auto_now=False, auto_now_add=False)

    endDate = models.DateField(null=True, auto_now=False, auto_now_add=False)

    startTime = models.TimeField(null=True, auto_now=False, auto_now_add=False)

    endTime = models.TimeField(null=True, auto_now=False, auto_now_add=False)

    course = models.ForeignKey(Course, null=True, blank=True, related_name='RepeatedLessons')

    """
    It creates a new instance of RepeatedLesson and save it into db

    :return RepeatedLesson()
    """
    def makeNewRepeatedLesson(self):
        self.save()
        return self

    """
    It sets the attributes of current RepeatedLesson instance
    """
    def setLessonInfo(self, weekDay, startDate, endDate, startTime, endTime):
        self.weekDay = weekDay
        self.startDate = startDate
        self.endDate = endDate
        self.startTime = startTime
        self.endTime = endTime
        self.save()

    def __unicode__(self):
        return str(self.startDate) + " " +  str(self.endDate) + "(" + str(self.pk) + ")"
