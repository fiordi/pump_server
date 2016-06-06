from pump_app.model_classes.Packet import Packet, StandardPacket, CustomPacket
from rest_framework import serializers


"""
PacketSerializer Class
"""
class PacketSerializer(serializers.ModelSerializer):

	class Meta:
		model = Packet


		fields = ('id', 'name', 'description', 'price', 'state', 'courses', 'image')




"""
PacketSerializer_imageToText Class
"""
class PacketSerializer_imageToText(serializers.ModelSerializer):
	image = serializers.CharField()

	class Meta:
		model = Packet

		fields = ('id', 'name', 'description', 'price', 'state', 'courses', 'image')






"""
StandardPacketSerializer Class
"""
class StandardPacketSerializer(serializers.ModelSerializer):

	class Meta:
		model = StandardPacket


		fields = ('id', 'name', 'description', 'price', 'durate', 'upperBoundary', 'state', 'courses', 'image')






"""
CustomPacketSerializer Class
"""
class CustomPacketSerializer(serializers.ModelSerializer):

	class Meta:
		model = CustomPacket


		fields = ('id', 'name', 'description', 'price', 'startDate', 'endDate','state', 'courses', 'image')