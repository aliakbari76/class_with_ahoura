from django.urls import path
from core.apis.cars_view import CarsView
urlpatterns = [
    path('cars/' , CarsView.as_view() , name ='cars_list')
]