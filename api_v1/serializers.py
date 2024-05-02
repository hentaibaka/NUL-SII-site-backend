from dataclasses import fields
from rest_framework import serializers
from .models import *
 

class ProjectSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        return obj.photo.url
    class Meta:
        model = Project
        fields = ('photo', 'title', 'description', 'is_realized', 'type', 'slug')

    


class EmployeeSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        return obj.photo.url
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
    photo = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        return obj.photo.url
    class Meta:
        model = Project
        fields = ('photo', 'title', 'authors', 'description', 'instruction', 'is_realized', 'type', 'slug')
 
class ArticleSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        return obj.photo.url
    class Meta:
        model = Article
        fields = ('title', 'desc', 'text', 'slug', 'date', 'photo')