from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
from django.conf import settings
import csv
import pandas as pd
# Create your views here.

def mpmDatatable(request):
        df = pd.read_csv("static/tmp/massbank_compound_canopus.tab.chemont.abbr.tab", delimiter = '\t')
        object = df.to_html()
        return HttpResponse(object)
