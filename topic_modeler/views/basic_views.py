import os

from django.http import HttpResponse

from topic_modeler.models import PageView


def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)
    return HttpResponse(PageView.objects.count())


def health(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)
    return HttpResponse(PageView.objects.count())
