from pump_app.model_classes.Sale import Sale
from rest_framework import viewsets, permissions, filters, generics
from pump_app.REST_classes.SaleSerializer import SaleSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

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