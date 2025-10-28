from classes import *
import os

banco = Banco("RoubaPoupança", "Xique-Xique Bahia")


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


def acessarConta(self, cliente: Cliente): # Função para acesso de conta
    try:
        os.system("cls")
        numero = tratarErros("Insira o número da conta: ")
        senha = input("Insira a senha da conta: ")

        conta = cliente.get_Conta(numero, senha)
        if conta:
            print("Acesso concedido à conta Nº", {conta.get_Numero()})

    except Exception as e:
        print("Erro: ", e)



def menu(banco: Banco):
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
                                
                                #Fazer funções CRIAR_CONTA CORRENTE E CRIAR_CONTA POUPANÇA


                                conta = Corrente()
                            case 2: #Criar conta Poupança
                                pass

                case 2: #Acessar Conta existente
                    for num, opcao in enumerate(contas_opcoes, 1):
                        print(f"{num} - {opcao}")
                        i = tratarErros("Selecione uma conta a ser acessada\n--> ")
                        match i:
                            case 1: #Acessar conta Corrente
                                pass
                            case 2: #Acessar conta Poupança
                                pass
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