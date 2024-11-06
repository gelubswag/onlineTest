from django.forms import ModelForm
from testApp import models

class SubjectForm(ModelForm):
    
    class Meta:
        model = models.Subject
        fields = ["name"]