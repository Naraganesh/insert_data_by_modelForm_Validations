from typing import Any
from django import forms

def validation_for_a(data):
    if data.lower().startswith('a') :
        raise forms.ValidationError('starts with a') 
def validation_forl_len(data):
    if len(data)<5:
        raise forms.ValidationError('len is < 5')

                               

class SchoolForm(forms.Form): 
    Sname=forms.CharField(validators=[validation_for_a])
    Sprincipal=forms.CharField(validators=[validation_forl_len])
    Slocation=forms.CharField()  
    email=forms.EmailField()
    reenteremail=forms.EmailField()

    def clean(self): 
        e=self.cleaned_data['email']
        re=self.cleaned_data['reenteremail'] 

        if e!=re:
            raise forms.ValidationError('emails are not matching')