from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveAPIView
from recuritment.models import Recuritment
from recuritment.serializers import RecuritmentCreateSerializer, RecuritmentDetialSerializer, RecuritmentListSerializer, RecuritmentSerializer, RecuritmentUpdateSerializer
from rest_framework.response import Response
from rest_framework import status

from django.db.models import Q

""" 채용공고 목록 조회 및 검색 """
class RecuritmentListAPIView(ListAPIView):
    queryset = Recuritment.objects.all()
    serializer_class = RecuritmentListSerializer
    
    def get(self, request):
        keyword = self.request.GET.get('search', '')

        if keyword:
            qs = Recuritment.objects.filter(
                Q(company__name__contains=keyword)
                |Q(position__contains=keyword)
                |Q(tech__contains=keyword))
        else:
            qs = Recuritment.objects.all()
        
        serializer = RecuritmentListSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


""" 채용공고 등록 """
class RecuritmentCreateAPIView(CreateAPIView):
    queryset = Recuritment.objects.all()
    serializer_class = RecuritmentCreateSerializer


""" 채용공고 수정 """
class RecuritmentUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Recuritment.objects.all()
    serializer_class = RecuritmentUpdateSerializer


""" 채용공고 삭제 """
class RecuritmentDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Recuritment.objects.all()
    serializer_class = RecuritmentSerializer


""" 채용공고 상세 조회 """
class RecuritmentDetailAPIView(RetrieveAPIView):
    queryset = Recuritment.objects.all()
    serializer_class = RecuritmentDetialSerializer