from django.contrib.auth.models import User
from django.db import models
from pump_app.model_classes.PacketCatalog import PacketCatalog
from pump_app.model_classes.PacketPrototype import PacketPrototype
from pump_app.model_classes.PacketState import PacketState
from pump_app.model_classes.Course import Course
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
import datetime

"""
Packet Class
"""
class Packet(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.TextField(null=True, blank=False, default='Undefined')

    description = models.TextField(null=True, blank=False)

    price = models.PositiveIntegerField(null=True, verbose_name="price")

    startDate = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)

    endDate = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)

    content_type_state = models.ForeignKey(ContentType, verbose_name="state", null=True, blank=True, related_name="contentTypes_Packets")

    object_id_state = models.PositiveIntegerField(null=True, verbose_name="object")

    state = GenericForeignKey('content_type_state', 'object_id_state',)

    packetcatalog = models.ForeignKey(PacketCatalog, null=True, blank=False, on_delete=models.CASCADE, related_name='packets')

    courses = models.ManyToManyField(Course, blank=False, related_name='courses')

    """
    It creates a new instance of Packet and saves it into db
    """
    def makeNewPacket(self):
        self.save()
        return self

        """
    It sets the arguments of the current Packet instance
    """
    def setInfo(self, name, description, price, startDate, endDate):
        self.name = name
        self.description = description
        self.price = price
        self.startDate = startDate
        self.endDate = endDate
        self.save()

    def __unicode__(self):
        return self.name + '(' + str(self.id) + ')'
