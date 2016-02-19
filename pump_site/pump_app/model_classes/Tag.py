#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Course
import Customer

class Tag(object):
	def __init__(self):
		self.___name = None
		"""@AttributeType String"""
		self._defines = []
		# @AssociationType Course[]
		# @AssociationMultiplicity 0..*
		self._choose = []
		# @AssociationType Customer[]
		# @AssociationMultiplicity 0..*

