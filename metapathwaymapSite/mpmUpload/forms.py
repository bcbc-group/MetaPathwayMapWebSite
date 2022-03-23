# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import mpmUpload

class mpmUploadForm(ModelForm):
    class Meta:
        model = mpmUpload
        fields = '__all__'
