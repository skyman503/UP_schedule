from django.urls import path
from .views import homepage

urlpatterns = [
    path('<offset>', homepage),
    path('', homepage)
]
