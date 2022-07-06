from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def getname(request):
    return render(request, 'players/getname.html')
