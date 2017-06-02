import pytest
from validations.CPF import CPF

def test_cpf_is_blacklist():
	objectCPF = CPF('95469701084')
	assert objectCPF.is_blacklist() is False

def test_cpf_is_not_blacklist():
	objectCPF = CPF('43933309867')
	assert objectCPF.is_blacklist() is True