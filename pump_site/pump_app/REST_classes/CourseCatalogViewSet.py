from pump_app.model_classes.CourseCatalog import CourseCatalog
from pump_app.model_classes.utility.Singleton import SingletonModel
from rest_framework import viewsets
from pump_app.REST_classes.CourseCatalogSerializer import CourseCatalogSerializer

class CourseCatalogViewSet(viewsets.ModelViewSet):
	queryset = CourseCatalog.objects.all()

	serializer_class = CourseCatalogSerializer


