from django.http import JsonResponse
from rest_framework.views import Response
from rest_framework.decorators import api_view
import requests


# Create your views here.
def get_ip_location(ip):
    
    try:
        response = requests.get(f'https://ipapi.co/{ip}/json/')
        response.raise_for_status()
        data = response.json()
        print(data)

        location = data.get('city', 'New York')
        return location
    except requests.RequestException:
        return 'New York'
    
def get_ip(request):
    x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forw_for is not None:
        ip = x_forw_for.spilt(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    return ip

@api_view(['GET'])
def hello(request):
    name = request.GET.get('visitor_name', 'Mark')
    client_ip =get_ip(request) # request.META.get('REMOTE_ADDR')
    location = get_ip_location(ip=client_ip)

    data = {
        'client_ip': client_ip,
        'location': location,
        'greeting': f'Hello, {name}!, the temperature is 11 degree Celcius in {location}'
    }

    return Response(data)


