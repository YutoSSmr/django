from django import forms
 
class QuestionForm(forms.Form):
    questionNum = forms.CharField(initial=1)
    score = forms.CharField(initial=0)