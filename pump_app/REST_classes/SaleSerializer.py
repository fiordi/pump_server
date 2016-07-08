from pump_app.model_classes.Sale import Sale
from rest_framework import serializers

"""
SaleSerializer Class
"""
class SaleSerializer(serializers.ModelSerializer):
	applied_strategies = serializers.DictField(child=serializers.CharField(), read_only=True)

	class Meta:
		model = Sale
		fields = ('id', 'dateTime', 'amount_prediscount', 'amount', 'applied_strategies', 'packets', 'user')
		read_only_fields = ('dateTime', 'amount_prediscount', 'amount', 'applied_strategies', 'packets', 'user')




"""
SaleSerializer_packets_field Class
"""
class SaleSerializer_packets_field(serializers.ModelSerializer):

	class Meta:
		model = Sale
		fields = ('packets',)