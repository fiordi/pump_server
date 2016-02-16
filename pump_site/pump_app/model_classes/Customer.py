#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Course
import Tag
import User

class Customer(User):
	def __init__(self):
		self._enrolls = []
		# @AssociationType Course[]
		# @AssociationMultiplicity 0..*
		self._unnamed_Tag_ = []
		# @AssociationType Tag[]
		# @AssociationMultiplicity 0..*

