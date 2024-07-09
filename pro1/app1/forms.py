from django import forms
from .models import Bank
from django.core import validators
from datetime import date

gen = [('male', 'Male'),
       ('female', 'Female')]
class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = '__all__'


        labels = {
            'bid' : 'Customer ID',
            'name' : 'Customer Name',
            'email' : 'E-mail',
            'mob' : 'Mobile Number',
            'adhar' : 'Aadhar Number',
            'pan' : 'Pan Card Number',
            'accno' : 'Account Number',
            'ifsc' : 'IFSC Code',
            'gender' : 'Gender',
            'dob' : 'Birth Date',
            'profile_pic' : 'Profile Picture'
        }

        widgets = {
            'bid': forms.NumberInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'mob': forms.TextInput(attrs={'class':'form-control'}),
            'adhar': forms.TextInput(attrs={'class':'form-control'}),
            'pan': forms.TextInput(attrs={'class':'form-control'}),
            'accno': forms.TextInput(attrs={'class':'form-control'}),
            'ifsc': forms.TextInput(attrs={'class':'form-control'}),
            'gender': forms.RadioSelect(choices=gen),
            'dob': forms.DateInput(attrs={'type':'date', 'class': 'form-control'}),
            'profile_pic': forms.ClearableFileInput(attrs={'class':'form-control'})
        }

    def clean_dob(self):
        d = self.cleaned_data.get('dob')
        if d>date.today():
            raise validators.ValidationError('Date cannot be later than today.....')
        return d

