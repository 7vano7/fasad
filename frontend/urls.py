
from django.urls import path
#from django.conf.urls.i18n import i18n_patterns
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about', views.about, name = 'about'),
    path('factory', views.factory, name = 'factory'),
    path('production', views.production, name = 'production'),
    path('dostavka', views.dostavka, name = 'dostavka'),
    path('contacts', views.contacts, name = 'contacts'),
]

#urlpatterns = i18n_patterns('',
#    urlpatterns = i18n_patterns('', url(r'^$', 'views.home', name = 'home'),
#    url(r'^/about/$', 'views.about, name' = 'about'),
#    url(r'^/factory/$', 'views.factory', name = 'factory'),
#    url(r'^/production/$', 'views.production', name = 'production'),
#    url(r'^/dostavka/$', 'views.dostavka', name = 'dostavka'),
#    url(r'^/contacts/$', 'views.contacts', name = 'contacts')),
#)
