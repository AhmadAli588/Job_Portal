from django import forms
from django.forms import ModelForm
from .models import Resume
class ResumeForm(ModelForm):
    class Meta:
        model=Resume
        fields=[
            'full_name',
            'email',
            'message',
            'file'
        ]
        widgets = {
            "full_name": forms.TextInput(attrs={'required': "required"}),
            "email": forms.EmailInput(attrs={'required': "required"}),
            "message": forms.Textarea(attrs={'required': "required"}),
            "file": forms.FileInput(attrs={'required': "required"}),
            }
#class ResumeForm(forms.Form):
 #   full_name=forms.CharField()
  #  email=forms.EmailField()
   # message=forms.CharField(widget=forms.Textarea)

