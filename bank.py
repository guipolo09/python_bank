menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

===>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
error_message = "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
operation_failed = "\nOperação falhou! "
success_message = "\n=) =) =) =) =) =) =) =) =) =) =) =) =) =) =) =) =) =) =) =) =) =) =) =) =) =) =) =) =) "
operation_fulfiled = "\nOperação realizada com sucesso! "

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("\nInforme o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(success_message)
            print(operation_fulfiled)
            print(
                f"\nDeposito efetuado com sucesso. Você depositou R$ {valor:.2f}")
            print(success_message)
        else:
            print(error_message)
            print(operation_failed)
            print("\nO valor informado é inválido.")
            print(error_message)
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print(error_message)
            print(operation_failed)
            print("\nVocê não tem saldo suficiente.")
            print(error_message)
        elif excedeu_limite:
            print(error_message)
            print(operation_failed)
            print("\nO valor do saque excede o limite diário.")
            print(error_message)
        elif excedeu_saques:
            print(error_message)
            print(operation_failed)
            print("\nNumero de saques diário excedido.")
            print(error_message)
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(success_message)
            print(
                f"\nVocê sacou R$ {valor:.2f} da sua conta.")
            print(success_message)
        else:
            print(error_message)
            print(operation_failed)
            print("\nO valor informado é inválido.")
            print(error_message)
    elif opcao == "e":
        print("\n===============EXTRATO===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================================")
    elif opcao == "q":
        break
    else:
        print(error_message)
        print(operation_failed)
        print("\nOpção inválida, por favor, selecione novamente a opção desejada.")
        print(error_message)
