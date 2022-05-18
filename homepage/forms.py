from dataclasses import fields
from django import forms
from .models import Urun

class FormUrun(forms.ModelForm):
   class Meta:
      model = Urun
      fields = ('author','content','img','tl','alici')
      