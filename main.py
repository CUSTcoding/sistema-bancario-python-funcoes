from sistema_bancario import Conta


def menu():

    conta = Conta()
    
    while True:
        print("""
        ===== MENU =====
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [0] Sair
        =================
        """)

        option = input("Escolha uma opção: ")

        try:
            if option == '1':
                valor = float(input("Digita o valor do depósito: "))
                conta.depositar(valor)
            
            elif option == '2':
                valor = float(input("Digite o valor do saque: "))
                conta.sacar(valor)
            
            elif option == '3':
                conta.exibir_extrato()

            
            elif option == '0':
                print("Saindo...")
                break

            else:
                print("Opção inválida. Tente novamente.")

        except ValueError as e:
            print(f"Entrada inválida. Digite um número.: {e}")


if __name__ == "__main__":
    menu()
