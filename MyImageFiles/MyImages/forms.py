from django import forms

class MyImageForm(forms.Form):    
    file=forms.FileField(widget=forms.FileInput(attrs={'class':'form-control','multiple':True}))
    