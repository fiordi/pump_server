import django_filters
from pump_app.model_classes.SingleLesson import SingleLesson
from rest_framework import viewsets, permissions, filters, generics
from pump_app.REST_classes.SingleLessonSerializer import SingleLessonSerializer


class SingleLessonViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

	queryset = SingleLesson.objects.all()
	serializer_class = SingleLessonSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	# filter_fields = ('repeatedlesson')
