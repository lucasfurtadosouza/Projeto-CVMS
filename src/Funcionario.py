from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import EPackage, EAttribute, EString, EInt, EDouble
from pyecore.ecore import *
from Pessoa import Pessoa

name = 'Diagrama_Classe_Clinica_Odontologica_v2'
nsURI = 'http:///Diagrama_Classe_Clinica_Odontologica_v2.ecore'
nsPrefix = 'Diagrama_Classe_Clinica_Odontologica_v2'

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)

class Funcionario(Pessoa):

    funcao = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    salario = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    dia_pagamento = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)

    def __init__(self, *, funcao=None, salario=None, dia_pagamento=None, **kwargs):

        super().__init__(**kwargs)

        if funcao is not None:
            self.funcao = funcao

        if salario is not None:
            self.salario = salario

        if dia_pagamento is not None:
            self.dia_pagamento = dia_pagamento

    def CadastrarFuncionario(self):
        """
        Cadastra o funcionário atual na lista de funcionários da clínica.
        Valida os dados obrigatórios antes do cadastro.
        
        Returns:
            bool: True se cadastrado com sucesso, False caso contrário
        """
        try:
            # Validações básicas
            if not self.nome or not self.nome.strip():
                raise ValueError("Nome é obrigatório para cadastrar funcionário")
            
            if not self.funcao or not self.funcao.strip():
                raise ValueError("Função é obrigatória para cadastrar funcionário")
            
            if self.salario is None or self.salario <= 0:
                raise ValueError("Salário deve ser maior que zero")
            
            if self.dia_pagamento is None or not (1 <= self.dia_pagamento <= 31):
                raise ValueError("Dia de pagamento deve estar entre 1 e 31")
            
            if not self.cpf or not self.cpf.strip():
                raise ValueError("CPF é obrigatório para cadastrar funcionário")
            
            # Verifica se já existe funcionário com mesmo CPF
            for funcionario in Funcionario._funcionarios_cadastrados:
                if funcionario.cpf == self.cpf:
                    raise ValueError(f"Já existe funcionário cadastrado com CPF: {self.cpf}")
            
            # Adiciona à lista de funcionários cadastrados
            Funcionario._funcionarios_cadastrados.append(self)
            
            print(f"Funcionário {self.nome} cadastrado com sucesso!")
            print(f"ID: {self.id}, Função: {self.funcao}, Salário: R$ {self.salario:.2f}")
            
            return True
            
        except ValueError as e:
            print(f"Erro ao cadastrar funcionário: {e}")
            return False
        except Exception as e:
            print(f"Erro inesperado ao cadastrar funcionário: {e}")
            return False
        

    def AtualizarFuncionario(self, **kwargs):
        """
        Atualiza os dados do funcionário já cadastrado.
        
        Args:
            **kwargs: Campos a serem atualizados (nome, funcao, salario, dia_pagamento, etc.)
        
        Returns:
            bool: True se atualizado com sucesso, False caso contrário
        """
        try:
            # Verifica se o funcionário está cadastrado
            if self not in Funcionario._funcionarios_cadastrados:
                raise ValueError("Funcionário não encontrado na base de dados")
            
            # Armazena valores antigos para rollback em caso de erro
            valores_antigos = {}
            
            # Atualiza os campos fornecidos
            for campo, novo_valor in kwargs.items():
                if hasattr(self, campo):
                    valores_antigos[campo] = getattr(self, campo)
                    
                    # Validações específicas
                    if campo == 'salario' and (novo_valor is None or novo_valor <= 0):
                        raise ValueError("Salário deve ser maior que zero")
                    
                    if campo == 'dia_pagamento' and (novo_valor is None or not (1 <= novo_valor <= 31)):
                        raise ValueError("Dia de pagamento deve estar entre 1 e 31")
                    
                    if campo == 'nome' and (not novo_valor or not novo_valor.strip()):
                        raise ValueError("Nome não pode estar vazio")
                    
                    if campo == 'funcao' and (not novo_valor or not novo_valor.strip()):
                        raise ValueError("Função não pode estar vazia")
                    
                    if campo == 'cpf' and (not novo_valor or not novo_valor.strip()):
                        raise ValueError("CPF não pode estar vazio")
                    
                    # Verifica CPF duplicado se estiver sendo alterado
                    if campo == 'cpf':
                        for funcionario in Funcionario._funcionarios_cadastrados:
                            if funcionario != self and funcionario.cpf == novo_valor:
                                raise ValueError(f"Já existe funcionário com CPF: {novo_valor}")
                    
                    setattr(self, campo, novo_valor)
                else:
                    print(f"Aviso: Campo '{campo}' não existe na classe Funcionario")
            
            print(f"Funcionário {self.nome} atualizado com sucesso!")
            return True
            
        except ValueError as e:
            # Rollback das alterações
            for campo, valor_antigo in valores_antigos.items():
                setattr(self, campo, valor_antigo)
            print(f"Erro ao atualizar funcionário: {e}")
            return False
        except Exception as e:
            # Rollback das alterações
            for campo, valor_antigo in valores_antigos.items():
                setattr(self, campo, valor_antigo)
            print(f"Erro inesperado ao atualizar funcionário: {e}")
            return False
