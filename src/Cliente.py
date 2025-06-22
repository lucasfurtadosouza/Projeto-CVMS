from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import EPackage, EAttribute
from pyecore.ecore import *
from types import String
from Pessoa import Pessoa


name = 'Diagrama_Classe_Clinica_Odontologica_v2'
nsURI = 'http:///Diagrama_Classe_Clinica_Odontologica_v2.ecore'
nsPrefix = 'Diagrama_Classe_Clinica_Odontologica_v2'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)

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

