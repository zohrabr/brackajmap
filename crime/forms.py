from django import forms
from crime.models import crime

sexchoice = (
    ('H', 'Homme'),
    ('F', 'Femme'),
)


class crimeForm(forms.ModelForm):
    sexe = forms.ChoiceField(widget=forms.RadioSelect, choices=sexchoice, help_text='sexe:')

    class Meta:
        model = crime
