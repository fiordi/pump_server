from pump_app.model_classes.Course import Course
from rest_framework import serializers
from django.contrib.auth.models import User
from pump_app.model_classes.State import Activated, Deactivated, Incomplete, Trashed
from pump_app.model_classes.utility.Utility import Utility
from pump_app.libraries.generic_relations.relations import GenericRelatedField
import json

"""
StateField Class
"""
class StateField(serializers.RelatedField):

    """
    It returns the name of the class as output instead of the object

    value => Activated(), Deactivated(), Trashed(), Incomplete()
    """
    def to_representation(self, value):

        return value.__class__.__name__

"""
CourseSerializer Class
"""
class CourseSerializer(serializers.ModelSerializer):
    state = StateField(read_only=True)

    class Meta:
		model = Course

		fields = ('id', 'name', 'description', 'closed', 'subscrNumber', 'startDate', 'endDate', 'coursecatalog', 'state')

    """
    It overrides the default __update()__ method of REST API in order to allow writing of state field (GenericForeignKey!)

    instance => Course()
    validated_data => Unknown

    :return Course()
    """
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.closed = validated_data.get('closed', instance.closed)
        instance.subscrNumber = validated_data.get('subscrNumber', instance.subscrNumber)
        instance.startDate = validated_data.get('startDate', instance.startDate)
        instance.endDate = validated_data.get('endDate', instance.endDate)
        instance.coursecatalog = validated_data.get('coursecatalog', instance.coursecatalog)
        instance.save()
        course_request = self.context['request'].data
        if 'state' in course_request.keys():
            state_to_be_setted = Utility().str_to_class(str(course_request['state']))
            instance.setState(state_to_be_setted)
        return instance
