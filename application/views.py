from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from application.models import Application
from application.serializers import ApplicationSerializer

""" 사용자가 채용공고에 지원한다. """
class MemberApplyAPIView(CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def post(self, request):
        member = request.data["member"]
        check = Application.objects.filter(member_id=member).exists()
        
        if check:
            return Response({"message" : "지원한 내역이 있습니다. 사용자는 1회만 지원 가능합니다."}, status = status.HTTP_400_BAD_REQUEST)
        else:
            serializer = ApplicationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
