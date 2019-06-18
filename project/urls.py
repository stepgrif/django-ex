from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from topic_modeler.views import ping_topic_modeler, TopicModelViewSet, create_test_model, create_test_topic_extraction, \
    TopicExtractionJobViewSet, TopicWordViewSet, TopicViewSet

router = routers.DefaultRouter()
router.register(r'models', TopicModelViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'words', TopicWordViewSet)
router.register(r'topic_extractions', TopicExtractionJobViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^$', index),
    # url(r'^health$', health),
    url(r'^ping_topic_modeler', ping_topic_modeler),
    url(r'^create_test_model', create_test_model),
    url(r'^create_test_topic_extraction', create_test_topic_extraction),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rest_api/', include(router.urls))
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [url(r'^__debug__/', include(debug_toolbar.urls)), ] + urlpatterns
