"""Users URLs"""

# django
from django.urls import path,include

# Django REST framework
from rest_framework.routers import DefaultRouter

# Views
from .views import UserViewSet


router = DefaultRouter()
router.register(r'',UserViewSet,basename='users')

urlpatterns  = [
    path('',include(router.urls))
]