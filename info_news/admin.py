from django.contrib import admin

from info_news.models import News


# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'news_title', 'news_content', 'news_date')
