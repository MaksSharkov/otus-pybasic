from django.db import models


# Create your models here.
class Secret(models.Model):
    name = models.CharField(verbose_name="name", max_length=50)
    value = models.TextField(verbose_name="value")
    desc = models.TextField(verbose_name="description", blank=True)
    type = models.CharField(verbose_name="type", max_length=30)
