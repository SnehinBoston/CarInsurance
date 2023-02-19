import re
import string
from .models import CarInsurance
from django import forms

def make_validation(value):
    if any(p in value for p in string.punctuation):
        return True
    return False

def model_validation(value):
    if any(p in value for p in string.punctuation):
        return True
    return False

def year_validation(value):
    if value < 2000 or value > 2023:
        return True
    return False

def mileage_validation(value):
    if re.match(".*[a-z]+.*", value) or re.match(".*[A-Z]+.*", value):
        return True
    return False



class CarInsuranceForm(forms.Form):
    make = forms.CharField(max_length=100, label="Make", widget=forms.TextInput(attrs={'class':"input"}), required=True)
    model = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':"input"}), required=True)
    year = forms.IntegerField(widget= forms.DateInput(format="%Y"), required=True)
    mileage = forms.CharField(max_length=30,label="Mileage", widget=forms.TextInput(attrs={'class':"input"}), required=True)

    # error_messages = []
    def clean_make(self):
        make_data = self.cleaned_data.get('make')
        if make_validation(make_data):
            self.add_error('make', "Please enter only alphabets in Make field.")
            # raise forms.ValidationError("You cannot enter a number or punctuation in make field.")
        return make_data        
    
    def clean_model(self):
        model_data = self.cleaned_data['model']
        if model_validation(model_data):
            self.add_error('model', "Please enter only alphabets in Model field.")
            # raise forms.ValidationError("You cannot enter punctuations in model field.")
        return model_data
    
    def clean_year(self):
        year_data = self.cleaned_data['year']
        if year_validation(year_data):
            self.add_error('year', "Please enter years between 2000 and 2023.")
        return year_data

    def clean_mileage(self):
        mileage_data = self.cleaned_data['mileage']
        if mileage_validation(mileage_data):
            self.add_error('mileage', "Please enter only numbers in Mileage field.")
        return mileage_data 


            