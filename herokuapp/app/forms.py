from django import forms


class CreateForm(forms.Form):
    title = forms.CharField(label='Title', max_length=300)
    text = forms.CharField(widget=forms.Textarea)
