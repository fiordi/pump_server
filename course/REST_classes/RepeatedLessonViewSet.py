import django_filters
from rest_framework import viewsets, permissions, filters, generics
from course.model_classes.RepeatedLesson import RepeatedLesson
from course.REST_classes.RepeatedLessonSerializer import RepeatedLessonSerializer

"""
RepeatedLessonViewSet Class
"""
class RepeatedLessonViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

	queryset = RepeatedLesson.objects.all()
	serializer_class = RepeatedLessonSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('id', 'weekDay', 'startDate', 'endDate', 'course')