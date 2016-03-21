from pump_app.model_classes.Lesson import Lesson
from rest_framework import serializers
from django.contrib.auth.models import User


class LessonSerializer(serializers.ModelSerializer):

	class Meta:
		model = Lesson


		fields = ('id', 'name', 'date', 'startTime', 'endTime')

