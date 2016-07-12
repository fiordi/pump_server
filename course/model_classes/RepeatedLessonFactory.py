from django.db import models
from course.model_classes.LessonFactory import LessonFactory
from course.model_classes.RepeatedLesson import RepeatedLesson

"""
RepeatedLessonFactory
"""
class RepeatedLessonFactory(LessonFactory):

	"""
    It creates a new RepeatedLesson instance

    :return RepeatedLesson()
    """
	def createLesson(self):
		repeatedlesson = RepeatedLesson().makeNewRepeatedLesson()
		return repeatedlesson

