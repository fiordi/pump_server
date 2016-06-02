from pump_app.model_classes.Course import Course
from rest_framework import viewsets, permissions, filters, generics
from pump_app.REST_classes.CourseSerializer import CourseSerializer

"""
CourseViewSet Class
"""
class CourseViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

	queryset = Course.objects.all()
	serializer_class = CourseSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('id', 'name', 'startDate', 'endDate', 'state')