from django import forms


class InputDataForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
