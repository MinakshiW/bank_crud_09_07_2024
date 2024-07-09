from django.urls import path
from .views import *

urlpatterns = [
    path('hv/', homeview),
    path('bv/', bankview),
    path('sv/', showview),
    path('uv/<int:pk>/', updateview),
    path('dv/<int:x>/', deleteview),
]