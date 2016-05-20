import django_filters
from pump_app.model_classes.Packet import Packet
from rest_framework import viewsets, permissions, filters, generics
from pump_app.REST_classes.PacketSerializer import PacketSerializer

"""
PacketViewSet Class
"""
class PacketViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

	queryset = Packet.objects.all()
	serializer_class = PacketSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('id', 'name', 'courses', 'state')
