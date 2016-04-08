from django.db import models
from pump_app.model_classes.LessonFactory import LessonFactory
from pump_app.model_classes.RepeatedLesson import RepeatedLesson

class RepeatedLessonFactory(LessonFactory):

	def createLesson(self):
		repeatedlesson = RepeatedLesson().makeNewRepeatedLesson()
		return repeatedlesson

