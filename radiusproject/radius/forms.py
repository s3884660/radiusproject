from django import forms


class SignUpForm(forms.Form):
    username = forms.CharField(help_text="Enter a Username")
    email = forms.EmailField(help_text="Enter Email")
    password = forms.CharField(help_text="Enter Password", widget=forms.PasswordInput)


