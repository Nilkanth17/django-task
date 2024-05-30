from django import forms

from .models import Online

class Onlineform (forms.ModelForm):
    
    class meta:
        
        model = Online

        AA = [
            "category",
            "description",
        ]