from pump_app.model_classes.SingleLesson import SingleLesson
from rest_framework import viewsets, permissions
from pump_app.REST_classes.SingleLessonSerializer import SingleLessonSerializer


class LessonViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

	queryset = SingleLesson.objects.all()
	serializer_class = SingleLessonSerializer
