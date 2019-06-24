# import os
#
# from django.http import HttpResponse
# from rest_framework import viewsets
#
# from rest_framework import viewsets
#
# from topic_modeler.models import TopicModel, TopicExtractionJob, Topic, TopicWord, TrainData, DataRaw, RunningTasks
# from topic_modeler.serializers import TopicModelSerializer, TopicSerializer, TopicWordSerializer, \
#     TopicExtractionJobSerializer, TrainDataSerializer, DataRawSerializer, RunningTasksSerializer
#
#
# class RunningTasksViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = RunningTasks.objects.all().order_by('-id')
#     serializer_class = RunningTasksSerializer
#
#
# class DataRawViewSet(viewsets.ModelViewSet):
#     queryset = DataRaw.objects.all().order_by('-id')
#     serializer_class = DataRawSerializer
#
#
# class TrainDataViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = TrainData.objects.all().order_by('-id')
#     serializer_class = TrainDataSerializer
#
#
# class TopicModelViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = TopicModel.objects.all().order_by('-id')
#     serializer_class = TopicModelSerializer
#
#
# class TopicViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Topic.objects.all().order_by('-id')
#     serializer_class = TopicSerializer
#
#
# class TopicWordViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = TopicWord.objects.all().order_by('-id')
#     serializer_class = TopicWordSerializer
#
#
# class TopicExtractionJobViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = TopicExtractionJob.objects.all().order_by('-id')
#     serializer_class = TopicExtractionJobSerializer



import os

from django.http import HttpResponse

from topic_modeler.models import PageView
from topic_modeler.topic_modeler import schedule_train_topic_model, do_topic_extraction


def train_model(request):
    # extract parameters
    number_of_topics = request.GET['number_of_topics']
    words_per_topic = request.GET['words_per_topic']
    # schedule job
    message = schedule_train_topic_model(number_of_topics, words_per_topic)
    # done
    return HttpResponse(message)


def extract_topic(request):
    # extract parameters
    text = request.GET['text']
    # schedule job
    message = do_topic_extraction(text)
    # done
    return HttpResponse(message)


def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)
    return HttpResponse(PageView.objects.count())


def health(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)
    return HttpResponse(PageView.objects.count())
