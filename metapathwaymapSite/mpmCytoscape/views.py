from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def mpmCytoscape(request):

    return render(request, 'mpmCytoscape/cytoscape.html')
