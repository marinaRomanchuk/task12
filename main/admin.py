from django.contrib import admin
from main.models import InputData


class InputDataAdmin(admin.ModelAdmin):
    list_display = ("id", "data")


admin.site.register(InputData, InputDataAdmin)
