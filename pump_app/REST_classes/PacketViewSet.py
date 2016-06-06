from pump_app.model_classes.Packet import Packet, StandardPacket, CustomPacket
import django_filters
from rest_framework import viewsets, permissions, filters, generics
from pump_app.REST_classes.PacketSerializer import PacketSerializer, PacketSerializer_imageToText, CustomPacketSerializer, StandardPacketSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
import os, json

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
	It overrides the default __list()__ method of REST API for customizaton (print only relative path of images)

	request => HttpRequest()

	:return Response()
	"""
	def list(self, request):
		queryset = Packet.objects.all()

		for packet in queryset:
			if packet.image:
				packet.image = system_settings.relative_path_image_packet + os.path.basename(packet.image.name)

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

		if packet.image:
			packet.image = system_settings.relative_path_image_packet + os.path.basename(packet.image.name)

		serializer = PacketSerializer(packet)
		return Response(serializer.data)





	"""
	It overrides __create__ of REST API in order to create a Standard Packet or Customer Packet based on user request

	request => HttpRequest()

	:return Response()
	"""
	def create(self, request):
		if request.data.get('type') == CustomPacket().__class__.__name__:
			serializer = CustomPacketSerializer(data=request.data)
		elif request.data.get('type') == StandardPacket().__class__.__name__:
			serializer = StandardPacketSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()

		return Response(serializer.data)




	"""
	It creates a new router rule which is used to upload images of packet

	request => HttpRequest()
	pk => Integer

	:return Response()
	"""
	@detail_route(methods=['put', 'patch'], permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,))
	def update_img(self, request, pk=None):

		queryset = Packet.objects.all()
		packet = get_object_or_404(queryset, pk=pk)

		serializer = PacketSerializer(data=request.data)

		if serializer.is_valid():
			packet.image = request.data.get('image')
			image_path = system_settings.relative_path_image_packet + os.path.basename(packet.image.name)
		else:
			if not request.data.get('image'):
				packet.image = 'no_image.png'
				image_path = system_settings.relative_path_image_packet + os.path.basename(packet.image.name)

		packet.save()

		return Response({'image': image_path})





	"""
	It creates a new route rule which returns only not subscribed packets

	request => HttpRequest()

	:return Response()
	"""
	@list_route(methods=['get'], permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,))
	def not_subscr_packets(self, request):
		from pump_app.model_classes.ManageSubscriptionHandler import ManageSubscriptionHandler

		packets = Packet.objects.all()

		packets_not_subscribed =[]

		try:
			subscription = request.user.customer.subscription
		except:
			subscription = None

		if subscription:
			for packet in packets:
				packet_pk = packet.id
				if ManageSubscriptionHandler().checkPacketInSubscription(subscription, packet_pk):
					pass
				else:
					packets_not_subscribed.append(packet)
					packet.image = system_settings.relative_path_image_packet + os.path.basename(packet.image.name)
			serializer = PacketSerializer_imageToText(packets_not_subscribed, many=True)
		else:
			serializer = PacketSerializer_imageToText(packets, many=True)

		return Response(serializer.data)

