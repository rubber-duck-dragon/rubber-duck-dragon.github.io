from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('words', views.WordView)

urlpatterns = [
    path('', include(router.urls))
]