from django.urls import path
from .views import *

urlpatterns = [
    path('get-projects/', (ProjectAPIView.as_view()), name='getprojects'),
    path('get-projects/<slug:slug>/', (PorfolioAPIView.as_view()), name='getproject'),
    path('get-employees/', (EmployeeAPIView.as_view({'get': 'list'})), name='getemployees'),
    path('get-employees/<int:pk>', (EmployeeAPIView.as_view({'get': 'retrieve'})), name='getemployee'),
    path('get-publications/', (PublicationAPIView.as_view()), name='getpublications'),
    path('create-contact/', (ContactAPIView.as_view()), name='createcontact'),
]