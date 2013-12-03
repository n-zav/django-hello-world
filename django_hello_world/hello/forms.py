from django.forms import ModelForm, IntegerField, HiddenInput
from .models import Person
from .widgets import DatePickerInput


class EditForm(ModelForm):
    is_ajax_request = IntegerField(initial=0, widget=HiddenInput)

    class Meta:
        model = Person
        widgets = {
                'date_of_birth': DatePickerInput(format='%m/%d/%Y'),
                }
