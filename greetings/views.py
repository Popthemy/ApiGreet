from django.http import JsonResponse


# Create your views here.

def hello(request):
    name = request.GET.get('visitor_name', 'Mark')
    client_ip = request.META.get('REMOTE_ADDR', '127.0.0.1')
    location = "New York"

    data = {
        'client_ip': client_ip,
        'location': location,
        'greeting': f'Hello, {name}!'
    }

    return JsonResponse(data)