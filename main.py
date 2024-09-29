class Cliente:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, CPF: {self.cpf}, Data de Nascimento: {self.data_nascimento}")


class Conta:
    def __init__(self, saldo, numero, agencia, cliente):
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} efetuado com sucesso!")
            transacao = f"Saque de R$ {valor:.2f} da conta {self.numero}"
            self.historico.adicionar_transacao(transacao)

    def depositar(self, valor):
        if valor < 1:
            print("Valor inválido")
        else:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} efetuado com sucesso!")
            transacao = f"Depósito de R$ {valor:.2f} na conta {self.numero}"
            self.historico.adicionar_transacao(transacao)

    def exibir_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")


class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, limite, limite_saques):
        super().__init__(saldo, numero, agencia, cliente)
        self.limite = limite
        self.limite_saques = limite_saques


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)
        print("Transação adicionada ao histórico.")

    def exibir_historico(self):
        if self.transacoes:
            print("Histórico de Transações:")
            for t in self.transacoes:
                print(t)
        else:
            print("Nenhuma transação encontrada.")


def criar_usuario():
    nome = input("Nome do cliente: ")
    cpf = input("CPF do cliente: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    cliente = Cliente(nome, cpf, data_nascimento)
    usuarios.append(cliente)
    print("Usuário criado com sucesso!")


def criar_conta_corrente():
    saldo = float(input("Saldo inicial: "))
    numero = int(input("Número da conta: "))
    agencia = input("Agência: ")
    cpf_cliente = input("Informe o CPF do cliente: ")
    cliente_encontrado = next((cliente for cliente in usuarios if cliente.cpf == cpf_cliente), None)

    if cliente_encontrado:
        limite = float(input("Informe o limite da conta corrente: "))
        limite_saques = int(input("Informe o limite de saques: "))
        conta_corrente = ContaCorrente(saldo, numero, agencia, cliente_encontrado, limite, limite_saques)
        contas.append(conta_corrente)
        print("Conta Corrente criada com sucesso!")
    else:
        print("Cliente não encontrado.")


menu = """
[d] Depositar 
[s] Sacar
[e] Extrato
[q] Sair
[u] Criar Usuário
[c] Criar Conta Corrente

=> """

usuarios = []
contas = []

while True:
    opcao = input(menu)

    if opcao == "d":
        numero_conta = int(input("Informe o número da conta: "))
        valor = float(input("Informe o valor do depósito: "))
        for conta in contas:
            if conta.numero == numero_conta:
                conta.depositar(valor)
                break
        else:
            print("Conta não encontrada.")

    elif opcao == "s":
        numero_conta = int(input("Informe o número da conta: "))
        valor = float(input("Informe o valor do saque: "))
        for conta in contas:
            if conta.numero == numero_conta:
                conta.sacar(valor)
                break
        else:
            print("Conta não encontrada.")

    elif opcao == "e":
        numero_conta = int(input("Informe o número da conta: "))
        for conta in contas:
            if conta.numero == numero_conta:
                conta.exibir_saldo()
                conta.historico.exibir_historico()
                break
        else:
            print("Conta não encontrada.")

    elif opcao == "u":
        criar_usuario()

    elif opcao == "c":
        criar_conta_corrente()

    elif opcao == "q":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")
