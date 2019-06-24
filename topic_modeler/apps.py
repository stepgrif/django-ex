import logging

import nltk
from django.apps import AppConfig

logger = logging.getLogger(__name__)


class TopicModelerConfig(AppConfig):
    name = 'topic_modeler'

    def ready(self):
        logger.debug('Loaded stopwords')
        nltk.download('stopwords', quiet=True)
