from pump_app.model_classes.Sale import Sale
from rest_framework import serializers

"""
SaleSerializer Class
"""
class SaleSerializer(serializers.ModelSerializer):

	class Meta:
		model = Sale
		fields = ('id', 'dateTime', 'amount', 'packets', 'user')
		read_only_fields = ('dateTime', 'amount', 'user')



	"""
	It overrides the default __update()__ method of REST API in order to allow writing of state field (GenericForeignKey!)

	instance => Sale()
	validated_data => Unknown

	:return Sale()
	"""
	def update(self, instance, validated_data):
		from pump_app.model_classes.ManageSaleHandler import ManageSaleHandler

		instance.dateTime = validated_data.get('dateTime', instance.dateTime)
		instance.packets = validated_data.get('packets', instance.packets)

		#ogni volta che arrivano i pacchetti vengono aggiornati, ricalcolo il totale PreDiscount
		ManageSaleHandler().getTotal(instance)

		instance.save()
		course_request = self.context['request'].data
		return instance