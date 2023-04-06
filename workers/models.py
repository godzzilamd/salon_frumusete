from django.db import models
from drf_util.models import CommonModel


class Worker(CommonModel):
    name = models.CharField(max_length=160, null=False)
    position = models.CharField(max_length=100)
    description = models.CharField(max_length=300, default="")
    cover_photo = models.FileField(null=True)
    experience = models.FloatField(default=0)
