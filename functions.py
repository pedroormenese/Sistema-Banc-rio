from classes import *
import os

banco = Banco("RoubaPoupança", "Xique-Xique Bahia")
cliente1 = Cliente("Roberto", "Carlos", 12345678901, 69, "Ponta-Grossa")
cliente2 = Cliente("Cleide", "Schwagnazer", 12354678901, 43, "Pitamanhagaba")
cliente3 = Cliente("Valter", "Victor", 13245678901, 86, "Campos do Jordão")

def tratarErros(mensagem: str):
    while True:
        try:
            mensagem = input(mensagem)
            mensagem = int(mensagem)
            return mensagem
        except Exception:
            os.system("cls")
            print("Utilize somente números")
            os.system("pause")
            os.system("cls")


def cadastroCliente(banco: Banco): # Função para cadastro de clientes
    while True:
        try:
            print("Insira suas informações abaixo\n")
            nome = input("insira seu nome: ")
            sobrenome = input("Sobrenome: ")
            cpf = tratarErros("CPF: ")
            idade = tratarErros("Idade: ")
            endereco = input("Endereço: ")

            cliente = Cliente(nome, sobrenome, cpf, idade, endereco)
            banco.cadastrar_Cliente(cliente)
            return cliente
        except Exception as e:
            print("Erro", e)


def acessarConta(cliente: Cliente): # Função para acesso de conta
    try:
        os.system("cls")
        numero = tratarErros("Insira o CPF da conta: ")
        senha = input("Insira a senha da conta: ")

        conta = cliente.get_Conta(numero, senha)
        if conta:
            print("Acesso concedido à conta Nº", {conta.get_Numero()})
            return conta

    except Exception as e:
        print("Erro: ", e)

def criar_Corrente(cliente: Cliente):
    print("Criando conta Corrente")
    senha = input("Defina sua senha: ")
    corrente = Corrente(cliente.get_CPF(), senha, 0)
    cliente.add_conta(corrente)

def criar_Poupanca(cliente: Cliente):
    print("Criando conta Poupança")
    senha = input("Defina sua senha: ")
    poupanca = Corrente(cliente.get_CPF(), senha, 0)
    cliente.add_conta(poupanca)



def mainmenu(cliente: Cliente):
    while True:
        try:
            opcoes = ["Sacar", "Depositar", "Transferência", "Extrato", "Sair"]
            for num, opcao in enumerate(opcoes, 1):
                print(f"{num}. {opcao}\n")
                i = tratarErros("Selecione uma opção\n--> ")
                match i:
                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
                    case 4:
                        pass
                    case 5:
                        os.system("cls")
                        print("Retornando ao menu inicial...")
                        os.system("pause")
                        os.system("cls")
                        break
        except Exception as e:
            print("Erro", e)





def startmenu(banco: Banco):

    # ================================== Definindo futuras opções
    opcoes = ["Criar conta", "Acessar conta existente", "Sair"]
    contas_opcoes = ["Conta corrente", "Conta poupança"]
    while True:
        try:
            if not banco.get_Clientes():
                # ========================== Criando o cliente

                print(f"{banco.get_Nome()}\nPrimeira vez aqui? Faça seu cadastro")
                cliente = cadastroCliente()
                os.system("pause")
                os.system("clear")
                break
            
        except Exception as e:
            print("Erro: ", e)

    while True:
        try:
            print(f"Bem-vindo ao Banco {banco.get_Nome()}")
            for num, opcao in enumerate(opcoes, 1):
                print(f"{num} - {opcao}")
            i = tratarErros("Selecione uma das opções acima\n--> ")
            match i:
                case 1: #Criar conta
                    for num, opcao in enumerate(contas_opcoes, 1):
                        print(f"{num} - {opcao}")
                        i = tratarErros("Selecione uma das contas acima a serem criadas\n--> ")
                        match i:
                            case 1: #Criar conta Corrente
                                corrente = Corrente(cliente)
                            case 2: #Criar conta Poupança
                                poupanca = Poupanca(cliente)

                case 2: #Acessar Conta existente
                    acesso = acessarConta(cliente)
                    mainmenu(acesso) #Acessar conta com o return da conta da função acessarConta

                case 3: #Sair
                    print("Saindo...")
                    os.system("pause")
                    break
                case _:
                    print("Selecione uma das opções existentes")
                    os.system("pause")
                    os.system("cls")

        except Exception as e:
            print("Erro:", e)