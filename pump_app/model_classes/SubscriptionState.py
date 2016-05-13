from django.db import models
from solo.models import SingletonModel

"""
SubscriptionState Class (Interface)
"""
class SubscriptionState(models.Model):

    def setSubscriptionState(self, Course):
        pass

    class Meta:
		abstract = True


"""
SubscriptionActive Class (Singleton)
"""
class SubscriptionActive(SingletonModel, State):
    id = models.AutoField(primary_key=True)

    verbose_name = models.CharField(max_length=200, null=True, verbose_name="Active")

    """
    It sets the current SubscriptionActive instance to a Subscription

    Subscription => Subscription()
    """
    def setSubscriptionActiveState(self, Subscription):
        #la classe SingletonModel non assegna la pk all'oggetto. Le genericForeignKey tuttavia basano il loro funzionamento su di
        #esso, pertanto viene settato manualmente
        self.id = 1
        self.save()

        Course.state = self



"""
SubscriptionExpired Class (Singleton)
"""
class SubscriptionExpired(SingletonModel, State):
    id = models.AutoField(primary_key=True)

    verbose_name = models.CharField(max_length=200, null=True, verbose_name="Expired")

    """
    It sets the current SubscriptionExpired instance to a Subscription

    Subscription => Subscription()
    """
    def setSubscriptionExpiredState(self, Subscription):
        #la classe SingletonModel non assegna la pk all'oggetto. Le genericForeignKey tuttavia basano il loro funzionamento su di
        #esso, pertanto viene settato manualmente
        self.id = 1
        self.save()

        Course.state = self