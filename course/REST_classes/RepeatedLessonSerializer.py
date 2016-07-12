from rest_framework import serializers
from course.model_classes.RepeatedLesson import RepeatedLesson

"""
RepeatedLessonSerializer Class
"""
class RepeatedLessonSerializer(serializers.ModelSerializer):

	class Meta:
		model = RepeatedLesson


		fields = ('id', 'weekDay', 'startDate', 'endDate', 'startTime', 'endTime', 'course')

