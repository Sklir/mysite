from django.urls import path
from . import views
urlpatterns = [
    path('', views.main, name='post_list'),
    path('slim', views.slim, name='slim'),
    path('mass', views.mass, name='mass'),
    path('crossfit', views.crossfit, name='crossfit'),
]
