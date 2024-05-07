from django.urls import path
from. import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('moskow', views.moskow, name='moskow'),
    path('saint-petersburg', views.saint_petersburg, name='saint-petersburg'),
]