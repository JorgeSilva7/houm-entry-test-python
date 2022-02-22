from django.urls import path
from houmer.views.visit import VisitView

urlpatterns = [
    path('', VisitView.as_view({
        'post': 'create',
        'get': 'getByHoumer'
    }), name='visit'),
    path('<pk>/end', VisitView.as_view({
        'patch': 'end',
    }), name='visit_end'),

]
