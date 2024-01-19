from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Clipboard

from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_future_date(value):
    if value < timezone.now().date():
        raise ValidationError("The date cannot be in the past!")

class ClipboardForm(forms.ModelForm):
    field = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Clipboard
        fields = ['topic', 'description', 'field', 'expire_date']
        widgets = {
            'topic': forms.TextInput(attrs={'class': 'form-control'}), # use a text input with a class attribute
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), # use a text area with a class and rows attribute
            
            'expire_date': forms.SelectDateWidget(), # use a select date widget
        }
        labels = {
            'topic': 'Title', # change the label of the topic field to Title
            'field': 'Content', # change the label of the field field to Content
        }
        validators = {
            'expire_date': [validate_future_date], # add a validator to check if the expire date is in the future
        }
