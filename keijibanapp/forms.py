from django import forms
from .models import User,Keijiban
from django.contrib.auth.models import User

class KeijibanForm(forms.ModelForm) :
    class Meta :
        model = Keijiban
        fields = "__all__"

class CreateForm(forms.ModelForm):
    class Meta :
        model = Keijiban
        fields = ["toukou","created_at"]



class SignupForm(forms.ModelForm) :
    class Meta :
        model = User
        fields = ["username","password","email","age","sex","address","icon"]

class LoginForm(forms.ModelForm) :
    class Meta :
        model = User
        fields = ["username","password"]
