from django.db import models
from solo.models import SingletonModel

"""
PacketState Class (Interface)
"""
class PacketState(models.Model):

    def setPacketState(self, Course):
        pass

    class Meta:
		abstract = True
