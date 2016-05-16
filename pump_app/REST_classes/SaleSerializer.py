from pump_app.model_classes.Sale import Sale
from rest_framework import serializers

"""
SaleSerializer Class
"""
class SaleSerializer(serializers.ModelSerializer):

	class Meta:
		model = Sale
		fields = ('id', 'dateTime', 'amount', 'packets')

	"""
	It overrides the default __update()__ method of REST API in order to allow writing of state field (GenericForeignKey!)

	instance => Sale()
	validated_data => Unknown

	:return Sale()
	"""
	def update(self, instance, validated_data):
		from pump_app.model_classes.SalePricingStrategyFactory import SalePricingStrategyFactory

		instance.dateTime = validated_data.get('dateTime', instance.dateTime)
		instance.packets = validated_data.get('packets', instance.packets)

		packets = instance.packets.all()

		#ogni volta che arrivano i pacchetti vengono aggiornati, ricalcolo il totale PreDiscount
		prediscount_amount = 0
		for packet in packets:
			prediscount_amount = prediscount_amount + packet.price

		instance.amount_prediscount = prediscount_amount
		instance.amount = instance.amount_prediscount

		#dopo aver aggiornato il timeStamp e i pacchetti, devo adottare la strategia di sconto
		PricingStrategies = SalePricingStrategyFactory().getAllPricingStrategy()
		from pump_app.model_classes.SalePricingStrategy import MorePacketsStrategy
		for PricingStrategy in PricingStrategies:
			amount = PricingStrategy.getAmount(instance)
			instance.amount = amount

		instance.save()
		course_request = self.context['request'].data
		return instance