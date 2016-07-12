from rest_framework import serializers
from django.contrib.auth.models import User
from course.model_classes.SingleLesson import SingleLesson

"""
SingleLessonSerializer Class
"""
class SingleLessonSerializer(serializers.ModelSerializer):

	class Meta:
		model = SingleLesson


		fields = ('id', 'date', 'startTime', 'endTime', 'course', 'repeatedlesson')

