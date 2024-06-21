from django.shortcuts import render

def index(request):
    #PATH
    return render(request, 'vinme/index.html')
