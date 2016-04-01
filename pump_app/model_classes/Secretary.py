#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Course
import User

class Secretary(User):
	def __init__(self):
		self._creates = []
		# @AssociationType Course[]
		# @AssociationMultiplicity 0..*

