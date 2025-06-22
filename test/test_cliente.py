import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from Cliente import Cliente

class DummyPessoa:
    def __init__(self, nome=None, cpf=None, telefone=None, id=None):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.id = id

# Patch Pessoa base class for isolated testing if needed
Cliente._clientes_cadastrados = []
Cliente._tipos_sanguineos_validos = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']

@pytest.fixture(autouse=True)
def clear_clientes():
    Cliente._clientes_cadastrados.clear()

def test_cadastrar_cliente_sucesso(monkeypatch):
    cliente = Cliente(nome="João", cpf="12345678900", tipo_sanguineo="A+", necessidade_especial="Nenhuma", id=1)
    assert cliente.CadastrarCliente() is True
    assert cliente in Cliente._clientes_cadastrados

def test_cadastrar_cliente_nome_vazio():
    cliente = Cliente(nome="", cpf="12345678900", tipo_sanguineo="A+", id=2)
    assert cliente.CadastrarCliente() is False

def test_cadastrar_cliente_cpf_vazio():
    cliente = Cliente(nome="Maria", cpf="", tipo_sanguineo="O-", id=3)
    assert cliente.CadastrarCliente() is False

def test_cadastrar_cliente_tipo_sanguineo_invalido():
    cliente = Cliente(nome="Carlos", cpf="98765432100", tipo_sanguineo="X+", id=4)
    assert cliente.CadastrarCliente() is False

def test_cadastrar_cliente_cpf_duplicado():
    cliente1 = Cliente(nome="Ana", cpf="11122233344", tipo_sanguineo="B+", id=5)
    cliente2 = Cliente(nome="Ana 2", cpf="11122233344", tipo_sanguineo="B-", id=6)
    assert cliente1.CadastrarCliente() is True
    assert cliente2.CadastrarCliente() is False

def test_atualizar_cliente_sucesso():
    cliente = Cliente(nome="Pedro", cpf="55566677788", tipo_sanguineo="AB-", id=7)
    cliente.CadastrarCliente()
    assert cliente.AtualizarCliente(nome="Pedro Silva", telefone="99999999") is True
    assert cliente.nome == "Pedro Silva"
    assert hasattr(cliente, "telefone") and cliente.telefone == "99999999"

def test_atualizar_cliente_nome_vazio():
    cliente = Cliente(nome="Lucas", cpf="33344455566", tipo_sanguineo="O+", id=8)
    cliente.CadastrarCliente()
    assert cliente.AtualizarCliente(nome="") is False
    assert cliente.nome == "Lucas"

def test_atualizar_cliente_tipo_sanguineo_invalido():
    cliente = Cliente(nome="Julia", cpf="22233344455", tipo_sanguineo="A-", id=9)
    cliente.CadastrarCliente()
    assert cliente.AtualizarCliente(tipo_sanguineo="Z-") is False
    assert cliente.tipo_sanguineo == "A-"

def test_atualizar_cliente_cpf_duplicado():
    cliente1 = Cliente(nome="Rafa", cpf="10101010101", tipo_sanguineo="O-", id=10)
    cliente2 = Cliente(nome="Bia", cpf="20202020202", tipo_sanguineo="A+", id=11)
    cliente1.CadastrarCliente()
    cliente2.CadastrarCliente()
    assert cliente2.AtualizarCliente(cpf="10101010101") is False
    assert cliente2.cpf == "20202020202"

def test_atualizar_cliente_nao_cadastrado():
    cliente = Cliente(nome="Não Cadastrado", cpf="30303030303", tipo_sanguineo="B-", id=12)
    assert cliente.AtualizarCliente(nome="Novo Nome") is False