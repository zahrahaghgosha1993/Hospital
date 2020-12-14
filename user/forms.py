from django.forms import ModelForm
from .models import Patient


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['name','last_name',"phone",'disease','address']
