from django.forms import ModelForm
from .models import Person


class EditForm(ModelForm):
    class Meta:
        model = Person
