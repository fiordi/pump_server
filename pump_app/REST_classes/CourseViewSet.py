from pump_app.model_classes.Course import Course
from rest_framework import viewsets, permissions
from pump_app.REST_classes.CourseSerializer import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

	queryset = Course.objects.all()
	serializer_class = CourseSerializer
