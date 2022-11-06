from django import forms
from .models import ConatactUs


class ConatactUsF(forms.ModelForm):
    class Meta:
        model = ConatactUs
        fields = '__all__'
