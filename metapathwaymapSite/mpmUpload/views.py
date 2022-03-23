# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .forms import mpmUploadForm

import os
import subprocess
import sys

def mpmUpload(request):

    if request.method == 'POST':
        form = mpmUploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            for filename, file in request.FILES.items():
                name = request.FILES[filename].name
                path = 'static/tmp/' + name
                path2 = 'tmp/' + name
                path3 = 'tmp/' + name + ".chemont.top"
                path4 = 'tmp/' + name + ".chemont.top.format"
                path5 = 'tmp/' + name + ".chemont.top.format.abbr.tab"
                path6 = 'tmp/' + name + ".chemont.top.sort"

                context = {
                    "output": path2,
                    "input" : path2,
                    "chemont_top" : path3,
                    "chemont_top_format" : path4,
                    "chemont_top_format_abbr_tab" : path5,
                    "chemont_top_sort" : path6,
                }

            organism = form.cleaned_data['organism']

            if organism == 'PlantCyc':
                #output = subprocess.check_output(['python', 'metaPathwayMap/scripts/get_similar_pathways_wrapper.py', '-cmp', 'static/databases/compounds.dat', '-pwy', 'static/databases/pathways.dat', '-chemont', 'static/databases/ChemOnt_2_1.obo.mod.tax.organic', '-chebi', 'static/databases/ChEBI_126_classyfire_21_annotations.csv.mod', '-log', 'static/tmp/log.out'])
                output2 = subprocess.check_output(['python', 'metaPathwayMap/scripts/metaPathwayMap.py', '-pwy', 'static/databases/PlantCyc/pathways.dat.cid.all', '-canopus', path, '-jaccard', '0.7', '-log', 'static/tmp/log2.out'])
                return render(request, "mpmUpload/download.html", context)

            elif organism == 'SolCyc':     ###need to add somthing to deal with other databases
                #output = subprocess.check_output(['python', 'metaPathwayMap/scripts/get_similar_pathways_wrapper.py', '-cmp', 'static/databases/compounds.dat', '-pwy', 'static/databases/pathways.dat', '-chemont', 'static/databases/ChemOnt_2_1.obo.mod.tax.organic', '-chebi', 'static/databases/ChEBI_126_classyfire_21_annotations.csv.mod', '-log', 'static/tmp/log.out'])
                output2 = subprocess.check_output(['python', 'metaPathwayMap/scripts/metaPathwayMap.py', '-pwy', 'static/databases/TomatoCyc/pathways.dat.cid.all', '-canopus', path, '-jaccard', '0.7', '-log', 'static/tmp/log2.out'])
                return render(request, "mpmUpload/download.html", context)

            elif organism == 'BrachyCyc':     ###need to add somthing to deal with other databases
                #output = subprocess.check_output(['python', 'metaPathwayMap/scripts/get_similar_pathways_wrapper.py', '-cmp', 'static/databases/compounds.dat', '-pwy', 'static/databases/pathways.dat', '-chemont', 'static/databases/ChemOnt_2_1.obo.mod.tax.organic', '-chebi', 'static/databases/ChEBI_126_classyfire_21_annotations.csv.mod', '-log', 'static/tmp/log.out'])
                output2 = subprocess.check_output(['python', 'metaPathwayMap/scripts/metaPathwayMap.py', '-pwy', 'static/databases/BrachypodiumCyc/pathways.dat.cid.all', '-canopus', path, '-jaccard', '0.7', '-log', 'static/tmp/log2.out'])
                return render(request, "mpmUpload/download.html", context)

    else:
        form = mpmUploadForm()
        return render(request, "mpmUpload/entry.html", {
        "form": form
        })
