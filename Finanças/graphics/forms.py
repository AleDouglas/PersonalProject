from django import forms
from .models import Gain, Lose


class GainForms(forms.ModelForm):

    class Meta:
        model = Gain
        fields = ['usuario','valor', 'data']
        exclude = ('usuario',)

class LoseForms(forms.ModelForm):

    class Meta:
        model = Lose
        fields = ['usuario','valor', 'data']
        exclude = ('usuario',)