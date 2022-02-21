from django.urls import path
from houmer.views.houmer import HoumerView

urlpatterns = [
    path('', HoumerView.as_view({
        'post': 'create',
    }), name='houmer_create'),
]
