from django.urls import path

from . import views


urlpatterns = [
    # View for the homepage.
    path('', views.index, name='home'),
]
