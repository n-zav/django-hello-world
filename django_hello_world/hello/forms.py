from django.forms import ModelForm
from .models import Person
from .widgets import DatePickerInput


class EditForm(ModelForm):
    class Meta:
        model = Person
        widgets = {
                'date_of_birth': DatePickerInput(),
                }
