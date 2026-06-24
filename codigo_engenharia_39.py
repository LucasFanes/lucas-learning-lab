# Módulo de Gestão de Contas Bancárias (POO)

class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:
    def __init__(self, numero, saldo, clientes):
        self.numero = numero
        self.saldo = saldo
        self.clientes = clientes

    def exibir_saldo(self):
        print(f'Conta: {self.numero} ')
        print('Cliente(s): ', end='')
        if isinstance(self.clientes, list):
            for cliente in self.clientes:
                print(f'{cliente.nome} | ', end='')
        else:
            print(self.clientes.nome, end=' | ')
        print(f'Saldo: R$ {self.saldo:.2f} \n')

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

# Exemplo de uso do sistema bancário:
cliente1 = Cliente("Lucas Fanes", "11999999999")
cliente2 = Cliente("Maria Silva", "11888888888")

# Conta com dois titulares
minha_conta = Conta(numero="1234-5", saldo=1000.0, clientes=[cliente1, cliente2])
minha_conta.exibir_saldo()
minha_conta.sacar(250.0)
minha_conta.exibir_saldo()