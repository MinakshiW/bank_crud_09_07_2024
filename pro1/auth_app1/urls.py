from django.urls import path
from .views import  *

urlpatterns = [
    path('suv/', signview),
    path('lv/', loginview),
    path('lov/', logoutview),
]