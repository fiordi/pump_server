from pump_app.model_classes.Customer import Customer
from rest_framework import serializers

"""
CustomerSerializer Class
"""
class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
		model = Customer
		fields = ('id', 'user', 'type')

