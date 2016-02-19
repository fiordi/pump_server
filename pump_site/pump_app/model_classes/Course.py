from django.contrib.auth.models import User
from django.db import models
from pump_app.model_classes.CourseCatalog import CourseCatalog

class Course(models.Model):
	id = models.AutoField(primary_key=True)

	name = models.TextField(null=False, blank=False)

	description = models.TextField(null=False, blank=False)

	open = models.BooleanField()

	startDate = models.DateTimeField(auto_now=False, auto_now_add=False)

	endTime = models.DateTimeField(auto_now=False, auto_now_add=False)

	if True:
    		CourseCatalog = models.ForeignKey(CourseCatalog, null=False, blank=False, related_name='Activatedcourse')
	else:
			CourseCatalog = models.ForeignKey(CourseCatalog, null=False, blank=False, related_name='Dectivatedcourse')

	def addLesson(self, aWeekDay, aStarTime, aEndTime, aTrainer, aFrequency):
		pass

	def setInfo(self, aName, aDescription, aOpen, aStartDate, aEndDate):
		pass
