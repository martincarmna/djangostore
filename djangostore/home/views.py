from django.shortcuts import render

# Create your views here.
#Ya jala

def index(resquets):
    return render(resquets, 'home/index.html')

