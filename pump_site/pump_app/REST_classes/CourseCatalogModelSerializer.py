from pump_app.model_classes import CourseCatalog
from rest_framework import serializers


class CourseCatalogModelSerializer(serializers.ModelSerializer):

	class Meta:
		model = CourseCatalog
		fields = ('id', 'name')