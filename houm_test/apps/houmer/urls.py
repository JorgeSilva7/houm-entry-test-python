from django.urls import include, path

from houmer.routers.property import urls as property_urls
from houmer.routers.houmer import urls as houmer_urls
from houmer.routers.visit import urls as visit_urls

urlpatterns = [
    path('properties/', include(property_urls)),
    path('houmers/', include(houmer_urls)),
    path('visits/', include(visit_urls))
]
