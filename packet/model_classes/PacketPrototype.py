from django.db import models

"""
PacketPrototype Class (Interface)
"""
class PacketPrototype(models.Model):

    def clone(self):
        pass

    class Meta:
		abstract = True
