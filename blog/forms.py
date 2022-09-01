
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'type': "text",
        'class': "name-input",
        'placeholder': "Name",
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        'type': "text",
        'class': "email-input",
        'placeholder': "Email",
    }))

    subject = forms.CharField(widget=forms.TextInput(attrs={
        'type': "text",
        'class': "subject-input",
        'placeholder': "Subject",
    }))

    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': "6",
        'class': "message-input",
        'placeholder': "Message",

    }))