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

    # session_master = models.ForeignKey(MassageMaster, on_delete=models.DO_NOTHING, blank=True, null=True)
        # session_type = models.ForeignKey(MassageType, on_delete=models.DO_NOTHING, blank=True, null=True)
        # # session_client = models.ForeignKey(Client,  on_delete=models.DO_NOTHING, blank=True)
        # client_name = models.CharField(max_length=20)
        # client_phone = models.CharField()
        # session_date = models.DateTimeField(blank=True, null=True)
        # # TODO 4 варианта выбора, в обработке, прошел, назначен, отмена
        # session_status = models.CharField(default="processing")
        # session_comment = models.TextField(max_length=200, blank=True, null=True)
