from django import forms
from .models import Score

class ScoreForm(forms.ModelForm):

    class Meta:
        model = Score
        fields = '__all__'
        exclude = ['user', 'student', 'eval_item']