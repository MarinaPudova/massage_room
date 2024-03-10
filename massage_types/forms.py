from django import forms

from massage_types.models import MassageType


class MassageTypeForm(forms.ModelForm):
    class Meta:
        model = MassageType
        fields = ('name', 'description', 'cost', 'massage_cover', 'current_status')
        labels = {
            'name': 'название',
            'description': 'описание',
            'cost': 'стоимость',
            'massage_cover': 'изображение',
            'current_status': 'доступность',
        }
