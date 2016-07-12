from rest_framework import serializers
from customer.model_classes.Customer import Customer

"""
CustomerSerializer Class
"""
class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
		model = Customer
		fields = ('id', 'user', 'name', 'surname', 'email', 'phone', 'subscription', 'type')

