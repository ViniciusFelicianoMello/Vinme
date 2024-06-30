from django.urls import path
from vinme.views import index, about, services, projects, contact, thankspage

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('projects/', projects, name='projects'),
    path('contact/', contact, name='contact'),
    path('thankspage/', thankspage, name='thankspage'),
]
