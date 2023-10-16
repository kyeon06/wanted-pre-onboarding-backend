from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from recuritment.models import Recuritment
from recuritment.serializers import RecuritmentCreateSerializer, RecuritmentListSerializer, RecuritmentUpdateSerializer
from django.shortcuts import get_object_or_404

""" 채용공고 목록 조회 """
class RecuritmentListAPIView(ListAPIView):
    queryset = Recuritment.objects.all()
    serializer_class = RecuritmentListSerializer

""" 채용공고 등록 """
class RecuritmentCreateAPIView(CreateAPIView):
    queryset = Recuritment.objects.all()
    serializer_class = RecuritmentCreateSerializer

""" 채용공고 수정 """
class RecuritmentUpdateAPIView(UpdateAPIView):
    queryset = Recuritment.objects.all()
    serializer_class = RecuritmentUpdateSerializer