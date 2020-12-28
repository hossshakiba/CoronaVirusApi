from rest_framework import generics
from .models import CoronaVirus
from .serializers import CoronaVirusModelSerializer


class CoronaVirusListAPIView(generics.ListAPIView):
    
    queryset = CoronaVirus.objects.all()
    serializer_class = CoronaVirusModelSerializer

class CoronaVirusDetailAPIView(generics.RetrieveAPIView):
    
    queryset = CoronaVirus.objects.all()
    serializer_class = CoronaVirusModelSerializer
    lookup_field = 'slug'

    



