from abc import ABC, abstractmethod
from typing import override

# ========================================== Interface das operações financeiras
class OperacoesFinanceiras(ABC):
    @abstractmethod
    def sacar(self):
        pass

    @abstractmethod
    def transferir(self):
        pass

    @abstractmethod
    def depositar(self):
        pass

# ========================================== Classe conta, tipos de conta (Corrente e Poupança) e seus métodos
class Conta(OperacoesFinanceiras):
    @abstractmethod
    def __init__(self, numero: int, senha: str, saldo: float):
        self.__numero = numero
        self.__senha = senha
        self.__saldo = saldo

    @abstractmethod
    def get_Numero(self):
        pass
    
    @abstractmethod
    def genhat_Senha(self):
        pass
    
    @abstractmethod
    def get_Saldo(self):
        pass

class Corrente(Conta): # ======================= Conta Corrente
    def __init__(self, numero, senha, saldo):
        super().__init__(numero, senha, saldo)

    @override
    def get_Numero(self):
        return self.__numero
    
    @override
    def get_Senha(self):
        return self.__senha
    
    @override
    def get_Saldo(self):
        return self.__saldo
    
    @override
    def sacar(self):
        pass

    @override
    def transferir(self):
        pass

    @override
    def depositar(self):
        pass

class Poupanca(Conta): # ======================= Conta Poupança
    def __init__(self, numero, senha, saldo):
        super().__init__(numero, senha, saldo)

    @override
    def get_Numero(self):
        return self.__numero
    
    @override
    def get_Senha(self):
        return self.__senha
    
    @override
    def get_Saldo(self):
        return self.__saldo

    @override
    def sacar(self):
        pass

    @override
    def transferir(self):
        pass

    @override
    def depositar(self):
        pass

# ========================================== Classe cliente e seus métodos
class Cliente:
    def __init__(self, nome: str, sobrenome: str, CPF: int, idade: int, endereco: str, *contas):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = CPF
        self.__idade = idade
        self.__endereco = endereco
        self.__contas: Conta = contas

    def depositar(self, quantidade: float, conta: Conta):
        pass

    def sacar(self, quantidade: float, conta: Conta):
        pass

# ========================================== Classe banco e atributos
class Banco:
    def __init__(self, nome, endereco, *contas):
        self.__nome = nome
        self.__endereco = endereco
        self.__contas = contas