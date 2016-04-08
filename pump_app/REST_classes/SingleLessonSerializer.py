from pump_app.model_classes.SingleLesson import SingleLesson
from rest_framework import serializers
from django.contrib.auth.models import User


class SingleLessonSerializer(serializers.ModelSerializer):

	class Meta:
		model = SingleLesson


		fields = ('id', 'date', 'startTime', 'endTime', 'course', 'repeatedlesson')

