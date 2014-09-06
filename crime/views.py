from __future__ import division
from django.shortcuts import HttpResponse, render
from django.template import RequestContext
from django.db.models.query import Q
from crime.forms import crimeForm
from crime.models import crime
from geoposition import Geoposition
import json
from django.core.serializers.json import DjangoJSONEncoder
from calendar import timegm


def acceuil(request):
    context_dict = {'hello': "Introduction"}
    return render(request, 'crime/acceuil.html', context_dict)


def thanks(request):
    context_dict = {'thx': "merci pour votre participation pour une meilleur tunisie"}
    return render(request, 'crime/thanks.html', context_dict)


def add_crime(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = crimeForm(request.POST)
        var = request.POST['crimetype']

        if form.is_valid():
            form.save(commit=True)
            return thanks(request)
        else:
            print form.errors
    else:

        form = crimeForm()

    return render(request, 'crime/add_crime.html', locals())


def statistique(request):
    return render(request, 'crime/statistique.html', locals())


def delete(request):
    if 'id' not in request.GET:
        return HttpResponse("fail")
    the_id = int(request.GET['id'])
    try:
        obj = crime.objects.get(id=the_id)
        obj.delete()
        return HttpResponse("success ")
    except crime.DoesNotExist:
        return HttpResponse("fail")


def modify(request):
    if request.method == 'GET':
        if 'lat' and 'lng' not in request.GET:
            return HttpResponse("fail")
        lat = request.GET['lat']
        lng = request.GET['lng']
        try:
            p = Geoposition(lat, lng)
            obj = crime.objects.get(position=p)
            gouv = obj.gouvernorat
            desc = obj.description
            sx = obj.sexe
            temp = str(obj.time)
            cat = obj.crimetype
            pos = str(obj.position)
            dictionnaire = {'gouv': gouv,
                            'temp': temp,
                            'desc': desc,
                            'pos': pos,
                            'sx': sx,
                            'cat': cat}

            return HttpResponse(json.dumps(dictionnaire),
                                content_type='application/json')
        except crime.DoesNotExist:
            return HttpResponse("fail")
    elif request.method == 'POST':
        if 'id' not in request.GET:
            return HttpResponse("fail")
        the_id = request.GET['id']
        try:
            obj = crime.objects.get(id=the_id)
        except crime.DoesNotExist:
            return HttpResponse("fail")
        if "gouvernorat" in request.POST:
            obj.gouvernorat = request.POST["gouvernorat"]
        if "description" in request.POST:
            obj.description = request.POST["description"]
        if "sexe" in request.POST:
            obj.sexe = request.POST["sexe"]
        if "crimetype" in request.POST:
            obj.crimetype = request.POST["crimetype"]
        if "position" in request.POST:
            obj.position = request.POST["position"]
        if "time" in request.POST:
            obj.time = request.POST["time"]
        return HttpResponse("succes post")
    else:
        return HttpResponse("fail post")


def filtercrime(request):
    if request.method == "GET":
        sex, gouv, cat = None, None, None
        if "sex" in request.GET:
            sex = request.GET["sexe"]
        if "gouvernorat" in request.GET:
            gouv = request.GET["gouvernorat"]
        if "crimetype" in request.GET:
            cat = request.GET["crimetype"]
        q = Q()
        if sex:
            q = q & Q(sexe=sex)
        if gouv:
            q = q & Q(gouvernorat=gouv)
        if cat:
            q = q & Q(crimetype=cat)
        crimes = crime.objects.filter(q)

        crimes = list(crimes.values_list("gouvernorat", "position", "crimetype", "time"))
        return HttpResponse(json.dumps(crimes, cls=DjangoJSONEncoder), content_type="application/json")
    else:
        return HttpResponse()


def stat(request):
    if request.method == 'GET':
        nbr = crime.objects.count()
        if 'type' in request.GET:
            type_dict = {'braquage': 0,
                         'harcelement sexuelle': 0,
                         'viole': 0,
                         'vol': 0,
                         'agression': 0,
                         'assassinat': 0,
                         'kidnap': 0}
            for i in type_dict:
                type_dict[i] = (crime.objects.filter(Q(crimetype=i)).count() / nbr) * 100
            res = [list(l) for l in type_dict.items()]
            return HttpResponse(json.dumps(res), content_type="application/json")
        elif 'sexe' in request.GET:
            sex_dict = {"Femme": 0, "Homme": 0}
            for s in sex_dict:
                sex_dict[s] = (crime.objects.filter(Q(sexe=s)).count() / nbr) * 100
            res = [list(l) for l in sex_dict.items()]
            return HttpResponse(json.dumps(res), content_type="application/json")
        else:
            return HttpResponse()
    else:
        return HttpResponse()


def calendar_data(request):
    crimes = crime.objects.all().values_list("time", flat=True)
    crimes_stamp = [timegm(i.timetuple()) for i in crimes]
    res = dict(zip([str(i) for i in crimes_stamp], [1 for i in range(len(crimes_stamp))]))
    return HttpResponse(json.dumps(res), content_type="application/json")


def test(request):
    return render(request, 'crime/calendar.html', locals())


def mod_crime(request):
    pass