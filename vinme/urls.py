from django.urls import path
from vinme.views import index

urlpatterns = [
    path('', index, name='index'),
]