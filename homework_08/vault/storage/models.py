from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(verbose_name="name", max_length=50)

    # На уроке говорили, что так не стоит делать, но без указания в админке сущности висят как Object (1) и т.д.
    def __str__(self):
        return f"({self.id}) {self.name}"


class Type(models.Model):
    name = models.CharField(verbose_name="name", max_length=50)

    def __str__(self):
        return f"({self.id}) {self.name}"


class Secret(models.Model):
    name = models.CharField(verbose_name="name", max_length=50)
    value = models.TextField(verbose_name="value")
    desc = models.TextField(verbose_name="description", blank=True)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)

    def __str__(self):
        return f"({self.id}) {self.project.name} | {self.name}"
