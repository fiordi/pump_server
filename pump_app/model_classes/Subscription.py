from django.contrib.auth.models import User
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from pump_app.model_classes.Packet import Packet
from pump_app.model_classes.Customer import Customer
import datetime

"""
Subscription Class
"""
class Subscription(models.Model):
    id = models.AutoField(primary_key=True)

    startDate = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)

    endDate = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)

    customer = models.ForeignKey(Customer, null=True, blank=False, related_name='costumer')

    packets = models.ManyToManyField(Packet , blank=False, related_name='subscriptions')

    content_type_state = models.ForeignKey(ContentType, verbose_name="state", null=True, blank=True, related_name="contentTypes_Subscriptions")

    object_id_state = models.PositiveIntegerField(null=True, verbose_name="object")

    state = GenericForeignKey('content_type_state', 'object_id_state',)


    """
    It creates a new instance of Subscription and saves it into db
    """
    def makeNewSubscription(self):
        self.save()
        return self

        """
    It sets the arguments of the current Subscription instance
    """
    def setInfo(self, startDate, endDate):
        self.startDate = startDate
        self.endDate = endDate
        self.save()

    def __unicode__(self):
        return self.name + '(' + str(self.id) + ')'
