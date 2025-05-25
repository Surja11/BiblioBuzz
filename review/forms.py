from django import forms
from .models import *


class RegistrationForm(forms.ModelForm):
  
  password = forms.CharField(widget = forms.PasswordInput)
  confirm_password = forms.CharField(widget = forms.PasswordInput)
  class Meta:
    model = User
    fields = ["email","username","password","confirm_password"]

  def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data.get('password')
    confirm_password = cleaned_data.get('confirm_password')

    if password != confirm_password:
      self.add_error('confirm_password','Password and Confirm Password do not match')
      return cleaned_data
    
    def clean_email(self):
      email = self.cleaned_data.get('email')
      if User.objects.filter(email = email).exists():
        raise forms.ValidationError("A user with this email already exists")
      


class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ["image","bio","favorite_book"]

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['image'].widget.attrs.update({'class':'form-control-file'})






