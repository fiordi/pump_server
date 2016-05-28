from pump_app.model_classes.Packet import Packet
from rest_framework import serializers


"""
PacketSerializer Class
"""
class PacketSerializer(serializers.ModelSerializer):

	class Meta:
		model = Packet


		fields = ('id', 'name', 'description', 'price', 'startDate', 'endDate','state', 'courses', 'image')




"""
PacketSerializer_imageToText Class
"""
class PacketSerializer_imageToText(serializers.ModelSerializer):
	image = serializers.CharField()

	class Meta:
		model = Packet

		fields = ('id', 'name', 'description', 'price', 'startDate', 'endDate','state', 'courses', 'image')