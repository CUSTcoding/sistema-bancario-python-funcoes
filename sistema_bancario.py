class Conta:

    def __init__(self, limite_saque=500.0, numero_saques=3):
        self.saldo = 0.0
        self.limite_saque = limite_saque
        self.numero_saques = numero_saques
        self.saques_realizados = 0
        self.extrato = []

    def depositar(self, valor):
        if valor <= 0:
            print("O valor do depósito deve ser positivo.")
            return

        self.saldo += valor
        self.extrato.append(f"Depósito: {valor:.2f} MZN")

        print(f"Depósito de {valor:.2f} MZN realizado com sucesso.")


    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
            return

        if valor > self.saldo:
            print("Saldo insuficiente.")
            return

        if valor > self.limite_saque:
            print("Valor excede o limite de saque.")
            return

        if self.saques_realizados >= self.numero_saques:
            print("Número máximo de saques diários atingido.")
            return

        self.saldo -= valor
        self.saques_realizados += 1
        self.extrato.append(f"Saque: {valor:.2f} MZN")

        print(f"Saque de {valor:.2f} MZN realizado com sucesso.")


    def exibir_extrato(self):
        print("\n===== EXTRATO =====")
        if not self.extrato:
            print("Nenhuma transação realizada.")
        else:
            for transacao in self.extrato:
                print(transacao)
        print(f"\nSaldo atual: {self.saldo:.2f} MZN")
        print("===================")
