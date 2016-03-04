from pump_app.model_classes.Course import Course
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):

	class Meta:
		model = Course
		fields = ('id', 'name', 'description', 'open', 'startDate', 'endDate', 'coursecatalog')
