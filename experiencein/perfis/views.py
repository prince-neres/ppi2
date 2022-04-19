from django.shortcuts import render 

def index(request): 
    return render(request, 'index.html')

def exibir(request, perfil_id):
    print('ID do perfil recebido: {}'.format(perfil_id))
    return render(request, 'perfil.html')