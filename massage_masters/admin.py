from django.contrib import admin

from massage_masters.models import MassageMaster, MasterType


# Register your models here.


@admin.register(MassageMaster)
class MassageMasterAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'last_name', 'about_master', 'master_experience', 'master_rating', 'is_working', 'master_foto',
    )
    # list_display = ('id', 'name', 'last_name', 'about_master', 'master_experience', 'master_rating', 'is_working',
    # 'master_foto', 'master_types')


@admin.register(MasterType)
class MasterTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'master', 'type')
