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

""" 채용공고 삭제 Serializer """
class RecuritmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recuritment
        fields = '__all__'

""" 채용공고 상세 조회 Serializer """
class RecuritmentDetialSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source = 'company.name')
    nation = serializers.CharField(source = 'company.nation')
    region = serializers.CharField(source = 'company.region')
    recuritments = serializers.SerializerMethodField()

    class Meta:
        model = Recuritment
        fields = ("id",
                  "company_name",
                  "nation",
                  "region", 
                  "position",
                  "compensation",
                  "tech",
                  "contents",
                  "recuritments")
    
    """ `SerializerMethodField`는 `get_<field_name>`에 작성한 결과가 포함된다. """
    def get_recuritments(self, obj):
        return [recruit.id for recruit in Recuritment.objects.filter(company=obj.company).exclude(id=obj.id)]
