from rest_framework import viewsets

from topic_modeler.models import RunningTasks, DataRaw, TrainData, TopicModel, Topic, TopicWord, TopicExtractionJob
from topic_modeler.serializers import RunningTasksSerializer, DataRawSerializer, TrainDataSerializer, \
    TopicModelSerializer, TopicSerializer, TopicWordSerializer, TopicExtractionJobSerializer


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
