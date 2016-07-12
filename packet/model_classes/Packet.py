from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from packet.model_classes.PacketCatalog import PacketCatalog
from packet.model_classes.PacketPrototype import PacketPrototype
from packet.model_classes.PacketState import PacketState
from course.model_classes.Course import Course

import datetime
from decimal import *

# recupero le proprieta' di sistema
import pump_site.system_settings

system_settings = pump_site.system_settings

"""
Packet Class
"""


class Packet(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.TextField(null=True, blank=False, default='Undefined')

    description = models.TextField(null=True, blank=False)

    price = models.DecimalField(null=True, default=Decimal('0'), decimal_places=2, max_digits=12,
                                validators=[MinValueValidator(Decimal('0'))])

    state = models.ForeignKey(PacketState, to_field='name', null=True, blank=False, related_name='packets')

    packetcatalog = models.ForeignKey(PacketCatalog, null=True, blank=False, on_delete=models.CASCADE,
                                      related_name='packets')

    courses = models.ManyToManyField(Course, blank=True, related_name='courses')

    image = models.ImageField(upload_to=system_settings.relative_path_image_packet, null=True, blank=True,
                              default='static/packet_images/no_image.png')

    type = models.TextField(null=True, blank=False, default='Type of packet')

    """
    It creates a new instance of Packet and saves it into db
    """

    def makeNewPacket(self):
        self.save()
        return self

    """
    It sets the arguments of the current Packet instance
    """

    def setInfo(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
        self.save()

    """
    It sets the state of the current Packet instance to Activated

    """
    def setActivedState(self):
        from packet.model_classes.PacketState import ActivatedPacket

        ActivatedPacket.objects.all()[0].setState(self)
        self.save()

    """
    It sets the state of the current Packet instance to Dectivated

    """
    def setDeactivedState(self):
        from packet.model_classes.PacketState import DeactivatedPacket

        DeactivatedPacket.objects.all()[0].setState(self)
        self.save()


    """
    It sets the state of the current Packet instance to Incomplete

    """
    def setIncompleteState(self):
        from packet.model_classes.PacketState import IncompletePacket

        IncompletePacket.objects.all()[0].setState(self)
        self.save()



    def __unicode__(self):
        return self.name + '(' + str(self.id) + ')'


"""
StandardPacket Class
"""


class StandardPacket(Packet):
    durate = models.IntegerField(null=False, blank=False, default=30)

    expiringDate = models.DateTimeField(null=False, auto_now=False, auto_now_add=False)


"""
CustomPacket Class
"""


class CustomPacket(Packet):
    startDate = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)

    endDate = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)
