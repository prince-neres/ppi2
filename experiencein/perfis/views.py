from django.shortcuts import render
from perfis.models import Perfil

def index(request):
    return render(request, 'index.html')

def exibir(request, perfil_id):

    perfil = Perfil()

    if perfil_id == 1:
        perfil = Perfil('Fábio Henrique', 'fabio.oliveira@ifb.edu.br', '222222', 'IFB')
    if perfil_id == 2:
        perfil = Perfil('Elon Musk', 'elon.musk@tesla.com', '333333', 'Tesla') 

    return render(request, 'perfil.html', {'perfil' : perfil})