from django.contrib.auth.models import User
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from pump_app.model_classes.Packet import Packet
from pump_app.model_classes.SubscriptionState import SubscriptionState
import datetime

"""
Subscription Class
"""
class Subscription(models.Model):
    id = models.AutoField(primary_key=True)

    startDate = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)

    endDate = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)

    packets = models.ManyToManyField(Packet , blank=False, related_name='subscriptions')

    state = models.ForeignKey(SubscriptionState, to_field='name', null=True, blank=False, on_delete=models.PROTECT, related_name='subscriptions')

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
        return str(self.endDate) + '(' + str(self.id) + ')'
