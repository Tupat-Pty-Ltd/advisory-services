from django import forms

from ..models import ServicePrograme


class ServiceProgrameForm(forms.ModelForm):

    class Meta:
        model = ServicePrograme
        fields = '__all__'