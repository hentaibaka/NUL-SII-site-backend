from rest_framework import generics
from .serializers import *
from .models import *


class ProjectAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class EmployeeAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class PublicationAPIView(generics.ListAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

class ContactAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
