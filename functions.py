from classes import *
import os


# ======================================================================= Contas de teste para efetuar transferências a partir da sua conta principal
banco = Banco("RoubaPoupança", "Xique-Xique Bahia")
cliente1 = Cliente("Roberto", "Carlos", 12345678901, 69, "Ponta-Grossa")
cliente2 = Cliente("Cleide", "Schwagnazer", 12354678901, 43, "Pitamanhagaba")
cliente3 = Cliente("Valter", "Victor", 13245678901, 86, "Campos do Jordão")

corrente1 = Corrente(12345678901, "test", 0)
corrente2 = Corrente(12354678901, "test", 0)
corrente3 = Corrente(13245678901, "test", 0)

cliente1.add_conta(corrente1)
cliente2.add_conta(corrente2)
cliente3.add_conta(corrente3)

banco.cadastrar_Cliente(cliente1)
banco.cadastrar_Cliente(cliente2)
banco.cadastrar_Cliente(cliente3)


# ================================================== Funções
def cls():
    clear = "cls" if os.name == "nt" else "clear"
    os.system(clear)

def pause():
    p = "pause" if os.name == "nt" else "read a"
    os.system(p)

def tratarErros(mensagem: str):
    while True:
        try:
            i = input(mensagem)
            mensagem = int(i)
            return mensagem
        except Exception:
            cls()
            print("Utilize somente números")
            pause()
            cls()

def tratarErrosOP(mensagem: str):
    while True:
        try:
            i = input(mensagem)
            mensagem = float(i)
            return mensagem
        except Exception:
            cls()
            print("Utilize somente números")
            pause()
            cls()


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
            cls()
            numero = tratarErros("Insira o Número da conta: ")
            senha = input("Insira a senha da conta: ")

            conta = cliente.get_Conta(numero, senha)
            if conta:
                cls()
                print("Acesso concedido à conta Nº", conta.get_Numero())
                pause()
                cls()
                return conta
            else:
                print("A conta não foi encontrada ou não existe.")
                pause()

        except Exception as e:
            print(f"Erro ao acessar a conta. Verifique se ela existe\nDetalhes do erro: {e}")
            pause()

def criar_Corrente(cliente: Cliente):
    print("Criando conta Corrente")
    senha = input("Defina sua senha: ")
    corrente = Corrente(cliente.get_CPF(), senha, 0)
    cliente.add_conta(corrente)
    print(f"Conta Nº{corrente.get_Numero()} com sucesso.")
    pause()

def criar_Poupanca(cliente: Cliente):
    print("Criando conta Poupança")
    senha = input("Defina sua senha: ")
    poupanca = Poupanca(cliente.get_CPF(), senha, 0)
    cliente.add_conta(poupanca)
    print(f"Conta Nº{poupanca.get_Numero()} com sucesso.")
    pause()



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
                        pause()
                        cls()
                        continue
                    
                    resultado = conta.sacar(quantidade)
                    print(resultado)
                    pause()
                    cls()

                case 2: #Fazer depósito
                    print("-------DEPÓSITO-------")
                    print((f"Você tem: R${conta.get_Saldo()}\n Qual valor que você gostaria de depositar?"))
                    quantidade = tratarErrosOP("Insira o valor no espaço abaixo:\n\n--> ")
                    resultado = conta.depositar(quantidade)
                    print(resultado)
                    pause()
                    cls()

                case 3: #Fazer transferência
                    print("-------TRANSFERÊNCIA-------")
                    print((f"Você tem: R${conta.get_Saldo()}\n Qual valor que você gostaria de transferir?"))
                    quantidade = tratarErrosOP("Insira o valor no espaço abaixo:\n\n--> ")
                    if quantidade <= 0:
                        print("Valor insuficiente para efetuar uma transferência")
                        pause()
                        cls()
                        continue

                    num_conta = tratarErros("Insira o número da conta para qual você gostaria de realizar a transferência\n\n--> ")
                    conta_destino = None
                    for cliente_destino in banco.get_AllClientes():
                        conta_destino = cliente_destino.get_Destinatario(num_conta)
                        if conta_destino:
                            break

                    if conta_destino is None:
                        print("Conta destino não encontrada.")
                        pause()
                        cls()
                        continue

                    resultado = conta.transferir(quantidade, conta_destino)
                    print(resultado)
                    pause()
                    cls()

                case 4:
                    if not conta.get_Extrato():
                        print("Sua conta não possui nenhum histórico de operações financeiras")
                        continue
                    for num, extrato in enumerate(conta.get_Extrato(), 1):
                        print(f"{num} - {extrato}\n")
                        pause()
                        cls()
                case 5:
                    cls()
                    print("Retornando ao menu inicial...")
                    pause()
                    cls()
                    break
        except Exception as e:
            print("Erro", e)





def startmenu(banco: Banco):

    # ================================== Definindo futuras opções
    opcoes = ["Criar conta", "Acessar conta existente", "Sair"]
    contas_opcoes = ["Conta corrente", "Conta poupança"]
    while True:
        try:
            cls()
           
                # ========================== Criando o cliente
            print(f"{banco.get_Nome()}\n\nPrimeira vez aqui? Faça seu cadastro")
            cliente = cadastroCliente(banco)
            pause()
            cls()
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
                    cls()
                    for num, opcao in enumerate(contas_opcoes, 1):
                        print(f"{num} - {opcao}")
                    i = tratarErros("Selecione uma das contas acima a serem criadas\n--> ")
                    match i:
                        case 1: #Criar conta Corrente
                                corrente = criar_Corrente(cliente)
                        case 2: #Criar conta Poupança
                                poupanca = criar_Poupanca(cliente)

                case 2: #Acessar Conta existente
                    cls()
                    acesso = acessarConta(cliente)
                    if acesso:
                        mainmenu(acesso) #Acessar conta com o return da conta da função acessarConta

                case 3: #Sair
                    print("Saindo...")
                    pause()
                    cls()
                    break
                case _:
                    print("Selecione uma das opções existentes")
                    pause()
                    cls()

        except Exception as e:
            print("Erro:", e)
