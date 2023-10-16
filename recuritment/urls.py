from django.urls import path, include

from recuritment.views import RecuritmentListAPIView, RecuritmentCreateAPIView

urlpatterns = [
    path('recuritment/list/', RecuritmentListAPIView.as_view(), name='recuritment-list'),
    path('recuritment/', RecuritmentCreateAPIView.as_view(), name='recuritment-create')
]