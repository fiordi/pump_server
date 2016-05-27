from pump_app.model_classes.Packet import Packet
from rest_framework import serializers


"""
PacketSerializer Class
"""
class PacketSerializer(serializers.ModelSerializer):

	class Meta:
		model = Packet


		fields = ('id', 'name', 'description', 'price', 'startDate', 'endDate','state', 'courses', 'image')