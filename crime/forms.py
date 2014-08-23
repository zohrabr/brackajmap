from django import forms
from crime.models import  crime

sexchoice=(
	('H','Homme'),
	('F','Femme'),
)

class crimeForm(forms.ModelForm):
	
	cpt=forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	sexe=forms.ChoiceField(widget=forms.RadioSelect,choices=sexchoice,help_text='sexe:')
	class Meta:
		model = crime
	

