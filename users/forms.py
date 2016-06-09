from django import forms

class UsersForm(form.Form):
    user_name = forms.CharField(label='Your Name', max_length=100)
    password = forms.CharField(label='password', max_length=100)

