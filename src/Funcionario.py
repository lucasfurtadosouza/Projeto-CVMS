from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import EPackage, EAttribute
from pyecore.ecore import *
from types import String, Integer, EDouble
from Pessoa import Pessoa


name = 'Diagrama_Classe_Clinica_Odontologica_v2'
nsURI = 'http:///Diagrama_Classe_Clinica_Odontologica_v2.ecore'
nsPrefix = 'Diagrama_Classe_Clinica_Odontologica_v2'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)\

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
