from celery import Celery
from .models import CoronaVirus
import requests
from bs4 import BeautifulSoup
import sys

app = Celery()

sys.dont_write_bytecode = True

info = []
indices = [2,3,4,5,6,7,9,13,15,16]
url = f"https://www.worldometers.info/coronavirus"

@app.task(name='data') 
def get_statistics():

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    data = soup.find('tbody').find_all('tr')

    for d in data:
        d = d.text.split('\n')
        d = list(map(lambda x:'not available' if x==' ' or x=='' else x, d))
        d = [d[i] for i in indices]
        info.append(d)
    
    return info[7:]

@app.task(name='update')
def corona_virus_update():
    
    objects = CoronaVirus.objects.all()
    info = get_statistics()
    if objects.count() == 0:
        for i in range(len(info)):
            CoronaVirus.objects.create(
                                country         = info[i][0],
                                total_cases     = info[i][1],
                                new_cases       = info[i][2],
                                total_deaths    = info[i][3],
                                new_deaths      = info[i][4],
                                total_recovered = info[i][5],
                                active_cases    = info[i][6],
                                total_tests     = info[i][7],
                                population      = info[i][8],
                                continent       = info[i][9],
                                slug            = info[i][0].lower().replace(' ','-'))
    else:
        for i, obj in enumerate(objects):
            obj.country             = info[i][0]
            obj.total_cases         = info[i][1]
            obj.new_cases           = info[i][2]
            obj.total_deaths        = info[i][3]
            obj.new_deaths          = info[i][4]
            obj.total_recovered     = info[i][5]
            obj.active_cases        = info[i][6]
            obj.total_tests         = info[i][7]
            obj.population          = info[i][8]
            obj.continent           = info[i][9]
            obj.slug                = info[i][0].lower().replace(' ','-')
            obj.save()
