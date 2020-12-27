from rest_framework import serilizers
from .models import CoronaVirus

class CoronaVirusSerilizer(serilizers.ModelSerializer):
    class Meta:
        model = CoronaVirus
        fields = ['id', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths',
                
                'total_recovered', 'active_cases', 'total_tests', 'population', 'continent']
        