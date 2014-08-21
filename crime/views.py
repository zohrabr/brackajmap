from django.shortcuts import render_to_response, HttpResponse
from django.template import RequestContext
from crime.forms import crimeForm
from crime.models import crime
import json
def acceuil(request):
	context =  RequestContext(request)
	context_dict=  { 'hello':"Page d'acceuil de CriMap"}
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
def statistique(request):
	context =  RequestContext(request)
	return render_to_response('crime/statistique.html',{})	

def delete(request):
	if 'id' not in request.GET: 
		return HttpResponse("fail")
	the_id = request.GET['id']
	
	try:	
		obj=crime.objects.get(id=the_id)
		obj.delete()
		return 	HttpResponse("success ")
	except:
		return  HttpResponse("fail")
def modify(request):
	if 'id' not in request.GET: 
		return HttpResponse("fail")
	the_id=request.GET['id']
	if request.method == 'GET' :	
		try:
			obj=crime.objects.get(id=the_id)
			gouv = obj.gouvernorat
			desc= obj.description
			sx= obj.sexe
			temp=str(obj.time)
			cat=obj.crimetype
			pos=str(obj.position)
			dictionnaire={ 'gouv': gouv ,'temp':temp, 'desc':desc ,'pos' : pos, 'sx' : sx ,  'cat':cat }
	  
			return HttpResponse(json.dumps(dictionnaire))
		except:
			return HttpResponse("fail")
	elif request.method == 'POST':
		try :
			obj=crime.objects.get(id=the_id)
		except:
			return HttpResponse("fail")
		if "gouvernorat" in request.POST:
			obj.gouvernorat= request.POST["gouvernorat"]
		if "description" in request.POST:
			obj.description= request.POST["description"] 
		if "sexe" in request.POST:
			obj.sexe= request.POST["sexe"]
		if "crimetype" in request.POST:
			obj.crimetype= request.POST["crimetype"]
		if "position" in request.POST:
			obj.position= request.POST["position"]
		if "time" in request.POST:
			obj.time=request.POST["time"]
		return HttpResponse("succes post")
	else :
		return HttpResponse("fail post")		
		
def filtercrime(request):
	if request.method == "POST":
		sex = request.POST["sexe"]
		gouv = request.POST["gouvernorat"]
		cat = request.POST["crimetype"]
		
		q = Q()
		if sex :
			q= q & Q(sexe=sex)
		if gouv :
			q= q & Q(gouvernorat=gouv)
		if cat:
			q= q & Q(crimetype=cat)
		crimes=crime.objects.filter(q)
		l=[]
		for c in crimes:
			mot= str(c.time)
			m=mot[:18]
			l.append(m)
		crimes=list(crimes.values_list("gouvernorat","position","crimetype"))
                i= -1
		lis = []
		for c in crimes:
			i += 1
			a=list(c)
			a.append(l[i])
			x=tuple(a)
			lis.append(x)

		return HttpResponse(json.dumps(lis), content_type="application/json")
	else:
		return HttpResponse()




def fct(obj):
	temp =obj.date()






