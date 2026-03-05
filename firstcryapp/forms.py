from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, categories
from .models import CroppedImage
import re


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','mobile']



class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = CroppedImage
        fields = ('file',)
class RegistrationForm(forms.Form):
    firstname = forms.CharField(min_length=2,max_length=50)
    lastname = forms.CharField(min_length=2,max_length=50)
    phonenumber = forms.CharField(max_length=10)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget = forms.PasswordInput)
    def clean_firstname(self):
        name = self.cleaned_data['firstname']
        if not name.isalpha():
            raise forms.ValidationError('Allows only Characters')
        if len(set(name)) == 1:
            raise forms.ValidationError("Repeated Characters are not allowed")
        return name
    def clean_lastname(self):
        name = self.cleaned_data['lastname']
        if not name.isalpha():
            raise forms.ValidationError("Only characters are allowed")
        if len(set(name)) == 1:
            raise forms.ValidationError("Repeated characters are not allowed")
        return name
    def clean_phone(self):
        phone = self.cleaned_data['phonenumber']
        if not phone.isdigit():
            raise forms.ValidationError("Must be Numbers")
        if len(set(phone)) == 1:
            raise forms.ValidationError("Invalid Number")
        if len(phone) != 10:
            raise forms.ValidationError("Must be 10 digits ")
        return phone
    def clean(self):
        cleaned_data = super().clean()

        p1 = cleaned_data.get("password1")
        p2 = cleaned_data.get("password2")

        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Passwords do not match")


class UserUpdationForm(forms.Form):
    firstname = forms.CharField(min_length=2,max_length=50)
    lastname = forms.CharField(min_length=2,max_length=50)
    mobile = forms.CharField(max_length=10)
    def clean_firstname(self):
        name = self.cleaned_data['firstname']
        if not name.isalpha():
            raise forms.ValidationError(' Allows only Characters')
        if len(set(name)) == 1:
            raise forms.ValidationError("Invalid")
        return name
    def clean_lastname(self):
        name = self.cleaned_data['lastname']
        if not name.isalpha():
            raise forms.ValidationError("Allows only Characters")
        if len(set(name)) == 1:
            raise forms.ValidationError("Invalid")
        return name
    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if not mobile.isdigit():
            raise forms.ValidationError("Must be Numbers")
        if len(set(mobile)) == 1:
            raise forms.ValidationError("Invalid Mobile Number")
        if len(mobile) != 10:
            raise forms.ValidationError("Must be 10 digits ")
        return mobile




class CategoryForm(forms.ModelForm):

    class Meta:
        model = categories
        fields = ['titile', 'type', 'description', 'gender', 'image']

        widgets = {
            'titile': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),
        }