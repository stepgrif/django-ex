from rest_framework import serializers

from topic_modeler.models import TopicModel, TopicExtractionJob, Topic, TopicWord, TrainData, DataRaw


class DataRawSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataRaw
        fields = ('created_date', 'text')


class TrainDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrainData
        fields = ('created_date', 'text')


class TopicModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TopicModel
        fields = ('created_date', 'updated_date', 'perplexity', 'decomposition', 'features_extraction', 'inuse')


class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = ('model', 'created_date', 'topic', 'inuse')


class TopicWordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TopicWord
        fields = ('topic', 'created_date', 'word', 'inuse')


class TopicExtractionJobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TopicExtractionJob
        fields = ('model', 'created_date', 'updated_date', 'reference', 'processed', 'text')
