from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views
#  here.
class ParticipantViewSet(viewsets.ModelViewSet):
    query= Participant.objects.all()
    serializer_class=ParticipantSerializer


