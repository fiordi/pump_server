from pump_app.model_classes.Sale import Sale
from rest_framework import viewsets, permissions, filters, generics
from pump_app.REST_classes.SaleSerializer import SaleSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import detail_route
from rest_framework.response import Response
import datetime

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

		#ogni volta che vengono richieste informazioni su una sale, ne aggiorno il totale
		ManageSaleHandler().getTotal(sale)

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