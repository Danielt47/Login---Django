from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": 'user name / email', 'class':'login_input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": 'Password', 'class':'login_input'}))