from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, filters, generics
from rest_framework.decorators import list_route
from rest_framework.response import Response
from customer.model_classes.Customer import Customer
from customer.REST_classes.CustomerSerializer import CustomerSerializer

"""
CourseViewSet Class
"""
class CustomerViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer





	"""
	It returns the serialization of logged costumer

	request => HttpRequest()

	:return Response()
	"""
	@list_route(methods=['get'], permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,))
	def logged_customer(self, request):
		try:
			user = request.user
			customer = user.customer
		except:
			user = None

		if user and user.is_authenticated():
			serializer = CustomerSerializer(customer)
			return Response(serializer.data)
		else:
			return Response({'detail': 'Not found.'})