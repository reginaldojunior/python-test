import pytest
from validations.CPF import CPF


def test_is_valid():
    objectCPF = CPF('4393330967')
    assert objectCPF.is_valid() is True
