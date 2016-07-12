from pump_app.model_classes.CourseCatalog import CourseCatalog
from rest_framework import viewsets
from pump_app.REST_classes.CourseCatalogSerializer import CourseCatalogSerializer

"""
CourseCatalogViewSet Class
"""
class CourseCatalogViewSet(viewsets.ModelViewSet):
	queryset = CourseCatalog.objects.all()

	serializer_class = CourseCatalogSerializer


