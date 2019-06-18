from datetime import datetime

from django.http import HttpResponse
from rest_framework import viewsets

from topic_modeler.models import TopicModel
from topic_modeler.serializers import TopicModelSerializer


class TopicModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TopicModel.objects.all().order_by('-id')
    serializer_class = TopicModelSerializer


def test_insert_model(request):
    m = TopicModel()
    m.created_date = datetime.now()
    m.updated_date = datetime.now()
    m.perplexity = 0.0
    m.decomposition = 'LatentDirichletAllocation'
    m.features_extraction = 'CountVectorizer'
    m.fitted_model =  bytearray('test_insert_model', 'utf-8')
    m.save()
    return HttpResponse('Created test model')


def topic_modeler_ping(request):
    return HttpResponse('Topic modeler application online')
