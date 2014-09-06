from django.conf.urls import patterns, url
from crime import views

urlpatterns = patterns('crime.views',
                       url(r'^acceuil/$', 'acceuil', name='acceuil'),
                       url(r'^new_crime/$', 'add_crime', name='add_crime'),
                       url(r'^thanks/$', 'thanks', name='thanks'),
                       url(r'^statistique/$', 'statistique', name='statistique'),
                       url(r'^supprimer/$', 'delete', name='supprimer'),
                       url(r'^modifier/$', 'modify', name='modifier'),
                       url(r'^statistique/filter/$', 'filtercrime', name='filter'),
                       url(r'stat/', 'stat', name='stat'),
                       url(r'cdata/', 'calendar_data'),
                       url(r'test/', 'test'),
)
