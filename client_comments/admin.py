from django.contrib import admin

from client_comments.models import ClientComment


# Register your models here.

@admin.register(ClientComment)
class ClientCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'rating', 'created_at', 'master')
