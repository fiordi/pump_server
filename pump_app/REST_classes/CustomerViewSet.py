from pump_app.model_classes.Customer import Customer
from rest_framework import viewsets, permissions, filters, generics
from pump_app.REST_classes.CustomerSerializer import CustomerSerializer

"""
CourseViewSet Class
"""
class CustomerViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer