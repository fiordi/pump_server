from pump_app.model_classes.Sale import Sale
from rest_framework import viewsets, permissions, filters, generics
from pump_app.REST_classes.SaleSerializer import SaleSerializer

"""
SaleViewSet Class
"""
class SaleViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

	queryset = Sale.objects.all()
	serializer_class = SaleSerializer