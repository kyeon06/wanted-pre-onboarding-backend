from django.urls import path, include

from recuritment.views import RecuritmentListAPIView, RecuritmentCreateAPIView, RecuritmentUpdateAPIView, RecuritmentDestroyAPIView

urlpatterns = [
    path('recuritment/list/', RecuritmentListAPIView.as_view(), name='recuritment-list'),
    path('recuritment/', RecuritmentCreateAPIView.as_view(), name='recuritment-create'),
    path('recuritment/update/<int:pk>/', RecuritmentUpdateAPIView.as_view(), name='recuritment-update'),
    path('recuritment/delete/<int:pk>/', RecuritmentDestroyAPIView.as_view(), name='recuritment-delete')
]