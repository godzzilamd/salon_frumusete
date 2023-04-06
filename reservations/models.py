from django.db import models
from drf_util.models import CommonModel

from services.models import Service
from workers.models import Worker


class Reservation(CommonModel):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='workers')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='services')
    time = models.DateTimeField(max_length=20)
