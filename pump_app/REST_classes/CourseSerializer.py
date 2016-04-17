from pump_app.model_classes.Course import Course
from rest_framework import serializers
from django.contrib.auth.models import User
from pump_app.model_classes.State import Activated, Deactivated, Incomplete, Trashed
from pump_app.model_classes.utility.Utility import Utility
from pump_app.libraries.generic_relations.relations import GenericRelatedField
import json

class StateField(serializers.RelatedField):

    def to_representation(self, value):

        return value.__class__.__name__


class CourseSerializer(serializers.ModelSerializer):
    state = StateField(read_only=True)

    class Meta:
		model = Course

		fields = ('id', 'name', 'description', 'closed', 'subscrNumber', 'startDate', 'endDate', 'coursecatalog', 'state')

    #il metodo update e' stato sovrascritto per permettere la gestione dello state(genericForeignKey!)
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
