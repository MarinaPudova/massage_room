from django import forms

from info_news.models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('news_title', 'news_content', 'news_date')
        labels = {'news_title': 'Название новости', 'news_content': 'Новость', 'news_date': 'Дата публикации'}
