from . import views
from django.urls import path
app_name='searchApp'
urlpatterns = [
    path('', views.SearchResult, name='SearchResult'),
]