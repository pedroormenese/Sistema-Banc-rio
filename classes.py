from abc import ABC, abstractmethod
from typing import override
from datetime import *


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
    def __init__(self, cpf: int, senha: str, saldo: float):
        _prox_numero = 1000
        self.__cpf = cpf
        self.__senha = senha
        self.__saldo = saldo
        self.__numero = Conta._prox_numero
        _prox_numero += 1

    @abstractmethod
    def get_Numero(self):
        pass

    @abstractmethod
    def get_CPF(self):
        pass

    @abstractmethod
    def get_Saldo(self):
        pass

    @abstractmethod
    def get_Senha(self):
        pass

    @abstractmethod
    def sacar(self, quantidade: float):
        pass
    
    @abstractmethod
    def depositar(self, quantidade: float): 
        pass
    
    @abstractmethod
    def transferir(self, quantidade: float, conta: Conta):
        pass


class Corrente(Conta): # ======================= Conta Corrente
    def __init__(self, cpf, senha, saldo):
        super().__init__(cpf, senha, saldo)

    @override
    def get_Numero(self):
        return self.__numero
    
    @override
    def get_CPF(self):
        return self.__cpf
    
    @override
    def get_Saldo(self):
        return self.__saldo
        
    @override
    def depositar(self, quantidade: float):
        self.__saldo += quantidade
    
    @override
    def get_Senha(self):
        return self.__senha
    
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
            conta.depositar(quantidade)
            return "Transferência realizada com sucesso"
        else:
            return "Saldo insuficiente"



class Poupanca(Conta): # ======================= Conta Poupança
    def __init__(self, cpf, senha, saldo):
        super().__init__(cpf, senha, saldo)

    @override
    def get_Numero(self):
        return self.__numero

    @override
    def get_CPF(self):
        return self.__cpf

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
                self.__saldo -= quantidade
                return "Saque realizado com sucesso"
            else:
                return "Saldo insuficiente"
        else:
            return "Você deve possuir no mínimo R$100 para realizar um saque"
        
    @override
    def depositar(self, quantidade: float):
        self.__saldo += quantidade

    @override
    def transferir(self, quantidade: float, conta: Conta):
        if self.get_Saldo() >= 100:
            if quantidade <= self.get_Saldo():
                quantidade -= self.__saldo
                conta.depositar(quantidade)
                return "Transferência realizada com sucesso"
            else:
                return "Saldo insuficiente"
        else:
            return "Você deve possuir no mínimo R$100 para realizar uma transferência"



# ========================================== Classe cliente e seus métodos
class Cliente:
    def __init__(self, nome: str, sobrenome: str, CPF: int, idade: int, endereco: str):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = CPF
        self.__idade = idade
        self.__endereco = endereco
        self.__contas: list[Conta] = [] #associação

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

    def add_conta(self, conta: Conta):
        self.__contas.append(conta)
        print(f"Conta {conta.get_CPF()} associada ao cliente {self.get_Nome()} {self.get_Sobrenome()}")

    def remover_conta(self, cpf: int):
        for conta in self.__contas:
            if conta.get_CPF() == cpf:
                self.__contas.remove(conta)
                print(f"Conta {cpf} removida")
                return
        print("Conta não encontrada")

    def listar_contas(self): #Listar todas as contas do cliente
        if not self.__contas:
            print("Nenhuma conta associada")
            return
        
        print(f"Contas de {self.get_Nome()} {self.get_Sobrenome()}")
        for i, conta in enumerate(self.__contas, 1):
            if isinstance(conta, Corrente):
                tipo = "Corrente"
            elif isinstance(conta, Poupanca):
                tipo = "Poupança"
            else:
                tipo = "Tipo desconhecido"
        
            print(f"{i}. {tipo} Conta Nº: {conta.get_CPF()} | Saldo: R${conta.get_Saldo()}")

    def get_Conta(self, cpf: int, senha: str):
        for conta in self.__contas:
            if conta.get_CPF() == cpf and conta.get_Senha() == senha:
                return conta
            
    
