from . import views
from django.urls import path
app_name='cinemaapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('MovieCategory/<slug:c_slug>/', views.home, name='movie_category'),
    path('Movies/<int:movie_id>/', views.detail, name='detail'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('add/', views.add_movie, name='add_movie'),
]