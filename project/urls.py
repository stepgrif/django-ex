from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from topic_modeler.views import ping_topic_modeler, TopicModelViewSet, TopicExtractionJobViewSet, TopicWordViewSet, \
    TopicViewSet, TrainDataViewSet, DataRawViewSet, RunningTasksViewSet, \
    train_model, extract_topic

router = routers.DefaultRouter()
router.register(r'models', TopicModelViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'words', TopicWordViewSet)
router.register(r'topic_extractions', TopicExtractionJobViewSet)
router.register(r'train_data', TrainDataViewSet)
router.register(r'data_raw', DataRawViewSet)
router.register(r'running_tasks', RunningTasksViewSet)

urlpatterns = [
    # for testing
    url(r'^ping_topic_modeler', ping_topic_modeler),
    # for working
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rest_api/', include(router.urls)),
    url(r'^train_model/', train_model),
    url(r'^extract_topic/', extract_topic)
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [url(r'^__debug__/', include(debug_toolbar.urls)), ] + urlpatterns
