from rest_framework import serializers
from .models import CoronaVirus
from django.utils.formats import number_format

class CoronaVirusModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoronaVirus
        fields = ['country', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths',
                
                'total_recovered', 'active_cases', 'total_tests', 'population', 'continent']
