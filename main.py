menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Informe o quanto você gostaria de depositar: "))

        if deposito <= 0.0:
            print("Valor inválido. Por favor, forneça um valor positivo")
            continue

        saldo += deposito
        msg = f"Depósito de R${deposito:0.2f} realizado."
        print(msg)
        extrato += msg + "\n"

    elif opcao == "s":
        saques_restantes = LIMITE_SAQUES - numero_saques

        if saques_restantes == 0:
            print(
                "Você não tem direitos à mais saques por hoje. Por favor, tente de novo amanhã."
            )
            continue

        print(
            f"Você ainda tem direito à {saques_restantes} saque{'s' if saques_restantes > 1 else ''}"
        )
        saque = float(
            input(
                f"Informe o quanto você gostaria de sacar (limite de R${limite:0.2f}): "
            )
        )

        if saque <= 0.0 or saque > 500.0:
            print(
                f"Valor inválido. Por favor, forneça um valor positivo até R${limite:0.2f}."
            )
            continue
        elif saque > saldo:
            print("Saldo insuficiente")
            continue

        saldo -= saque
        numero_saques += 1
        msg = f"Saque de R${saque:0.2f} realizado."
        print(msg)
        extrato += msg + "\n"

    elif opcao == "e":
        msg = (
            "EXTRATO".center(50, "-")
            + "\n"
            + extrato
            + f"SALDO R${saldo:0.2f}\n"
            + "".center(50, "-")
        )
        print(msg)

    elif opcao == "q":
        print("ENCERRANDO SISTEMA".center(50, "-"))
        break

    else:
        print("Operação inválida. Por favor selection novamente a operação desejada.")

print("SISTEMA ENCERRADO".center(50, "-"))
