from django import forms
from django.contrib.auth.forms import UserCreationForm
from delight.models import User,Category,cakes,cakevarients,offers

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2","address","phone"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


class CategorycreateForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=["name"]

class CakeAddForm(forms.ModelForm):
    class Meta:
        model=cakes
        fields="__all__"  

class CakeVarientForm(forms.ModelForm):
    class Meta:
        model=cakevarients
        exclude=("cake",)            

class OfferAddForm(forms.ModelForm):
    class Meta:
        model=offers
        exclude=("cakevarient",)  
        widgets={
            "start_date":forms.DateInput(attrs={"type":"date"}),
            "due_date":forms.DateInput(attrs={"type":"date"})
        }

    



           

        