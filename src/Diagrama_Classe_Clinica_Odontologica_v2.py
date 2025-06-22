"""Definition of meta model 'Diagrama_Classe_Clinica_Odontologica_v2'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import EPackage, EAttribute, MetaEClass, EObject, EReference
from pyecore.ecore import *
from types import String, Integer, EDate, EDouble


name = 'Diagrama_Classe_Clinica_Odontologica_v2'
nsURI = 'http:///Diagrama_Classe_Clinica_Odontologica_v2.ecore'
nsPrefix = 'Diagrama_Classe_Clinica_Odontologica_v2'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


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



