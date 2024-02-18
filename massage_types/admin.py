from django.contrib import admin

from massage_types.models import MassageType


# Register your models here.


@admin.register(MassageType)
class MassageTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'cost')
    # list_display = ('id', 'name', 'description', 'cost', 'massage_cover')
