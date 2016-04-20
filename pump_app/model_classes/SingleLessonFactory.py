from django.db import models
from pump_app.model_classes.LessonFactory import LessonFactory
from pump_app.model_classes.SingleLesson import SingleLesson

"""
SingleLessonFactory Class
"""
class SingleLessonFactory(LessonFactory):

    """
    It creates a new SingleLesson instance

    date => dateTime
    startTime => dateTime
    endTime => dateTime

    :return SingleLesson()
    """
	def createLesson(self, date, startTime, endTime):
		singlelesson = SingleLesson().makeNewSingleLesson()
		singlelesson.setLessonInfo(date, startTime, endTime)
		return singlelesson

