from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

"""
SubscriptionState Class (Interface)
"""
class SubscriptionState(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.TextField(null=True, blank=False, unique=True, default='Undefined')

    def __unicode__(self):
        return self.name + '(' + str(self.id) + ')'

"""
ActiveSubscription Class (Singleton)
"""
class ActiveSubscription(SubscriptionState):

    def setName(self):
        self.name = "Active"
        self.save()

    def setState(self, subscription):
        subscription.state = self

"""
InactiveSubscription Class (Singleton)
"""
class InactiveSubscription(SubscriptionState):

    def setName(self):
        self.name = "Inactive"
        self.save()

    def setState(self, subscription):
        subscription.state = self

"""
ExpiredSubscription Class (Singleton)
"""
class ExpiredSubscription(SubscriptionState):

    def setName(self):
        self.name = "Expired"
        self.save()

    def setState(self, subscription):
        subscription.state = self