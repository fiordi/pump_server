from django.contrib.auth.models import User
from django.db import models

"""
Lesson Class (Interface)
"""
class Lesson(models.Model):

    def addLesson(self):
        pass

    def removeLesson(self):
        pass

    def setLessonInfo(self):
        pass

    class Meta:
		abstract = True

