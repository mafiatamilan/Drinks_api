from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

def drinks_list(request):
    drink = Drink.objects.all()
    serializer = DrinkSerializer(drink,many=True)
    return JsonResponse(serializer.data,safe=False)