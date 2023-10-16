from rest_framework import serializers

from recuritment.models import Recuritment

""" 채용공고 목록 조회 Serializer """
class RecuritmentListSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source = 'company.name')
    nation = serializers.CharField(source = 'company.nation')
    region = serializers.CharField(source = 'company.region')

    class Meta:
        model = Recuritment
        fields = ("id",
                  "company_name",
                  "nation",
                  "region", 
                  "position",
                  "compensation",
                  "tech")

""" 채용공고 등록 Serializer """
class RecuritmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recuritment
        fields = ("company", "position", "compensation", "contents", "tech")

""" 채용공고 수정 Serializer """
class RecuritmentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recuritment
        fields = ("position", "compensation", "contents", "tech")
