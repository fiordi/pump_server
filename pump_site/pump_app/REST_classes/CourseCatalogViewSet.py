from pump_app.model_classes import CourseCatalog
from rest_framework import viewsets
from CourseCatalogModelSerializer import CourseCatalogModelSerializer

class CourseCatalogViewSet(viewsets.ModelViewSet):
	queryset = CourseCatalog.objects.all()
	serializer_class = CourseCatalogModelSerializer


