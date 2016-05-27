from pump_app.model_classes.Sale import Sale
from rest_framework import serializers

"""
SaleSerializer Class
"""
class SaleSerializer(serializers.ModelSerializer):
	applied_strategies = serializers.DictField(child=serializers.CharField())

	class Meta:
		model = Sale
		fields = ('id', 'dateTime', 'amount', 'applied_strategies', 'packets', 'user')
		read_only_fields = ('dateTime', 'amount', 'applied_strategies', 'user')