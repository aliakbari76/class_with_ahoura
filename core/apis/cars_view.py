from core.models import Car
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

class CarsView(APIView):
    def get(self , request):
        all_cars =  Car.objects.all()
        print(all_cars)
        allcars = []
        for car in all_cars:
            allcars.append(str(car))
        print(allcars)
        return Response(data = allcars)