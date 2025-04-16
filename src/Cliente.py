"""Definition of meta model 'Diagrama_Classe_Clinica_Odontologica_v2'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from types import String, Integer


name = 'Diagrama_Classe_Clinica_Odontologica_v2'
nsURI = 'http:///Diagrama_Classe_Clinica_Odontologica_v2.ecore'
nsPrefix = 'Diagrama_Classe_Clinica_Odontologica_v2'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


class Pessoa(EObject, metaclass=MetaEClass):

    id = EAttribute(eType=Integer, unique=True, derived=False, changeable=True)
    nome = EAttribute(eType=String, unique=True, derived=False, changeable=True)
    cpf = EAttribute(eType=String, unique=True, derived=False, changeable=True)
    data_nasc = EAttribute(eType=EDate, unique=True, derived=False, changeable=True)
    endereco = EAttribute(eType=String, unique=True, derived=False, changeable=True)
    telefone = EAttribute(eType=String, unique=True, derived=False, changeable=True)
    email = EAttribute(eType=String, unique=True, derived=False, changeable=True)

    def __init__(self, *, id=None, nome=None, cpf=None, data_nasc=None, endereco=None, telefone=None, email=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if nome is not None:
            self.nome = nome

        if cpf is not None:
            self.cpf = cpf

        if data_nasc is not None:
            self.data_nasc = data_nasc

        if endereco is not None:
            self.endereco = endereco

        if telefone is not None:
            self.telefone = telefone

        if email is not None:
            self.email = email


class Consulta(EObject, metaclass=MetaEClass):

    id = EAttribute(eType=Integer, unique=True, derived=False, changeable=True)
    data = EAttribute(eType=EDate, unique=True, derived=False, changeable=True)
    horario = EAttribute(eType=String, unique=True, derived=False, changeable=True)
    valor = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    forma_pagamento = EAttribute(eType=String, unique=True, derived=False, changeable=True)
    id_cliente_fk = EAttribute(eType=Integer, unique=True, derived=False, changeable=True)
    id_funcionario_fk = EAttribute(eType=Integer, unique=True, derived=False, changeable=True)
    procedimentos = EReference(ordered=False, unique=True,
                               containment=True, derived=False, upper=-1)

    def __init__(self, *, id=None, data=None, horario=None, valor=None, forma_pagamento=None, id_cliente_fk=None, id_funcionario_fk=None, procedimentos=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if data is not None:
            self.data = data

        if horario is not None:
            self.horario = horario

        if valor is not None:
            self.valor = valor

        if forma_pagamento is not None:
            self.forma_pagamento = forma_pagamento

        if id_cliente_fk is not None:
            self.id_cliente_fk = id_cliente_fk

        if id_funcionario_fk is not None:
            self.id_funcionario_fk = id_funcionario_fk

        if procedimentos:
            self.procedimentos.extend(procedimentos)

    def CadastrarConsulta(self):

        raise NotImplementedError('operation CadastrarConsulta(...) not yet implemented')

    def AtualizarConsulta(self):

        raise NotImplementedError('operation AtualizarConsulta(...) not yet implemented')

    def DeletarConsulta(self):

        raise NotImplementedError('operation DeletarConsulta(...) not yet implemented')


class Procedimentos(EObject, metaclass=MetaEClass):

    id = EAttribute(eType=Integer, unique=True, derived=False, changeable=True)
    nome = EAttribute(eType=String, unique=True, derived=False, changeable=True)
    valor = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    duracao = EAttribute(eType=String, unique=True, derived=False, changeable=True)
    descricao = EAttribute(eType=String, unique=True, derived=False, changeable=True)

    def __init__(self, *, id=None, nome=None, valor=None, duracao=None, descricao=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if nome is not None:
            self.nome = nome

        if valor is not None:
            self.valor = valor

        if duracao is not None:
            self.duracao = duracao

        if descricao is not None:
            self.descricao = descricao

    def CadastrarProcedimento(self):

        raise NotImplementedError('operation CadastrarProcedimento(...) not yet implemented')

    def AtualizarProcedimento(self):

        raise NotImplementedError('operation AtualizarProcedimento(...) not yet implemented')

    def DeletarProcedimento(self):

        raise NotImplementedError('operation DeletarProcedimento(...) not yet implemented')


class Cliente(Pessoa):

    tipo_sanguineo = EAttribute(eType=String, unique=True, derived=False, changeable=True)
    necessidade_especial = EAttribute(eType=String, unique=True, derived=False, changeable=True)

    def __init__(self, *, tipo_sanguineo=None, necessidade_especial=None, **kwargs):

        super().__init__(**kwargs)

        if tipo_sanguineo is not None:
            self.tipo_sanguineo = tipo_sanguineo

        if necessidade_especial is not None:
            self.necessidade_especial = necessidade_especial

    def CadastrarCliente(self):

        raise NotImplementedError('operation CadastrarCliente(...) not yet implemented')

    def AtualizarCliente(self):

        raise NotImplementedError('operation AtualizarCliente(...) not yet implemented')

    def DeletarCliente(self):

        raise NotImplementedError('operation DeletarCliente(...) not yet implemented')


class Funcionario(Pessoa):

    funcao = EAttribute(eType=String, unique=True, derived=False, changeable=True)
    salario = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    dia_pagamento = EAttribute(eType=Integer, unique=True, derived=False, changeable=True)

    def __init__(self, *, funcao=None, salario=None, dia_pagamento=None, **kwargs):

        super().__init__(**kwargs)

        if funcao is not None:
            self.funcao = funcao

        if salario is not None:
            self.salario = salario

        if dia_pagamento is not None:
            self.dia_pagamento = dia_pagamento

    def CadastrarFuncionario(self):

        raise NotImplementedError('operation CadastrarFuncionario(...) not yet implemented')

    def AtualizarFuncionario(self):

        raise NotImplementedError('operation AtualizarFuncionario(...) not yet implemented')

    def DeletarFuncionario(self):

        raise NotImplementedError('operation DeletarFuncionario(...) not yet implemented')
