from django.contrib import admin
from storage.models import (
    Secret,
    Project,
    Type,
)


# Register your models here.
admin.site.register(Secret)
admin.site.register(Project)
admin.site.register(Type)
