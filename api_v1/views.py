from rest_framework import generics
from rest_framework import viewsets
from .serializers import *
from .models import *


class PorfolioAPIView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    queryset = Project.objects.all()
    serializer_class = PortfoloSerializer

class ProjectAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class EmployeeAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class PublicationAPIView(generics.ListAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

class ContactAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
