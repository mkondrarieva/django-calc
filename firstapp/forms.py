from django import forms
 
class UserForm(forms.Form):
   
     num1 = forms.CharField()
     denum1 = forms.CharField()
     num2= forms.CharField()
     denum2 = forms.CharField()
#    age = forms.IntegerField()
