#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Trainer
import Course

class Lesson(object):
	def setLessonInfo(self, aDay, aWeekDay, aStartTime, aEndTime, aRepeated):
		pass

	def __init__(self):
		self.___id = None
		"""@AttributeType string"""
		self.___startTime = None
		"""@AttributeType time"""
		self.___endTime = None
		"""@AttributeType time"""
		self.___weekDay = None
		"""@AttributeType day"""
		self.___repeated = None
		"""@AttributeType boolean"""
		self.___date = None
		"""@AttributeType date"""
		self._lessonTrainer = None
		# @AssociationType Trainer
		# @AssociationMultiplicity 1
		self._unnamed_Course_ = None
		# @AssociationType Course
		# @AssociationMultiplicity 1

