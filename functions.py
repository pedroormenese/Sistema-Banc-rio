from classes import *
import os

banco = Banco("RoubaPoupança", "Xique-Xique Bahia")
cliente1 = Cliente("Roberto", "Carlos", 12345678901, 69, "Ponta-Grossa")
cliente2 = Cliente("Cleide", "Schwagnazer", 12354678901, 43, "Pitamanhagaba")
cliente3 = Cliente("Valter", "Victor", 13245678901, 86, "Campos do Jordão")

def tratarErros(mensagem: str):
    while True:
        try:
            i = input(mensagem)
            mensagem = int(i)
            return mensagem
        except Exception:
            os.system("cls")
            print("Utilize somente números")
            os.system("pause")
            os.system("cls")

def tratarErrosOP(mensagem: str):
    while True:
        try:
            i = input(mensagem)
            mensagem = float(i)
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
    while True:
        try:
            os.system("cls")
            numero = tratarErros("Insira o CPF da conta: ")
            senha = input("Insira a senha da conta: ")

            conta = cliente.get_Conta(numero, senha)
            if conta:
                print("Acesso concedido à conta Nº", conta.get_Numero())
                return conta
            else:
                print("A conta não foi encontrada ou não existe.")

        except Exception as e:
            print(f"Erro ao acessar a conta. Verifique se ela existe\nDetalhes do erro: {e}")
            os.system("Pause")

def criar_Corrente(cliente: Cliente):
    print("Criando conta Corrente")
    senha = input("Defina sua senha: ")
    corrente = Corrente(cliente.get_CPF(), senha, 0)
    cliente.add_conta(corrente)

def criar_Poupanca(cliente: Cliente):
    print("Criando conta Poupança")
    senha = input("Defina sua senha: ")
    poupanca = Poupanca(cliente.get_CPF(), senha, 0)
    cliente.add_conta(poupanca)



def mainmenu(conta: Conta):
    while True:
        try:
            opcoes = ["Sacar", "Depositar", "Transferência", "Extrato", "Sair"]
            for num, opcao in enumerate(opcoes, 1):
                print(f"{num}. {opcao}\n")
            i = tratarErros("Selecione uma opção\n--> ")
            match i:
                case 1: #Fazer saque
                    print("-------SAQUE-------")
                    print((f"Você tem: R${conta.get_Saldo():.2f}\n Qual valor que você gostaria de sacar?"))
                    quantidade = tratarErros("Insira o valor no espaço abaixo:\n\n--> ")

                    if quantidade <= 0:
                        print("Valor inválido")
                        os.system("pause")
                        os.system("cls")
                        continue
                    
                    resultado = conta.sacar(quantidade)
                    print(resultado)

                case 2: #Fazer depósito
                    print("-------DEPÓSITO-------")
                    print((f"Você tem: R${conta.get_Saldo()}\n Qual valor que você gostaria de depositar?"))
                    quantidade = tratarErrosOP("Insira o valor no espaço abaixo:\n\n--> ")
                    resultado = conta.depositar(quantidade)
                    print(resultado)

                case 3: #Fazer transferência
                    print("-------TRANSFERÊNCIA-------")
                    print((f"Você tem: R${conta.get_Saldo()}\n Qual valor que você gostaria de transferir?"))
                    quantidade = tratarErrosOP("Insira o valor no espaço abaixo:\n\n--> ")
                    num_conta = tratarErros("Insira o número da conta para qual você gostaria de realizar a transferência\n\n--> ")
                    procedimento = conta.transferir(quantidade, banco.get_Clientes(num_conta))
                    if procedimento == False:
                        print("Não foi possível efetuar a transferência. Verifique se a conta destino existe")
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
            if not banco.get_AllClientes():
                # ========================== Criando o cliente

                print(f"{banco.get_Nome()}\nPrimeira vez aqui? Faça seu cadastro")
                cliente = cadastroCliente(banco)
                os.system("pause")
                os.system("cls")
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
                                corrente = criar_Corrente(cliente)
                        case 2: #Criar conta Poupança
                                poupanca = criar_Poupanca(cliente)

                case 2: #Acessar Conta existente
                    acesso = acessarConta(cliente)
                    if acesso:
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
