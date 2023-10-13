from django.db import models

class Company(models.Model):
    """
    채용공고를 등록할 수 있는 회사 모델입니다.
    """
    name = models.CharField("회사명", max_length=50)
    address = models.CharField("주소", max_length=200)
    nation = models.CharField("국가", max_length=50)
    region = models.CharField("지역", max_length=50)

    def __str__(self):
        return self.name