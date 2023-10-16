from django.urls import path, include

from recuritment.views import RecuritmentListAPIView, RecuritmentCreateAPIView, RecuritmentUpdateAPIView

urlpatterns = [
    path('recuritment/list/', RecuritmentListAPIView.as_view(), name='recuritment-list'),
    path('recuritment/', RecuritmentCreateAPIView.as_view(), name='recuritment-create'),
    path('recuritment/<int:pk>/', RecuritmentUpdateAPIView.as_view(), name='recuritment-update'),
]