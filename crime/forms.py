from django import forms
from crime.models import crimetype, crime
gouv_choice=(
	('Ariana','Ariana'), 
	('Beja','Beja'), 
	('Ben Arous', 'Ben Arous'),
	('Bizerte', 'Bizerte'),
	('Gabes','Gabes'),
	('Gafsa','Gafsa'),
	('Jendouba','Jendouba'),
	('Kairouan','Kairouan'),
	('Kasserine','Kasserine'),
	('Kebili','Kebili'),
	('Kef' ,'Kef'),
	('Mahdia' ,'Mahdia'),
	('Manouba','Manouba'), 
	('Medenine','Medenine'),
	('Monastir','Monastir'),
 	('Nabeul','Nabeul'),
 	('Sfax','Sfax'),
	('Sidi Bouzid','Sidi Bouzid'),
	('Siliana' ,'Siliana'),
	('Sousse' ,'Sousse'),
	('Tataouine','Tataouine'),  
	('Tozeur' ,'Tozeur'),
 	('Tunis' ,'Tunis'),
 	('Zaghouan','Zaghouan'),
)
crime_choice=(
	('braquage','braquage'),
	('harcelement sexuelle','harcelement sexuelle'),
	('viole','viole'),
	('vol','vol'),
)
class crimeForm(forms.ModelForm):
	gouvernorat=forms.ChoiceField(label="Selection", choices=gouv_choice)	
	crimetype=forms.ChoiceField(label="selection", choices=crime_choice)
	time=forms.DateField()
	description=forms.CharField(widget=forms.Textarea)
	cpt=forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	
	class Meta:
		model= crime
		fields=('time','description','gouvernorat','cpt')


