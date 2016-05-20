from pump_app.model_classes.Course import Course
from rest_framework import serializers
from django.contrib.auth.models import User
from pump_app.model_classes.utility.Utility import Utility
from pump_app.libraries.generic_relations.relations import GenericRelatedField
import json

"""
CourseSerializer Class
"""
class CourseSerializer(serializers.ModelSerializer):

    class Meta:
		model = Course

		fields = ('id', 'name', 'description', 'closed', 'subscrNumber', 'startDate', 'endDate', 'coursecatalog', 'state')
