from django.shortcuts import render
from .models import Chave


def index(request):
    if request.method == "GET":
        return render(request, 'registro-chaves.html')
    elif request.method == "POST":
        return render(request, 'passo_2.html')
    
def listagem(request):
    return render(request, "listagem.html", 
                {"chaves": Chave.objects.all()})