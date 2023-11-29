from django.urls import path
from .views import *

urlpatterns = [
    path('get-projects/', (ProjectAPIView.as_view()), name='getprojects'),
    path('get-employees/', (EmployeeAPIView.as_view()), name='getemployees'),
    path('get-publications/', (PublicationAPIView.as_view()), name='getpublications'),
    path('create-contact/', (ContactAPIView.as_view()), name='createcontact'),
]