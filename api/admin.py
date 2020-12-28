from django.contrib import admin
from .models import CoronaVirus


class CoronaVirusAdmin(admin.ModelAdmin):
    
    list_display = ['country', 'total_cases', 'total_deaths', 'total_recovered']
    search_fields = ['country']
    ordering = ['-total_cases',]

admin.site.register(CoronaVirus, CoronaVirusAdmin)
