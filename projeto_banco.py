menu = """
==== Menu ====
[1] Sacar
[2] Depositar
[3] Extrato
[0] Sair
"""
print(menu) 
saldo = 1700
extrato = ""
limite_saque = 500
saques_diarios = 0
LIMITE_SAQUES_DIARIOS = 3
while True:
    opcao = input("Digite o número da operação desejada: ")
    if opcao == "1":
        saque = float(input("Digite o valor que deseja sacar: "))
        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite_saque
        excedeu_saques = saques_diarios >= LIMITE_SAQUES_DIARIOS        
        if excedeu_saldo:
            print("Seu saldo é insuficiente para realizar essa operação.")
        elif excedeu_limite:
            print("O valor do saque excede o limite permitido para o seu tipo de conta.")
        elif excedeu_saques:
            print("O número máximo de saques diários foi atingido.")
        elif saque > 0:
            saldo -= saque
            saques_diarios += 1
            extrato += f"Saque: R$ {saque:.2f} realizado.\n"
            print(f"Saque de R$ {saque:.2f} realizado.")
        else:
            print("Valor inválido. O valor do saque deve ser maior que zero.") 
    elif opcao == "2":
        deposito = float(input("Digite o valor que deseja depositar: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Deposito: R$ {deposito:.2f}\n"
            print(f"Deposito de R$ {deposito:.2f} realizado.")
        else:
            print("Valor inválido. O valor depositado deve ser maior do que R$ 0,00.")
    elif opcao == "3":
        print("\n===================== Extrato ===============================================")
        print("Não foram realizadas movimentações na conta" if not extrato else extrato)
        print(f"Saldo disponivel em sua conta é de R$ {saldo:.2f}")
        print("===============================================================================")
    elif opcao == "0":
        print("Saindo do sistema...")
        print("Obrigado por utilizar nosso sistema, volte sempre!")
        break
    else:
        print("A opção escolhida é invalida, tente novamente.")