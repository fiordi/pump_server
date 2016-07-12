from rest_framework import viewsets, permissions, filters, generics
from course.model_classes.Course import Course
from course.REST_classes.CourseSerializer import CourseSerializer

"""
CourseViewSet Class
"""
class CourseViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

	queryset = Course.objects.all()
	serializer_class = CourseSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('id', 'name', 'startDate', 'endDate', 'state')