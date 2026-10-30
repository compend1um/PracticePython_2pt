from django.db import models


class GPU(models.Model):
    brand = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    video_memory_GB = models.IntegerField()
    video_memory_type = models.IntegerField()

    objects = models.Manager()
    DoesNotExist = models.Manager
