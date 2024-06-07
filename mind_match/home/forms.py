from django import forms
from django.forms import Select

from .models import Profile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control text-primary shadow m-3 fs-1 fs-1'}),
            'first_name':forms.TextInput(attrs={'class': 'form-control text-primary shadow m-3 fs-1'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control text-primary shadow m-3 fs-1'}),
            'email' :forms.TextInput(attrs={'class': 'form-control text-primary shadow m-3 fs-1'}),
            'password' :forms.TextInput(attrs={'class': 'form-control text-primary shadow m-3 fs-1'}),
        }
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['desc','drink','kids','smoke']
        widgets = {
            'desc': forms.TextInput(attrs={'class': 'form-control text-primary shadow m-3 fs-1'}),
            'drink': forms.Select(attrs = {'class' : "form-select text-primary shadow m-3 fs-1"},choices=[
                ("", "Unknown"),
                (True, "Yes"),
                (False, "No"),] ),
            'kids': forms.Select(attrs = {'class' : "form-select text-primary shadow m-3 fs-1"},choices=[
                ("", "Unknown"),
                (True, "Yes"),
                (False, "No"),] ),
            'smoke': forms.Select(attrs = {'class' : "form-select text-primary shadow m-3 fs-1"},choices=[
                ("", "Unknown"),
                (True, "Yes"),
                (False, "No"),] )
}
