from rest_framework import serializers
from subscription.model_classes.Subscription import Subscription

"""
SubscriptionSerializer Class
"""
class SubscriptionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Subscription
		fields = ('id', 'startDate', 'endDate', 'packets', 'state')
		read_only_fields = ('id', 'startDate', 'endDate', 'packets')
