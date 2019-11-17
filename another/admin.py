from django.contrib import admin

# Register your models here.
from another.models import AnotherModel

admin.site.register(AnotherModel)
