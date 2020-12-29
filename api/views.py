from rest_framework import generics
from .models import CoronaVirus
from .serializers import CoronaVirusModelSerializer

class CoronaVirusListAPIView(generics.ListAPIView):
    
    queryset         = CoronaVirus.objects.all()
    queryset         = queryset.extra(select={
        'total_cases': 'CAST(REPLACE(total_cases, ",","") AS INT)',
        'total_deaths': 'CAST(REPLACE(total_deaths, ",","") AS INT)',
        'total_recovered': 'CAST(REPLACE(total_recovered, ",","") AS INT)',})
    
    serializer_class = CoronaVirusModelSerializer
    search_fields    = ['country', 'continent']
    ordering_fields  = ['total_cases', 'total_deaths', 'total_recovered']
class CoronaVirusDetailAPIView(generics.RetrieveAPIView):
    
    queryset = CoronaVirus.objects.all()
    serializer_class = CoronaVirusModelSerializer
    lookup_field = 'slug'

    



