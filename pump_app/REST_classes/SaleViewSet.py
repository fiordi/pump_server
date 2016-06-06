from django.shortcuts import get_object_or_404
from pump_app.model_classes.Sale import Sale
from pump_app.REST_classes.SaleSerializer import SaleSerializer, SaleSerializer_packets_field
from rest_framework import viewsets, permissions, filters, generics, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from collections import Counter
import datetime, json


"""
SaleViewSet Class
"""
class SaleViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

	queryset = Sale.objects.all()
	serializer_class = SaleSerializer






	"""
	It overrides the default __retrieve()__ method of REST API for customizaton (amount must be update on every reload)

	request => HttpRequest()
	pk => Integer

	:return Response()
	"""
	def retrieve(self, request, pk=None):
		from pump_app.model_classes.ManageSaleHandler import ManageSaleHandler

		queryset = Sale.objects.all()
		sale = get_object_or_404(queryset, pk=pk)

		serializer = SaleSerializer(sale)
		return Response(serializer.data)









	"""
	It overrides the default __create()__ method of REST API in order to create a new sale and put into it a timeStamp of
	starting dateTime and the User linked to the sale

	request => HttpRequest()
	pk => Integer

	:return Response()
	"""
	def create(self, request, pk=None):

		sale = Sale()

		serializer = SaleSerializer(data=request.data)

		logged_user = request.user

		if serializer.is_valid() and logged_user.is_authenticated():
			sale.dateTime = datetime.datetime.now()
			sale.user = logged_user.customer
			sale.save()

		serializer = SaleSerializer(sale)
		return Response(serializer.data)




	"""
	It creates a new route rule which checks if Sale can be completed and, if so, creates a new Subscription or updates existing

	request => HttpRequest()
	pk => Integer

	:return Response()
	"""
	@detail_route(methods=['get'], permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,))
	def confirm_sale(self, request, pk=None):
		from pump_app.model_classes.ManageSubscriptionHandler import ManageSubscriptionHandler
		from pump_app.model_classes.SubscriptionState import SubscriptionActive
		from pump_app.model_classes.SaleState import SaleCompleted, SaleState

		queryset = Sale.objects.all()
		sale = get_object_or_404(queryset, pk=pk)

		#checks (to be written)
		#...
		#...

		customer = request.user.customer

		#verifica se il cliente ha gia' una subscription oppure ne crea una nuova
		if customer.subscription:
			subscription = customer.subscription
		else:
			subscription = ManageSubscriptionHandler().makeNewSubscription()


		packets = Counter(subscription.packets.all()) + Counter(sale.packets.all())


		startdate_subscription = ManageSubscriptionHandler().evalStartDate(packets, sale.dateTime)
		enddate_subscription = ManageSubscriptionHandler().evalEndDate(packets)

		for packet in packets:
			subscription.packets.add(packet)

		subscription.startDate = startdate_subscription
		subscription.endDate = enddate_subscription
		subscription.state = SubscriptionActive.objects.all()[0]
		subscription.save()

		customer.subscription = subscription
		customer.save()

		sale.state = SaleCompleted.objects.all()[0]
		sale.save()


		serializer = SaleSerializer(sale)
		return Response(serializer.data)






	"""
	It checks if a Packet can be added to a Sale and, if so, does it

	request => HttpRequest()
	pk => Integer

	:return Response()
	"""
	@detail_route(methods=['put', 'patch'], permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,))
	def patch_packets(self, request, pk=None):
		from pump_app.model_classes.ManageSubscriptionHandler import ManageSubscriptionHandler
		from pump_app.model_classes.Packet import Packet
		from pump_app.model_classes.SaleLineItem import SaleLineItem

		queryset = Sale.objects.all()
		sale = get_object_or_404(queryset, pk=pk)

		serializer = SaleSerializer_packets_field(data=request.data)

		customer = request.user.customer

		try:
			subscription = customer.subscription
		except:
			subscription = None

		if serializer.is_valid():
			packets = request.data.get('packets')
			sale.packets.clear()
			#ogni volta che faccio un patch, cancello e rivaluto tutte le SaleLineItems
			SaleLineItem.objects.filter(sale=sale).delete()
			for packet_pk, quantity in packets.iteritems():
				if subscription and ManageSubscriptionHandler().checkPacketInSubscription(subscription, packet_pk):
					pass
				else:
					packet = Packet.objects.get(pk=packet_pk)
					salelineitem = SaleLineItem(sale=sale, packet=packet, quantity=quantity)
					salelineitem.save()
					sale.save()

			sale.save()

		serializer = SaleSerializer(sale)
		return Response(serializer.data)