from django.contrib.auth.models import User
from django.db import models
from course.model_classes.Course import Course
from course.model_classes.RepeatedLesson import RepeatedLesson

"""
SingleLesson Class
"""
class SingleLesson(models.Model):
    id = models.AutoField(primary_key=True)

    date = models.DateField(null=True, auto_now=False, auto_now_add=False)

    startTime = models.TimeField(null=True, auto_now=False, auto_now_add=False)

    endTime = models.TimeField(null=True, auto_now=False, auto_now_add=False)

    repeatedlesson = models.ForeignKey(RepeatedLesson, null=True, blank=True, related_name='single_lessons')

    course = models.ForeignKey(Course, null=True, blank=True, related_name='single_lessons')



    """
    It creates a new instance of SingleLesson and saves it into db

    :return SingleLesson()
    """
    def makeNewSingleLesson(self):
        self.save()
        return self



    """
    It sets the attributes of current SingleLesson instance
    """
    def setLessonInfo(self, date, startTime, endTime):
        self.date = date
        self.startTime = startTime
        self.endTime = endTime
        self.save()



    def __unicode__(self):
        return str(self.date)
