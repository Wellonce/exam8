from django.urls import path
from .views import homeView, search_vacancies

urlpatterns = [
    path('', homeView, name='home'),
    path('search/', search_vacancies, name='search_vacancies'),
]
