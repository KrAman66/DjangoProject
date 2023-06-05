from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm



class UserForm(forms.ModelForm):
    password = forms.CharField(label="Enter Password",widget=forms.PasswordInput)
    email = forms.EmailField(label="Enter email id",required=True,widget=forms.widgets.EmailInput(attrs={'placeholder':'Enter email'}))
    class Meta:
        model = User
        fields = ('username','password','email')


class UserProfileChange(UserChangeForm): #inheriting
    email = forms.EmailField(label="Enter email id",required=True,widget=forms.widgets.EmailInput(attrs={'placeholder':'Enter email'}))
    username = forms.CharField(disabled=True)
    password = None
    class Meta:
        model = User
        fields = ('username','email','password') # attribute from the auth_user table inside dbsqlite
