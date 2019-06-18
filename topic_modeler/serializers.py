from rest_framework import serializers

from topic_modeler.models import TopicModel, TopicExtractionJob, Topic, TopicWord


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
