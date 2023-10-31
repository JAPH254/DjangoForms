from django import forms


class StudentForms(forms.Form):
    fname = forms.CharField(label="Your first Name", max_length=30)
    lname = forms.CharField(label="Your last Name", max_length=30)
    eml = forms.EmailField(label="Enter you email", max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
