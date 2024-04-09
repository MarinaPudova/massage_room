from django.contrib import admin

from massage_types.models import MassageType


# Register your models here.


@admin.register(MassageType)
class MassageTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'description', 'cost')
