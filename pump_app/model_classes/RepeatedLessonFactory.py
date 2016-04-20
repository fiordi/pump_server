from django.db import models
from pump_app.model_classes.LessonFactory import LessonFactory
from pump_app.model_classes.RepeatedLesson import RepeatedLesson

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

