#!/usr/bin/python
# -*- coding: UTF-8 -*-
import UserCatalog
import CourseCatalog
import Course

class ManageCourseHandler(object):
	def makeNewCourse(self):
		pass

	def setCourseInfo(self, aName, aDescription, aStartDate, aEndDate, aTypology):
		pass

	def addLesson(self, aWeekDay, aStartTime, aEndTime, aTrainer, aFrequency):
		pass

	def saveCourse(self):
		pass

	def activateCourse(self):
		pass

	def __init__(self):
		self._unnamed_UserCatalog_ = None
		# @AssociationType UserCatalog
		self._unnamed_CourseCatalog_ = None
		# @AssociationType CourseCatalog
		self._unnamed_Course_ = None
		# @AssociationType Course

