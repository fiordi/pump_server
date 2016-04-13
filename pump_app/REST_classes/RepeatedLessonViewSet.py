import django_filters
from pump_app.model_classes.RepeatedLesson import RepeatedLesson
from rest_framework import viewsets, permissions, filters
from pump_app.REST_classes.RepeatedLessonSerializer import RepeatedLessonSerializer


class RepeatedLessonViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

	queryset = RepeatedLesson.objects.all()
	serializer_class = RepeatedLessonSerializer