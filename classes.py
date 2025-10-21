from abc import ABC, abstractmethod
from typing import override


class Conta:
    pass
# ========================================== Classe banco e atributos
class Banco:
    def __init__(self, nome, endereco, *contas):
        self.__nome = nome
        self.__endereco = endereco
        self.__contas: Conta = contas


# ========================================== Interface das operações financeiras
class OperacoesFinanceiras(ABC):
    @abstractmethod
    def sacar(self, quantidade: float):
        pass

    @abstractmethod
    def transferir(self, quantidade: float, conta: Conta):
        pass

    @abstractmethod
    def depositar(self, quantidade: float):
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
    def get_Saldo(self):
        pass

class Corrente(Conta): # ======================= Conta Corrente
    def __init__(self, numero, senha, saldo):
        super().__init__(numero, senha, saldo)

    @override
    def get_Numero(self):
        return self.__numero
    
    @override
    def get_Saldo(self):
        return self.__saldo
    
    @override
    def sacar(self, quantidade: float):
        if self.get_Saldo() - quantidade >= 0:
            self.__saldo -= quantidade
            return "Saque realizado com sucesso"
        else:
            return "Saldo insuficiente"

    @override
    def transferir(self, quantidade: float, conta: Conta):
        if self.get_Saldo() - quantidade >= 0:
            self.__saldo -= quantidade
            conta.__saldo += quantidade
            return "Transferência realizada com sucesso"
        else:
            return "Saldo insuficiente"

    @override
    def depositar(self, quantidade: float):
        self.__saldo += quantidade

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
    def sacar(self, quantidade: float):
        if self.get_Saldo() >= 100:
            if quantidade <= self.get_Saldo():
                quantidade -= self.__saldo
                return "Saque realizado com sucesso"
            else:
                return "Saldo insuficiente"
        else:
            return "Você deve possuir no mínimo R$100 para realizar um saque"
        

    @override
    def transferir(self, quantidade: float, conta: Conta):
        if self.get_Saldo() >= 100:
            if quantidade <= self.get_Saldo():
                quantidade -= self.__saldo
                conta.__saldo += quantidade
                return "Transferência realizada com sucesso"
            else:
                return "Saldo insuficiente"
        else:
            return "Você deve possuir no mínimo R$100 para realizar uma transferência"

    @override
    def depositar(self, quantidade: float):
        self.__saldo += quantidade

# ========================================== Classe cliente e seus métodos
class Cliente:
    def __init__(self, nome: str, sobrenome: str, CPF: int, idade: int, endereco: str, *contas):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = CPF
        self.__idade = idade
        self.__endereco = endereco
        self.__contas: Conta = contas