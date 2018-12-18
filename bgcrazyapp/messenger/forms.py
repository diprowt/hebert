"""messenger forms."""

# Django
from django import forms

# Models
from messenger.models import Message , Thread





# class MesageForm(forms.ModelForm):
#     content = forms.CharField(label="", widget=forms.Textarea(attrs={'class':'', 'placeholder':'escribe un mensaje'}))
#     class Meta:
#         model = Thread 
#         fields = ('users','messages')