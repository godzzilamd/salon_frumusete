from django.db import models
from drf_util.models import CommonModel


class Service(CommonModel):
    name = models.CharField(max_length=160, null=False)
    price = models.FloatField(default=0)
    cover_photo = models.FileField()
    category = models.CharField(max_length=20, default='common')

    def __str__(self):
        return "test"
