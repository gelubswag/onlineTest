from django.forms import ModelForm, Textarea
from testApp import models

class SubjectForm(ModelForm):
    
    class Meta:
        model = models.Subject
        fields = ["name"]

class TestForm(ModelForm):
    
    class Meta:
        model = models.SubjTest
        fields = ["name","questions_num"]
        
class QuesttForm(ModelForm):
    
    class Meta:
        model = models.Question
        fields = ["image","text","optionsNum","weight"]
        widgets = {'vision': Textarea(attrs={'rows':6,
                                            'cols':22,
                                            'style':'resize:none',
                                            }),
        }

class OptForm(ModelForm):
    
    class Meta:
        model = models.Option
        fields = ["image","text","isRight"]