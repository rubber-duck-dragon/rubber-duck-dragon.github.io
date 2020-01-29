from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register('words', views.WordView)
router.register('lists', views.ListView)
router.register('users', views.UserView)

urlpatterns = [

] + router.urls
