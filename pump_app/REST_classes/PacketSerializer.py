from pump_app.model_classes.Packet import Packet
from rest_framework import serializers
from django.contrib.auth.models import User

"""
PacketSerializer Class
"""
class PacketSerializer(serializers.ModelSerializer):

	class Meta:
		model = Packet


		fields = ('id', 'name', 'description', 'price', 'startDate', 'endDate', 'courses')

