from django.db import models
from pump_app.model_classes.LessonFactory import LessonFactory
from pump_app.model_classes.SingleLesson import SingleLesson

class SingleLessonFactory(LessonFactory):

	def createLesson(self, date, startTime, endTime):
		singlelesson = SingleLesson().makeNewSingleLesson()
		singlelesson.setLessonInfo(date, startTime, endTime)
		return singlelesson

