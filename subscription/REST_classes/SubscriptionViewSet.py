from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, filters, generics
from subscription.model_classes.Subscription import Subscription
from subscription.REST_classes.SubscriptionSerializer import SubscriptionSerializer


"""
SubscriptionViewSet Class
"""
class SubscriptionViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

	queryset = Subscription.objects.all()
	serializer_class = SubscriptionSerializer