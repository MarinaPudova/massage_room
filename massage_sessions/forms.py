from django import forms

from massage_sessions.models import MassageSession


class MassageSessionForm(forms.ModelForm):
    class Meta:
        model = MassageSession
        fields = ('session_master', 'session_type', 'client_name', 'client_phone', 'session_comment')
        # fields = ('session_master', 'session_type', 'client_name', 'client_phone', 'session_date', 'session_comment')
        labels = {
            'session_master': 'Мастер',
            'session_type': 'Вид массажа',
            'client_name': 'Имя *',
            'client_phone': 'Номер телефона *',
            # 'session_date': 'Дата сеанса',
            'session_comment': 'Комментарий',
        }


class MassageSessionAdminForm(forms.ModelForm):
    class Meta:
        model = MassageSession
        fields = ('session_master', 'session_type', 'client_name', 'client_phone', 'session_date', 'session_comment')
        # labels = {'content': 'Отзыв', 'rating': 'Оценка'}
