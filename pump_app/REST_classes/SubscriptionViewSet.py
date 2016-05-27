from pump_app.model_classes.Subscription import Subscription
from rest_framework import viewsets, permissions, filters, generics
from pump_app.REST_classes.SubscriptionSerializer import SubscriptionSerializer
from django.shortcuts import get_object_or_404

"""
SubscriptionViewSet Class
"""
class SubscriptionViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

	queryset = Subscription.objects.all()
	serializer_class = SubscriptionSerializer