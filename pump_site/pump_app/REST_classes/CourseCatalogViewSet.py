from pump_app.model_classes.CourseCatalog import CourseCatalog
from pump_app.model_classes.utility.Singleton import SingletonModel
from rest_framework import viewsets
from pump_app.REST_classes.CourseCatalogModelSerializer import CourseCatalogModelSerializer

class CourseCatalogViewSet(viewsets.ModelViewSet):
	queryset = CourseCatalog.objects.all()

	serializer_class = CourseCatalogModelSerializer


