from django import forms


class CreateForm(forms.Form):
    title = forms.CharField(label='Title', max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(label='Text', widget=forms.Textarea(attrs={'class': 'form-control'}))
