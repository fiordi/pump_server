#!/usr/bin/python
# -*- coding: UTF-8 -*-
import CourseCatalog

class Gym(object):
	def __init__(self):
		self.___name = None
		"""@AttributeType String"""
		self.___address = None
		"""@AttributeType address"""
		self._belongs_to = []
		# @AssociationType CourseCatalog[]
		# @AssociationMultiplicity 0..*

