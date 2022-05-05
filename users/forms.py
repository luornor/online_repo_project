from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UploadModel





class UserModelForm(UserCreationForm):
    # def __init__(self, *args, **kwargs): 
    #     super().__init__(*args, **kwargs) 
    #     self.fields['username'].widget.attrs.update({ 
    #         'class': 'form-input', 
    #         'required':'', 
    #         'name':'username', 
    #         'id':'username', 
    #         'type':'text', 
    #         'placeholder':'John Doe', 
    #         'maxlength': '16', 
    #         'minlength': '6', 
    #         }) 
    #     self.fields['email'].widget.attrs.update({ 
    #         'class': 'form-input', 
    #         'required':'', 
    #         'name':'email', 
    #         'id':'email', 
    #         'type':'email', 
    #         'placeholder':'JohnDoe@mail.com', 
    #         }) 
    #     self.fields['password1'].widget.attrs.update({ 
    #         'class': 'form-input', 
    #         'required':'', 
    #         'name':'password1', 
    #         'id':'password1', 
    #         'type':'password', 
    #         'placeholder':'password', 
    #         'maxlength':'22',  
    #         'minlength':'8' 
    #         }) 
    #     self.fields['password2'].widget.attrs.update({ 
    #         'class': 'form-input', 
    #         'required':'', 
    #         'name':'password2', 
    #         'id':'password2', 
    #         'type':'password', 
    #         'placeholder':'password', 
    #         'maxlength':'22',  
    #         'minlength':'8' 
    #         }) 


    class Meta:
        model = User
        fields = ['username','email','password1', 'password2',]
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}) ,
            'password2':forms.PasswordInput(attrs={'class':'form-control'}),
        }
        
class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadModel
        fields = '__all__'


		