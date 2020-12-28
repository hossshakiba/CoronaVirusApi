from django.urls import path
from .views import CoronaVirusListAPIView, CoronaVirusDetailAPIView

urlpatterns = [
    path('', CoronaVirusListAPIView.as_view()),
    path('<slug>', CoronaVirusDetailAPIView.as_view())
]
