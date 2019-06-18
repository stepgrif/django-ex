import uuid
from datetime import datetime

from django.http import HttpResponse
from rest_framework import viewsets

from topic_modeler.models import TopicModel, TopicExtractionJob, Topic, TopicWord
from topic_modeler.serializers import TopicModelSerializer, TopicSerializer, TopicWordSerializer, \
    TopicExtractionJobSerializer


class TopicModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TopicModel.objects.all().order_by('-id')
    serializer_class = TopicModelSerializer


class TopicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Topic.objects.all().order_by('-id')
    serializer_class = TopicSerializer


class TopicWordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TopicWord.objects.all().order_by('-id')
    serializer_class = TopicWordSerializer


class TopicExtractionJobViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TopicExtractionJob.objects.all().order_by('-id')
    serializer_class = TopicExtractionJobSerializer


def create_test_model(request):
    # model
    m = TopicModel()
    m.created_date = datetime.now()
    m.updated_date = datetime.now()
    m.perplexity = 0.0
    m.decomposition = 'LatentDirichletAllocation'
    m.features_extraction = 'CountVectorizer'
    m.inuse = False
    m.fitted_model = bytearray('test_insert_model', 'utf-8')
    m.save()
    m.refresh_from_db()
    # topic
    t = Topic()
    t.model = m
    t.created_date = datetime.now()
    t.inuse = False
    t.topic = 'test topic 1'
    t.save()
    t.refresh_from_db()
    # word
    w = TopicWord()
    w.topic = t
    w.created_date = datetime.now()
    w.word = 'test word 1'
    w.inuse = False
    w.save()
    # done
    return HttpResponse('Created test model, test topic with a word')


def create_test_topic_extraction(request):
    text_param = request.GET['text']
    model_id = request.GET['model_id']
    model_from_db = TopicModel.objects.get(id=model_id)
    if model_from_db and text_param:
        t = TopicExtractionJob()
        t.model = model_from_db
        t.created_date = datetime.now()
        t.updated_date = datetime.now()
        t.reference = str(uuid.uuid1())
        t.processed = False
        t.text = text_param
        t.save()
    return HttpResponse('Created test model')


def ping_topic_modeler(request):
    return HttpResponse('Topic modeler application online')
