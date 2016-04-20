from pump_app.model_classes.CourseCatalog import CourseCatalog
from rest_framework import serializers

"""
CourseCatalogSerializer Class
"""
class CourseCatalogSerializer(serializers.ModelSerializer):

	class Meta:
		model = CourseCatalog
		fields = ('id', 'name')