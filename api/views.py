from django.shortcuts import render
from .models import CoronaVirus
from .utils import info

def corona_virus_update():
    objects = CoronaVirus.objects.all()
    for obj in objects:
        obj.country             = info[0]
        obj.total_cases         = info[1]
        obj.new_cases           = info[2]
        obj.country             = info[3]
        obj.total_deaths        = info[4]
        obj.new_deaths          = info[5]
        obj.total_recovered     = info[6]
        obj.active_cases        = info[7]
        obj.total_tests         = info[8]
        obj.population          = info[9]
        obj.continent           = info[10]
        obj.slug                = info[0].lower().replace(' ','-')
        obj.save()


