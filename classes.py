from abc import ABC, abstractmethod
from typing import override


class Conta:
    pass

class Cliente:
    pass



# ========================================== Classe banco e atributos
class Banco:
    def __init__(self, nome, endereco):
        self.__nome = nome
        self.__endereco = endereco
        self.__clientes: list[Cliente] = []

    def get_Nome(self):
        return self.__nome
    
    def get_Endereco(self):
        return self.__endereco

    def cadastrar_Cliente(self, cliente: Cliente):
        self.__clientes.append(cliente)

    def get_Clientes(self):
        return self.__clientes
        


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



class Conta(OperacoesFinanceiras): # ========================================== Classe conta, tipos de conta (Corrente e Poupança) e seus métodos
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

    @abstractmethod
    def get_Numero(self):
        pass

    @abstractmethod
    def get_Senha(self):
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

    @override
    def get_Numero(self):
        return self.__numero
    
    @override
    def get_Senha(self):
        return self.__senha



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
    def __init__(self, nome: str, sobrenome: str, CPF: int, idade: int, endereco: str):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = CPF
        self.__idade = idade
        self.__endereco = endereco
        self.__contas: list[Conta] = []

    def get_Nome(self):
        return self.__nome

    def get_Sobrenome(self):
        return self.__sobrenome
    
    def get_CPF(self):
        return self.__cpf
    
    def get_Idade(self):
        return self.__idade
    
    def get_Endereco(self):
        return self.__endereco
    
    def set_Nome(self, nome):
        self.__nome = nome

    def set_Sobrenome(self, sobrenome):
        self.__sobrenome = sobrenome
    
    def set_CPF(self, cpf):
        self.__cpf = cpf
    
    def set_Idade(self, idade):
        self.__idade = idade
    
    def set_Endereco(self, endereco):
        self.__endereco = endereco