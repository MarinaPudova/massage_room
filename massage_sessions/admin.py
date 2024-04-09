from django.contrib import admin

from massage_sessions.models import MassageSession


# Register your models here.


@admin.register(MassageSession)
class MassageMasterAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'session_master', 'session_type', 'client_name',
        'client_phone', 'session_date', 'session_status', 'session_comment',
    )
