from django.urls import path, include
from application.views import MemberApplyAPIView

urlpatterns = [
    path('recuritment/apply/', MemberApplyAPIView.as_view(), name='recuritment-apply'),
]