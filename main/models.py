from django.db import models


class InputData(models.Model):
    data = models.JSONField()

    class Meta:
        verbose_name = "Input data"
        verbose_name_plural = "Input data"
