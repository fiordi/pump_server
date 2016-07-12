from django.contrib import admin

from subscription.models import Subscription
from subscription.models import SubscriptionState, ActiveSubscription

admin.site.register(Subscription)
admin.site.register(ActiveSubscription)
