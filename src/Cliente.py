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
        """
        Cadastra o cliente atual na lista de clientes da clínica.
        Valida os dados obrigatórios antes do cadastro.
        
        Returns:
            bool: True se cadastrado com sucesso, False caso contrário
        """
        try:
            # Validações básicas
            if not self.nome or not self.nome.strip():
                raise ValueError("Nome é obrigatório para cadastrar cliente")
            
            if not self.cpf or not self.cpf.strip():
                raise ValueError("CPF é obrigatório para cadastrar cliente")
            
            # Validação do tipo sanguíneo
            if self.tipo_sanguineo and self.tipo_sanguineo not in self._tipos_sanguineos_validos:
                raise ValueError(f"Tipo sanguíneo inválido. Tipos válidos: {', '.join(self._tipos_sanguineos_validos)}")
            
            # Verifica se já existe cliente com mesmo CPF
            for cliente in Cliente._clientes_cadastrados:
                if cliente.cpf == self.cpf:
                    raise ValueError(f"Já existe cliente cadastrado com CPF: {self.cpf}")
            
            # Adiciona à lista de clientes cadastrados
            Cliente._clientes_cadastrados.append(self)
            
            print(f"Cliente {self.nome} cadastrado com sucesso!")
            print(f"ID: {self.id}")
            print(f"CPF: {self.cpf}")
            if self.tipo_sanguineo:
                print(f"Tipo Sanguíneo: {self.tipo_sanguineo}")
            if self.necessidade_especial:
                print(f"Necessidade Especial: {self.necessidade_especial}")
            
            return True
            
        except ValueError as e:
            print(f"Erro ao cadastrar cliente: {e}")
            return False
        except Exception as e:
            print(f"Erro inesperado ao cadastrar cliente: {e}")
            return False

    def AtualizarCliente(self, **kwargs):
        """
        Atualiza os dados do cliente já cadastrado.

        Args:
            **kwargs: Campos a serem atualizados (nome, cpf, telefone, tipo_sanguineo, necessidade_especial, etc.)

        Returns:
            bool: True se atualizado com sucesso, False caso contrário
        """
        try:
            # Verifica se o cliente está cadastrado
            if self not in Cliente._clientes_cadastrados:
                raise ValueError("Cliente não encontrado na base de dados")

            # Armazena valores antigos para rollback em caso de erro
            valores_antigos = {}

            # Atualiza os campos fornecidos
            for campo, novo_valor in kwargs.items():
                if hasattr(self, campo):
                    valores_antigos[campo] = getattr(self, campo)

                    # Validações específicas
                    if campo == 'nome' and (not novo_valor or not novo_valor.strip()):
                        raise ValueError("Nome não pode estar vazio")

                    if campo == 'cpf' and (not novo_valor or not novo_valor.strip()):
                        raise ValueError("CPF não pode estar vazio")

                    if campo == 'tipo_sanguineo' and novo_valor and novo_valor not in self._tipos_sanguineos_validos:
                        raise ValueError(f"Tipo sanguíneo inválido. Tipos válidos: {', '.join(self._tipos_sanguineos_validos)}")

                    # Verifica CPF duplicado se estiver sendo alterado
                    if campo == 'cpf':
                        for cliente in Cliente._clientes_cadastrados:
                            if cliente != self and cliente.cpf == novo_valor:
                                raise ValueError(f"Já existe cliente com CPF: {novo_valor}")

                    setattr(self, campo, novo_valor)
                else:
                    print(f"Aviso: Campo '{campo}' não existe na classe Cliente")

            print(f"Cliente {self.nome} atualizado com sucesso!")

            # Mostra os dados atualizados
            print(f"ID: {self.id}")
            print(f"Nome: {self.nome}")
            print(f"CPF: {self.cpf}")
            if hasattr(self, 'telefone') and self.telefone:
                print(f"Telefone: {self.telefone}")
            if self.tipo_sanguineo:
                print(f"Tipo Sanguíneo: {self.tipo_sanguineo}")
            if self.necessidade_especial:
                print(f"Necessidade Especial: {self.necessidade_especial}")

            return True

        except ValueError as e:
            # Rollback das alterações
            for campo, valor_antigo in valores_antigos.items():
                setattr(self, campo, valor_antigo)
            print(f"Erro ao atualizar cliente: {e}")
            return False
        except Exception as e:
            # Rollback das alterações
            for campo, valor_antigo in valores_antigos.items():
                setattr(self, campo, valor_antigo)
            print(f"Erro inesperado ao atualizar cliente: {e}")
            return False