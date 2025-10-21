from classes import *
import os

banco = Banco("RoubaPoupança", "Xique-xique Bahia")


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
    try:
        if not banco.get_Clientes():
            # ========================== Criando o cliente

            print(f"{banco}\nPrimeira vez aqui? Faça seu cadastro")
            cadastroCliente()
            os.system("pause")
            os.system("clear")
        
    except Exception as e:
        print("Erro: ", e)

    while True:
        try:
            print(f"Bem-vindo ao Banco {banco.get_Nome()}")
            for opcao in opcoes:
                print(f"{n} - {opcao}")
                n+=1
            n = 1
            i = int(input("Selecione uma das opções acima\n--> "))
            match i:
                case 1:
                    for opcao in contas_opcoes:
                        print(f"{n} - {opcao}")
                    i = int(input("Selecione uma das opções acima\n--> "))
                    match i:
                        case 1:
                            pass
                        case 2:
                            pass
                case 2:
                    pass
                case 3:
                    pass
                case _:
                    print("Selecione uma das opções existentes")
                    os.system("pause")
                    os.system("cls")
                    



        except Exception as e:
            print("Erro:", e)