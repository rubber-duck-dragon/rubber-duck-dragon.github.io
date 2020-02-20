from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'students'
urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
]