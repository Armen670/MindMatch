from django import forms
from django.contrib.auth.forms import AuthenticationForm,UsernameField
from django.forms import Select
from django.utils.translation import gettext_lazy as _

from .models import Profile,Image
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

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control text-primary shadow m-3 fs-1 fs-1'}),
            'first_name':forms.TextInput(attrs={'class': 'form-control text-primary shadow m-3 fs-1'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control text-primary shadow m-3 fs-1'}),
            'email' :forms.TextInput(attrs={'class': 'form-control text-primary shadow m-3 fs-1'}),
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
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image']
        widgets = {
            'desc': forms.TextInput(attrs={'class': 'form-control text-primary shadow m-3 fs-1'})
        }

class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(label="Username",widget=forms.TextInput(attrs={"autofocus": True ,
                                                           'class': 'form-control text-primary shadow  fs-1'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password" ,
                                          'class': 'form-control text-primary shadow  fs-1'}))

    """def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)"""
        #print(type(self.fields["username"].label_tag))
        #print(self.fields["username"].label_tag)

        #print(dir(self.fields["username"]))
    """def as_p(self):
        "Returns this form rendered as HTML <p>s."
        return self._html_output(
            normal_row='<p%(html_class_attr)s><label class="custom-label-class" for="%(id)s">%(label)s</label> %(field)s%(help_text)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=False)"""