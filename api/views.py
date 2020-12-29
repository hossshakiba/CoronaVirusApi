from rest_framework import generics
from .models import CoronaVirus
from .serializers import CoronaVirusModelSerializer


class CoronaVirusListAPIView(generics.ListAPIView):
    
    queryset         = CoronaVirus.objects.all()
    serializer_class = CoronaVirusModelSerializer
    search_fields    = ['country', 'continent']
    ordering_fields  = ['total_cases',]

class CoronaVirusDetailAPIView(generics.RetrieveAPIView):
    
    queryset = CoronaVirus.objects.all()
    serializer_class = CoronaVirusModelSerializer
    lookup_field = 'slug'

    



