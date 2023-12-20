from django import forms
class UrubuPixForm(forms.Form):
    matricula = forms.CharField(label="matricula", max_length=100)