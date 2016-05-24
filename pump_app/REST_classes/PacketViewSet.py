import django_filters
from pump_app.model_classes.Packet import Packet
from rest_framework import viewsets, permissions, filters, generics
from pump_app.REST_classes.PacketSerializer import PacketSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

#recupero le proprieta' di sistema
import pump_site.system_settings
system_settings = pump_site.system_settings

"""
PacketViewSet Class
"""
class PacketViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

	queryset = Packet.objects.all()
	serializer_class = PacketSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('id', 'name', 'courses', 'state')


	"""
	It overrides the default __list()__ method of REST API for customizaton (print only relative path of image)

	request => HttpRequest()

	:return Response()
	"""
	def list(self, request):
		queryset = Packet.objects.all()

		for packet in queryset:
			packet.image = system_settings.relative_path_image_packet + str(packet.image.name)

		serializer = PacketSerializer(queryset, many=True)
		return Response(serializer.data)

	"""
	It overrides the default __retrieve()__ method of REST API for customizaton (print only relative path of image)

	request => HttpRequest()
	pk => Integer

	:return Response()
	"""
	def retrieve(self, request, pk=None):

		queryset = Packet.objects.all()
		packet = get_object_or_404(queryset, pk=pk)


		packet.image = system_settings.relative_path_image_packet + str(packet.image.name)

		serializer = PacketSerializer(packet)
		return Response(serializer.data)



	"""
	It overrides the default __update()__ method of REST API for customizaton (print only relative path of image)

	request => HttpRequest()
	pk => Integer

	:return Response()
	"""
	def update(self, request, pk=None):

		queryset = Packet.objects.all()
		packet = get_object_or_404(queryset, pk=pk)


		packet.image = system_settings.relative_path_image_packet + str(packet.image.name)

		serializer = PacketSerializer(packet)
		return Response(serializer.data)