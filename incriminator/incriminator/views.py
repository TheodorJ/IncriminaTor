from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import IndexForm

from .exonerator import ipDateIsTorNode
from .apility import ipIsInBlacklist, ipGeoLocation

def render_index(request):
    if(request.method == "GET"):
        index_form = IndexForm()

        return render(request, "index.html", {'index_form': index_form})

    elif(request.method == "POST"):
        index_form = IndexForm(request.POST)

        if(index_form.is_valid()):

            ip = index_form.cleaned_data['ip']
            date = index_form.cleaned_data['date']

            return HttpResponseRedirect("/" + ip + "/" + str(date) + "/")

def render_results(request, ip, date):

    isTorNode = ipDateIsTorNode(ip, date)

    apilityBlacklist = ipIsInBlacklist(ip)
    if(not apilityBlacklist[0]): apilityBlacklist = None
    apilityGeoInfo = ipGeoLocation(ip)
    if(apilityGeoInfo):
        agi_country = apilityGeoInfo["country"]
        agi_continent = apilityGeoInfo["continent"]
        agi_latitude = apilityGeoInfo["latitude"]
        agi_longitude = apilityGeoInfo["longitude"]
    else:
        agi_country = None
        agi_continent = None
        agi_latitude = None
        agi_longitude = None

    if(apilityBlacklist == None):
        inter = None
    else:
        inter = apilityBlacklist[1]

    context = {'isTorNode': isTorNode,
               'apilityBlacklist': inter,
               'apilityGeoInfo': apilityGeoInfo,
               'agi_country': agi_country,
               'agi_continent': agi_continent,
               'agi_latitude': agi_latitude,
               'agi_longitude': agi_longitude}

    return render(request, "results.html", context)
