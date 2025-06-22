from pyecore.ecore import EAttribute, EObject, MetaEClass, EInt, EString
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from datetime import date

name = 'Diagrama_Classe_Clinica_Odontologica_v2'
nsURI = 'http:///Diagrama_Classe_Clinica_Odontologica_v2.ecore'
nsPrefix = 'Diagrama_Classe_Clinica_Odontologica_v2'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)

class Pessoa(EObject, metaclass=MetaEClass):

    id = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    nome = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    cpf = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    data_nasc = EAttribute(eType=EString, unique=True, derived=False, changeable=True)  # Use EString para datas
    endereco = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    telefone = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    email = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, id=None, nome=None, cpf=None, data_nasc=None, endereco=None, telefone=None, email=None):
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
