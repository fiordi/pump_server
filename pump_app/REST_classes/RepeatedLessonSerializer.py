from pump_app.model_classes.RepeatedLesson import RepeatedLesson
from rest_framework import serializers


"""
RepeatedLessonSerializer Class
"""
class RepeatedLessonSerializer(serializers.ModelSerializer):

	class Meta:
		model = RepeatedLesson


		fields = ('id', 'weekDay', 'startDate', 'endDate', 'startTime', 'endTime', 'course')

