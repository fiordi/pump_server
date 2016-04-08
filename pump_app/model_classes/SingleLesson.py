from django.contrib.auth.models import User
from django.db import models
from pump_app.model_classes.Course import Course
from pump_app.model_classes.RepeatedLesson import RepeatedLesson

class SingleLesson(models.Model):
    id = models.AutoField(primary_key=True)

    date = models.DateField(null=True, auto_now=False, auto_now_add=False)

    startTime = models.TimeField(null=True, auto_now=False, auto_now_add=False)

    endTime = models.TimeField(null=True, auto_now=False, auto_now_add=False)

    repeatedlesson = models.ForeignKey(RepeatedLesson, null=True, blank=True, related_name='single_lessons')

    course = models.ForeignKey(Course, null=True, blank=True, related_name='single_lessons')

    def makeNewSingleLesson(self):
        self.save()
        return self

    def setLessonInfo(self, date, startTime, endTime):
        self.date = date
        self.startTime = startTime
        self.endTime = endTime
        #self.Trainer = Trainer
        self.save()

    def __unicode__(self):
        return str(self.date)
