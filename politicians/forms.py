from django import forms
from .models import Review
from captcha.fields import CaptchaField
from django_starfield import Stars
from django.utils.safestring import mark_safe

class AddCommentForm(forms.ModelForm):
    CHOICES=[('1','1'),
         ('2','2'), ('3', '3'), ('4', '4'), ('5', '5')]
    # honesty_rate = forms.ChoiceField(label="პატიოსნება", choices=CHOICES, widget=forms.RadioSelect)
    honesty_rate = forms.IntegerField(label="პატიოსნება", widget=Stars)
    focus_rate = forms.IntegerField(label="ორიენტირებულობა", widget=Stars)
    ambition_rate = forms.IntegerField(label="ამბიციურობა", widget=Stars)
    respect_rate = forms.IntegerField(label="პატივისცემა", widget=Stars)
    persuasiveness_rate = forms.IntegerField(label="დამაჯერებლობა", widget=Stars)
    general_rate = forms.IntegerField(label=mark_safe('<br />საერთო შეფასება'), widget=Stars)
    captcha = CaptchaField(label=" ")
    class Meta:
        model = Review
        fields = ('comment', 'honesty_rate', 'focus_rate', 'ambition_rate', 'respect_rate', 'persuasiveness_rate', 'general_rate', 'captcha')
        labels = {
            'comment': 'კომენტარი',
        }
