from django.urls import path
from . import views

urlpatterns = [
    path('validate/', views.validate_data, name='validate_data'),
]
