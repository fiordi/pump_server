from django.contrib.auth.models import User
from rest_framework import serializers
from course.model_classes.Course import Course


"""
CourseSerializer Class
"""
class CourseSerializer(serializers.ModelSerializer):

    class Meta:
		model = Course

		fields = ('id', 'name', 'description', 'closed', 'subscrNumber', 'startDate', 'endDate', 'coursecatalog', 'state')
