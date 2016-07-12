from django.db import models
from course.model_classes.LessonFactory import LessonFactory
from course.model_classes.SingleLesson import SingleLesson

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

