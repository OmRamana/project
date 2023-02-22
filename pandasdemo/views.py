from django.shortcuts import render
from .models import *
import pandas as pd



def home(request):
    item = Student.objects.all().values()
    df = pd.DataFrame(item)

    myDict = {
        'df': df.to_html()       
    }
   
    return render(request, 'index.html', context = myDict)
