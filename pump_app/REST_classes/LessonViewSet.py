from pump_app.model_classes.Lesson import Lesson
from rest_framework import viewsets, permissions
from pump_app.REST_classes.LessonSerializer import LessonSerializer


class LessonViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

	queryset = Lesson.objects.all()
	serializer_class = LessonSerializer
