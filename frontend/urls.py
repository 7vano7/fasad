
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about', views.about, name = 'about'),
    path('factory', views.factory, name = 'factory'),
    path('production', views.production, name = 'production'),
    path('dostavka', views.dostavka, name = 'dostavka'),
    path('contacts', views.contacts, name = 'contacts'),
]
