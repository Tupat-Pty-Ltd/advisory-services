from django import forms

from ..models import BioData


class BioDataForm(forms.ModelForm):

    class Meta:
        model = BioData
        fields = '__all__'
