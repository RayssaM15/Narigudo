from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == "GET":
        return render(request, 'registro-chaves.html')
    elif request.method == "POST":
        return render(request, 'passo_2.html')