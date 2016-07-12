from django.contrib.auth.models import User
from django.db import models
from solo.models import SingletonModel


"""
PacketCatalog class (Singleton)
"""
class PacketCatalog(SingletonModel):
	id = models.AutoField(primary_key=True)

	name = models.TextField(null=True, blank=False, default="Packet Catalog")

	"""
	It adds a Packet to PacketCatalog

	Packet => Packet()
	"""
	def addCourse(self, Packet):
		Packet.packetcatalog = self
		Packet.save()

	def __unicode__(self):
		return self.name
