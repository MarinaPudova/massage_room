from django import forms

from client_comments.models import ClientComment


class ClientCommentForm(forms.ModelForm):
    class Meta:
        model = ClientComment
        fields = ('content', 'rating')
        labels = {'content': 'Отзыв', 'rating': 'Оценка'}
