from pump_app.model_classes.Course import Course
from rest_framework import serializers
from django.contrib.auth.models import User


class CourseSerializer(serializers.ModelSerializer):

	class Meta:
		model = Course

		#user = User.objects.get(username='federico')
		#if user.has_perm('pump_app.change_course'):
		fields = ('id', 'name', 'description', 'closed', 'subscrNumber', 'startDate', 'endDate', 'coursecatalog', 'state')
		#else:
			#fields = ('id', 'name', 'description', 'open', 'startDate', 'endDate')
