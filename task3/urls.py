from django.urls import path
from . import views

urlpatterns = [
    path('', views.encrypt_data, name='enc-page'),
    path('dec/', views.decrypt_data, name='dec-page'),
]
