from django.db import models

from company.models import Company

class Recuritment(models.Model):
    """
    기업이 등록한 채용 공고 모델입니다.
    """
    position = models.CharField("채용포지션", max_length=50)
    compensation= models.IntegerField("채용보상금", default=0)
    contents = models.TextField("채용내용")
    tech = models.CharField("사용기술", max_length=100)

    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
