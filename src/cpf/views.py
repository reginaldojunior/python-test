from django.shortcuts import render
from validations.CPF import CPF


def situation(request, cpf):
    objectCPF = CPF(cpf)

    is_valid = 'FREE'

    if not objectCPF.is_blacklist():
        is_valid = 'BLOCK'

    return render(request, 'index.html', {'response': is_valid})


def home(request):
    return render(request, 'index.html', {'response': 'RUNNING'})
