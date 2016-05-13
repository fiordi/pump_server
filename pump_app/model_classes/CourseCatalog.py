from django.contrib.auth.models import User
from django.db import models
from solo.models import SingletonModel


"""
CourseCatalog class (Singleton)
"""
class CourseCatalog(SingletonModel):
	id = models.AutoField(primary_key=True)

	name = models.TextField(null=True, blank=False, default="Course Catalog")

	"""
	It adds a Course to CourseCatalog

	Course => Course()
	"""
	def addCourse(self, Course):
		Course.coursecatalog = self
		Course.save()

	def __unicode__(self):
		return self.name
