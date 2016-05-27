from pump_app.model_classes.Course import Course
from rest_framework import serializers
from django.contrib.auth.models import User

"""
CourseSerializer Class
"""
class CourseSerializer(serializers.ModelSerializer):

    class Meta:
		model = Course

		fields = ('id', 'name', 'description', 'closed', 'subscrNumber', 'startDate', 'endDate', 'coursecatalog', 'state')
