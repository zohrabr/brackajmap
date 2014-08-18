from django.shortcuts import render_to_response
from django.template import RequestContext
from crime.forms import crimeForm
def acceuil(request):
	context =  RequestContext(request)
	context_dict=  { 'hello':"Bienvenue sur notre site CrimeMap"}
	return render_to_response('crime/acceuil.html',context_dict)
def thanks(request):
	context = RequestContext(request)
	context_dict={ 'thx' : "merci pour votre participation pour une meilleur tunisie" }
	return render_to_response('crime/thanks.html',context_dict)
def add_crime(request):
	context = RequestContext(request)
	if request.method == 'POST' :
		form =crimeForm(request.POST)
		var=request.POST['crimetype']
		
		if form.is_valid():
			form.save(commit=True)
			
			return thanks(request)
		else: 
			print form.errors
	else:
		
		form = crimeForm()
	
	return render_to_response('crime/add_crime.html',{'form':form},context)


