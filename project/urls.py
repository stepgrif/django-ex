from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from topic_modeler.views import topic_modeler_ping, TopicModelViewSet, test_insert_model

router = routers.DefaultRouter()
router.register(r'models', TopicModelViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^$', index),
    # url(r'^health$', health),
    url(r'^topic_modeler_ping', topic_modeler_ping),
    url(r'^test_insert_model', test_insert_model),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rest_api/', include(router.urls))
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [url(r'^__debug__/', include(debug_toolbar.urls)), ] + urlpatterns
