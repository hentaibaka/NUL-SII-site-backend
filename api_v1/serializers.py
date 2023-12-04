from rest_framework import serializers
from .models import *
 

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('photo', 'title', 'description', 'is_realized', 'type', 'slug')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('photo', 'post', 'last_name', 'first_name', 'patronymic', 'link')

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ('title', 'authors', 'journal', 'link')

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'question')

class PortfoloSerializer(serializers.ModelSerializer):
    authors = EmployeeSerializer(read_only=True, many=True)
    class Meta:
        model = Project
        fields = ('photo', 'title', 'authors', 'description', 'instruction', 'is_realized', 'type', 'slug')
 