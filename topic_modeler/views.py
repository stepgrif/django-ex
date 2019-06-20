from django.http import HttpResponse
from rest_framework import viewsets

from topic_modeler.models import TopicModel, TopicExtractionJob, Topic, TopicWord, TrainData, DataRaw, RunningTasks
from topic_modeler.serializers import TopicModelSerializer, TopicSerializer, TopicWordSerializer, \
    TopicExtractionJobSerializer, TrainDataSerializer, DataRawSerializer, RunningTasksSerializer


class RunningTasksViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RunningTasks.objects.all().order_by('-id')
    serializer_class = RunningTasksSerializer


class DataRawViewSet(viewsets.ModelViewSet):
    queryset = DataRaw.objects.all().order_by('-id')
    serializer_class = DataRawSerializer


class TrainDataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TrainData.objects.all().order_by('-id')
    serializer_class = TrainDataSerializer


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


def ping_topic_modeler(request):
    return HttpResponse('Topic modeler application online')


def create_test_model(request):
    # model
    m = TopicModel()
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
    t.inuse = False
    t.topic = 'test topic'
    t.save()
    t.refresh_from_db()
    # word
    w = TopicWord()
    w.topic = t
    w.word = 'test word'
    w.inuse = False
    w.save()
    # done
    return HttpResponse('Created test model, test topic with a word')
