from django.http import HttpResponse


# Create your views here.

def topic_modeler_ping(request):
    return HttpResponse('Topic modeler application online')
