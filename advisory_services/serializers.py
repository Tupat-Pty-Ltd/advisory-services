from rest_framework import serializers

from .models import BioData, Message, ServicePrograme


class BioDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BioData
        fields = [
            'name', 'email', 'dob',
            'cell', 'education',
            'occupation']
        


class ServiceProgrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePrograme
        fields = [
            'message', 'start_date', 'start_end',
            'age_group', 'gender', 'education',
            'program_description']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['subject', 'message_body', 'recipient',
                  'message_platform']