from django.db import models

from member.models import Member
from recuritment.models import Recuritment

class Application(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    recuritment = models.ForeignKey(Recuritment, on_delete=models.CASCADE)

    def __str__(self):
        return f"Apply {self.member} / {self.recuritment}"