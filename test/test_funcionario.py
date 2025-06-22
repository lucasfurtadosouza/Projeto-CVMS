import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from Funcionario import Funcionario
# ...restante do código...

@pytest.fixture(autouse=True)
def clear_funcionarios():
    if hasattr(Funcionario, "_funcionarios_cadastrados"):
        Funcionario._funcionarios_cadastrados.clear()
    else:
        Funcionario._funcionarios_cadastrados = []

def test_cadastrar_funcionario_sucesso():
    funcionario = Funcionario(nome="João", cpf="12345678900", funcao="Dentista", salario=5000.0, dia_pagamento=5, id=1)
    assert funcionario.CadastrarFuncionario() is True
    assert funcionario in Funcionario._funcionarios_cadastrados

def test_cadastrar_funcionario_nome_vazio():
    funcionario = Funcionario(nome="", cpf="12345678901", funcao="Recepcionista", salario=2000.0, dia_pagamento=10, id=2)
    assert funcionario.CadastrarFuncionario() is False

def test_cadastrar_funcionario_funcao_vazia():
    funcionario = Funcionario(nome="Maria", cpf="12345678902", funcao="", salario=2500.0, dia_pagamento=15, id=3)
    assert funcionario.CadastrarFuncionario() is False

def test_cadastrar_funcionario_salario_invalido():
    funcionario = Funcionario(nome="Carlos", cpf="12345678903", funcao="Auxiliar", salario=0, dia_pagamento=20, id=4)
    assert funcionario.CadastrarFuncionario() is False

def test_cadastrar_funcionario_dia_pagamento_invalido():
    funcionario = Funcionario(nome="Ana", cpf="12345678904", funcao="Dentista", salario=4000.0, dia_pagamento=0, id=5)
    assert funcionario.CadastrarFuncionario() is False

def test_cadastrar_funcionario_cpf_vazio():
    funcionario = Funcionario(nome="Pedro", cpf="", funcao="Dentista", salario=4000.0, dia_pagamento=10, id=6)
    assert funcionario.CadastrarFuncionario() is False

def test_cadastrar_funcionario_cpf_duplicado():
    funcionario1 = Funcionario(nome="Lucas", cpf="12345678905", funcao="Dentista", salario=4000.0, dia_pagamento=10, id=7)
    funcionario2 = Funcionario(nome="Julia", cpf="12345678905", funcao="Recepcionista", salario=2000.0, dia_pagamento=15, id=8)
    assert funcionario1.CadastrarFuncionario() is True
    assert funcionario2.CadastrarFuncionario() is False

def test_atualizar_funcionario_sucesso():
    funcionario = Funcionario(nome="Rafa", cpf="12345678906", funcao="Dentista", salario=4000.0, dia_pagamento=10, id=9)
    funcionario.CadastrarFuncionario()
    assert funcionario.AtualizarFuncionario(nome="Rafael", salario=4500.0) is True
    assert funcionario.nome == "Rafael"
    assert funcionario.salario == 4500.0

def test_atualizar_funcionario_nome_vazio():
    funcionario = Funcionario(nome="Bia", cpf="12345678907", funcao="Recepcionista", salario=2000.0, dia_pagamento=15, id=10)
    funcionario.CadastrarFuncionario()
    assert funcionario.AtualizarFuncionario(nome="") is False
    assert funcionario.nome == "Bia"

def test_atualizar_funcionario_funcao_vazia():
    funcionario = Funcionario(nome="Leo", cpf="12345678908", funcao="Auxiliar", salario=1800.0, dia_pagamento=12, id=11)
    funcionario.CadastrarFuncionario()
    assert funcionario.AtualizarFuncionario(funcao="") is False
    assert funcionario.funcao == "Auxiliar"

def test_atualizar_funcionario_salario_invalido():
    funcionario = Funcionario(nome="Tina", cpf="12345678909", funcao="Dentista", salario=4000.0, dia_pagamento=10, id=12)
    funcionario.CadastrarFuncionario()
    assert funcionario.AtualizarFuncionario(salario=0) is False
    assert funcionario.salario == 4000.0

def test_atualizar_funcionario_dia_pagamento_invalido():
    funcionario = Funcionario(nome="Nina", cpf="12345678910", funcao="Recepcionista", salario=2000.0, dia_pagamento=15, id=13)
    funcionario.CadastrarFuncionario()
    assert funcionario.AtualizarFuncionario(dia_pagamento=32) is False
    assert funcionario.dia_pagamento == 15

def test_atualizar_funcionario_cpf_duplicado():
    funcionario1 = Funcionario(nome="Ana", cpf="12345678911", funcao="Dentista", salario=4000.0, dia_pagamento=10, id=14)
    funcionario2 = Funcionario(nome="Clara", cpf="12345678912", funcao="Recepcionista", salario=2000.0, dia_pagamento=15, id=15)
    funcionario1.CadastrarFuncionario()
    funcionario2.CadastrarFuncionario()
    assert funcionario2.AtualizarFuncionario(cpf="12345678911") is False
    assert funcionario2.cpf == "12345678912"

def test_atualizar_funcionario_nao_cadastrado():
    funcionario = Funcionario(nome="Não Cadastrado", cpf="12345678913", funcao="Auxiliar", salario=1800.0, dia_pagamento=12, id=16)
    assert funcionario.AtualizarFuncionario(nome="Novo Nome") is False