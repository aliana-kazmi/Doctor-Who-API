from django.urls import path
from .views import *

urlpatterns = [
    path('',GadgetView, name='all-gadgets'),
    path('<int:pk>/',GadgetView, name='search-gadget' ),
]