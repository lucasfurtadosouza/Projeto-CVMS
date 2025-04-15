
from .Diagrama_Classe_Clinica_Odontologica_v2 import getEClassifier, eClassifiers
from .Diagrama_Classe_Clinica_Odontologica_v2 import name, nsURI, nsPrefix, eClass
from .Diagrama_Classe_Clinica_Odontologica_v2 import Pessoa, Cliente, Funcionario, Consulta, Procedimentos


from . import Diagrama_Classe_Clinica_Odontologica_v2

__all__ = ['Pessoa', 'Cliente', 'Funcionario', 'Consulta', 'Procedimentos']

eSubpackages = []
eSuperPackage = None
Diagrama_Classe_Clinica_Odontologica_v2.eSubpackages = eSubpackages
Diagrama_Classe_Clinica_Odontologica_v2.eSuperPackage = eSuperPackage

Consulta.procedimentos.eType = Procedimentos

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
