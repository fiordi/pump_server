from django.db import models

"""
PacketState Class (Interface)
"""
class PacketState(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.TextField(null=True, blank=False, unique=True, default='Undefined')

    def __unicode__(self):
        return self.name + '(' + str(self.id) + ')'

"""
ActivatedPacket Class (Singleton)
"""
class ActivatedPacket(PacketState):

    def setName(self):
        self.name = "Activated"
        self.save()

    def setState(self, Packet):
        Packet.state = self

"""
PacketDeativated Class (Singleton)
"""
class DeactivatedPacket(PacketState):

    def setName(self):
        self.name = "Deactivated"
        self.save()

    def setState(self, Packet):
        Packet.state = self

"""
IncompletePacket Class (Singleton)
"""
class IncompletePacket(PacketState):

    def setName(self):
        self.name = "Incomplete"
        self.save()

    def setState(self, Packet):
        Packet.state = self