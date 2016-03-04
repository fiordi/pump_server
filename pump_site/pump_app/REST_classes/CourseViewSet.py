from pump_app.model_classes.Course import Course
from rest_framework import viewsets
from pump_app.REST_classes.CourseSerializer import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):

	queryset = Course.objects.all()
	serializer_class = CourseSerializer
