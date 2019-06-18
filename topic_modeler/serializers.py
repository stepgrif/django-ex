from rest_framework import serializers

from topic_modeler.models import TopicModel


class TopicModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TopicModel
        fields = ('created_date', 'updated_date', 'perplexity', 'decomposition', 'features_extraction')
