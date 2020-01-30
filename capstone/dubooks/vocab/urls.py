from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # path('', TemplateView.as_view(template_name="vocab/home_page.html"))
    path('', views.tokenize, name="tokenize")
]