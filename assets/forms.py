from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=254, required=True)
    email = forms.EmailField(required=True)
    movie_name = forms.CharField(widget=forms.Textarea)
