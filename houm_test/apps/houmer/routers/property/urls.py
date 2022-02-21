"""
Course router urls.

Part of routers.course module.
"""


from django.urls import path
from houmer.views.property import PropertyView

urlpatterns = [
    path('', PropertyView.as_view({
        'post': 'create',
        'get': 'list_by_logged'
    }), name='property'),

]
