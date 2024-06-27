from django.urls import path
from vinme.views import index, contact, thankspage

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('thankspage/', thankspage, name='thankspage'),
]
