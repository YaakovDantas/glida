from django import forms
from django.contrib.auth.models import User

class GerenteForm(forms.Form):
    
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


