#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Course
import ManageCourseHandler
import Gym

class CourseCatalog(object):
	def addCourse(self):
		pass

	def activateCourse(self):
		pass

	def __init__(self):
		self.___activatedCourses = None
		"""@AttributeType Course"""
		self.___deactivatedCourses = None
		"""@AttributeType Course"""
		self._unnamed_Course_ = None
		# @AssociationType Course
		self._unnamed_ManageCourseHandler_ = None
		# @AssociationType ManageCourseHandler
		self._belongs_to = None
		# @AssociationType Gym
		# @AssociationMultiplicity 1

