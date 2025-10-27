from classes import *
import os

banco = Banco("RoubaPoupança", "Xique-Xique Bahia")


def cadastroCliente(banco: Banco): # Função para cadastro de clientes
    print("Insira suas informações abaixo\n")
    nome = input("insira seu nome: ")
    sobrenome = input("Sobrenome: ")
    cpf = int(input("CPF: "))
    idade = int(input("Idade: "))
    endereco = input("Endereço: ")

    cliente = Cliente(nome, sobrenome, cpf, idade, endereco)
    banco.cadastrar_Cliente(cliente)


def acessarConta(banco: Banco): # Função para acesso de conta
    try:
        os.system("cls")
        numero = int(input("Insira o número da conta: "))
        senha = input("Insira a senha da conta: ")

        for conta in banco.get_Clientes():
            if conta.get_Numero() == numero and conta.get_Senha() == senha:
                return conta
            else:
                print("Sua conta não existe ou não foi encontrada")
    except Exception as e:
        print("Erro", e)




def menu(banco: Banco):
    # ================================== Definindo futuras opções
    opcoes = ["Criar conta", "Acessar conta existente", "Sair"]
    contas_opcoes = ["Conta corrente", "Conta poupança"]
    n = 1
    while True:
        try:
            if not banco.get_Clientes():
                # ========================== Criando o cliente

                print(f"{banco.get_Nome()}\nPrimeira vez aqui? Faça seu cadastro")
                cadastroCliente()
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
            i = int(input("Selecione uma das opções acima\n--> "))
            match i:
                case 1: #Criar conta
                    for num, opcao in enumerate(contas_opcoes, 1):
                        print(f"{num} - {opcao}")
                        i = int(input("Selecione uma das contas acima a serem criadas\n--> "))
                        match i:
                            case 1: #Criar conta Corrente

                                #Fazer funções CRIAR_CONTA CORRENTE E CRIAR_CONTA POUPANÇA

                                
                                conta = Corrente()
                            case 2: #Criar conta Poupança
                                pass

                case 2: #Acessar Conta existente
                    for num, opcao in enumerate(contas_opcoes, 1):
                        print(f"{num} - {opcao}")
                        i = int(input("Selecione uma conta a ser acessada\n--> "))
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