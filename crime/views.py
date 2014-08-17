from django.shortcuts import render_to_response
from django.template import RequestContext
from crime.forms import crimeForm
def acceuil(request):
	context=RequestContext(request)
	context_dict=  { 'hello':"Bienvenue sur notre site CrimeMap"}
	return render_to_response('crime/acceuil.html',context_dict)

def add_crime(request):
	context = RequestContext(request)
	if request.method == 'Post' :
		form =crimeForm(request.Post)
		if form.is_valid():
			form.save(commit=True)
			return thanks(request)
		else: 
			print form.errors
	else:
		form=crimeForm()
	return render_to_response('crime/add_crime.html',{'form':form},context)
def thanks(request):
	context=RequestContext(request)
	cont_dict={ 'thx' : "merci pour votre participation pour une meilleur tunisie" }
	return render_to_response('crime/thanks.html',cont_dict)
