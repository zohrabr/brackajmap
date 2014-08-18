from django.db import models
from geoposition.fields import GeopositionField


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

class crimetype(models.Model):
	
	name = models.CharField(max_length=128,choices=crime_choice,default='braquage')
	
	def __unicode__(self):
		return self.name

class crime(models.Model):
	pseudonyme = models.CharField(max_length=80,help_text="pseudonyme:")
	gouvernorat = models.CharField(max_length=30, choices=gouv_choice,default='Tunis',help_text="Gouvernorat")
	description = models.TextField(help_text="informations sur le crime ")
	time = models.DateTimeField(auto_now_add=False, auto_now=False, verbose_name="Date de crime",help_text="Date et Heure du crime ")
	position = GeopositionField()
	crimetype = models.ForeignKey(crimetype,help_text="Quel est le crime ?")
	cpt = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.pseudonyme


	

