#!/usr/bin/python
# -*- coding: UTF-8 -*-
import ManageCourseHandler
import Lesson
import Tag
import CourseCatalog
import Administrator
import Customer

class Course(object):
	def addLesson(self, aWeekDay, aStarTime, aEndTime, aTrainer, aFrequency):
		pass

	def setInfo(self, aName, aDescription, aOpen, aStartDate, aEndDate):
		pass

	def __init__(self):
		self.___id = None
		"""@AttributeType string"""
		self.___name = None
		"""@AttributeType String"""
		self.___description = None
		"""@AttributeType string"""
		self.___open = None
		"""@AttributeType boolean"""
		self.___startDate = None
		"""@AttributeType time"""
		self.___endDate = None
		"""@AttributeType time"""
		self._unnamed_ManageCourseHandler_ = None
		# @AssociationType ManageCourseHandler
		self._unnamed_Lesson_ = []
		# @AssociationType Lesson[]
		# @AssociationMultiplicity 0..*
		# @AssociationKind Composition
		self._defines = []
		# @AssociationType Tag[]
		# @AssociationMultiplicity 0..*
		self._unnamed_CourseCatalog_ = None
		# @AssociationType CourseCatalog
		self._creates = None
		# @AssociationType Administrator
		# @AssociationMultiplicity 1
		self._enrolls = []
		# @AssociationType Customer[]
		# @AssociationMultiplicity 0..*

